import numpy as np
from models.team.Team import Team
import services.cartola_services as cartola_services
import random
import sys

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count = None, max_known_value = None,
                 selection_method='roulette', tournament_size=None, budget = 100, alpha = 0.5, crossover_type='one_point'):

        self.population_size = population_size

        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.selection_method = selection_method
        self.tournament_size = tournament_size
        self.best_individual = None
        self.best_fitness = None
        self.current_population = []
        self.alpha = alpha
        self.budget = budget
        self.crossover_type = crossover_type

    def initialize_population(self):
        """
        Cria a população inicial de atletas.
        """
        
        current_population = []

        database = cartola_services.fetch_athletes()

        team_formation = [
            {
                'position': 'GOL',
                'quantity': 1
            },
            {
                'position': 'ZAG',
                'quantity': 2
            },
            {
                'position': 'LAT',
                'quantity': 2
            },
            {
                'position': 'MEI',
                'quantity': 3
            },
            {
                'position': 'ATA',
                'quantity': 3
            }
        ]

        for _ in range(self.population_size):

            team = Team([])

            for position in team_formation:

                database_by_position = [athlete for athlete in database if athlete.position == position['position'] and athlete.status == "Provável"]

                for _ in range(position['quantity']):
                    athlete = random.choice(database_by_position)
                    team.add_athlete(athlete)

            current_population.append(team)

        return current_population

    def calculate_team_score(self, team):
        """
        Calcula a pontuação do time.
        """
        score = 0
        for athlete in team.athletes:
            # SCORE=α⋅media_rodadas+(1−α)⋅pontos_ultima_rodada
            score += athlete.avg_score * self.alpha + athlete.score * (1 - self.alpha)
        return score
    
    def calculate_team_budget(self, team):
        """
        Calcula o budget do time.
        """
        budget = 0
        for athlete in team.athletes:
            budget += athlete.price
        return budget

    def calculate_team_fitness(self, team):
        """
        Calcula a aptidão do time.
        """

        team_score = self.calculate_team_score(team)
        team_budget = self.calculate_team_budget(team)

        # fitness = (1 - ((preço_time- valor_disponivel)/valor_disponivel)) * score
        pen_budget = 1 - ((team_budget - self.budget) / self.budget)

        if pen_budget < 0:
            pen_budget = 0

        if pen_budget > 1:
            pen_budget = 1

        fitness = (1 - pen_budget) * team_score

        return fitness

    def fitness(self):
        """
        Calcula a aptidão (fitness) da população.
        Atualiza o melhor indivíduo, o erro do melhor e o erro médio da população.
        """
        fitness_values = [self.calculate_team_fitness(team) for team in self.current_population]
        best_idx = np.argmax(fitness_values)

        self.best_individual = self.current_population[best_idx]
        self.best_fitness = fitness_values[best_idx]

        return fitness_values


    def selection(self, fitness_values):
        """
        Seleciona os indivíduos para reprodução, com base no método definido.
        """

        if self.selection_method == 'roulette':
            self.current_population = self.roulette_selection(fitness_values)
        elif self.selection_method == 'tournament':
            self.current_population = self.tournament_selection(fitness_values)

    def roulette_selection(self, fitness_values):
        """
        Implementa a seleção por roleta.
        """

        probabilities = fitness_values / np.sum(fitness_values)
        selected_individuals = np.random.choice(len(self.current_population), size=self.population_size, p=probabilities)

        population_array = np.array(self.current_population)
        return population_array[selected_individuals].tolist()

    def tournament_selection(self, fitness_values):
        """
        Implementa a seleção por torneio.
        """

        selected = []

        for _ in range(self.population_size):

            participants_indices = np.random.choice(len(self.current_population), self.tournament_size, replace=False)
            participants_fitness = fitness_values[participants_indices]

            winner_indice = participants_indices[np.argmax(participants_fitness)] # type: ignore
            selected.append(self.current_population[winner_indice])

        return np.array(selected)

    def one_point_crossover(self, parent1, parent2):
        """
        Realiza o cruzamento por um ponto.
        """
        point = random.randint(1, len(parent1.athletes) - 1)

        child1 = Team(parent1.athletes[point:] + parent2.athletes[:point])
        child2 = Team(parent2.athletes[point:] + parent1.athletes[:point])

        return child1, child2
    
    def two_point_crossover(self, parent1, parent2):
        """
        Realiza o cruzamento por dois pontos.
        """
        point1 = random.randint(1, len(parent1.athletes) - 1)
        point2 = random.randint(1, len(parent1.athletes) - 1)

        if point1 > point2:
            point1, point2 = point2, point1

        child1 = Team(parent1.athletes[:point1] + parent2.athletes[point1:point2] + parent1.athletes[point2:])
        child2 = Team(parent2.athletes[:point1] + parent1.athletes[point1:point2] + parent2.athletes[point2:])

        return child1, child2

    def crossover(self):
        """
        Realiza o cruzamento entre dois pais (one-point ou two-point).
        """
        np.random.shuffle(self.current_population)
        children = []
        n = len(self.current_population)
        i = 0
        while i < n - 1:
            parent1 = self.current_population[i]
            parent2 = self.current_population[i+1]
            if random.random() < self.crossover_rate:
                if self.crossover_type == 'one_point':
                    child1, child2 = self.one_point_crossover(parent1, parent2)
                elif self.crossover_type == 'two_point':
                    child1, child2 = self.two_point_crossover(parent1, parent2)
                else: 
                    children.extend([child1, child2])
            else:
                children.extend([parent1, parent2])
            i += 2
        self.current_population = children

        if n % 2 == 1:
            children.append(self.current_population[-1])
        self.current_population = children

    def mutation(self):
        """
        Aplica a mutação no indivíduo.
        """
        
        for team in self.current_population:
            if random.random() < self.mutation_rate:
                position = random.sample(range(len(team.athletes)), 2)

                athlete1 = team.athletes[position[0]]
                team.athletes[position[0]] = team.athletes[position[1]]
                team.athletes[position[1]] = athlete1

    def run(self, generations, update_callback=None):
        """
        Executa o algoritmo genético por um número definido de gerações.
        """
        elite_individuals = None
        self.current_population = self.initialize_population()

        for _ in range(generations):

            print(f"Geração {_ + 1}")
            
            # Calcula a aptidão de cada indivíduo, 
            fitness_values = self.fitness()

            # Elitismo: mantém os melhores indivíduos da geração anterior
            if self.elitism_count and self.elitism_count > 0:
                elite_indices = np.argsort(fitness_values)[-self.elitism_count:]
                elite_individuals = self.current_population[elite_indices]

            # Faz a seleção, crossover e mutação
            self.selection(fitness_values)
            self.crossover() 
            self.mutation()

            if elite_individuals is not None:
                new_fitness_values = 0
                worst_indices = np.argsort(new_fitness_values)[:self.elitism_count]
                for i, idx in enumerate(worst_indices):
                    self.current_population[idx] = elite_individuals[i]

            self.fitness()

        return self.best_individual, self.best_fitness