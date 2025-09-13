from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm

def main():

    genetic_algorithm = GeneticAlgorithm(population_size=500, 
                                         mutation_rate=0.2, 
                                         crossover_rate=0.75, 
                                         budget=100, alpha=0.9, 
                                         crossover_type='one_point',
                                         selection_method='roulette',
                                         tournament_size=4,
                                         elitism_count=2,
                                         team_formation='4-3-3')
    
    genetic_algorithm.run(generations=500)

    #['3-4-3', '3-5-2', '4-3-3', '4-4-2', '4-5-1', '5-3-2', '5-4-1']

    print(genetic_algorithm.best_individual.__str__())

    if genetic_algorithm.best_individual is not None:
        print("Preço do time: ", genetic_algorithm.best_individual.get_total_price())

if __name__ == "__main__":
    main()
