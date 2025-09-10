from genetic_algorithm.GeneticAlgorithm import GeneticAlgorithm

def main():

    genetic_algorithm = GeneticAlgorithm(population_size=100, mutation_rate=0.02, crossover_rate=0.8, budget=100, alpha=0.2, crossover_type='one_point')
    genetic_algorithm.run(generations=100)

    print(genetic_algorithm.best_fitness)
    print(genetic_algorithm.best_individual.__str__())
    print(genetic_algorithm.best_individual.get_total_price())

if __name__ == "__main__":
    main()
