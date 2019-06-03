from individual import Individual
from functions import *


def generate_initial_population():
    for i in range(population_size):
        instance = Individual(0, 0, 0, 0)
        individuals.append(instance)


def calculate_fitness():
    for item in individuals:
        item.update_fitness()


def show_all_population():
    for item in individuals:
        item.show_genes()
        item.show_fitness()


def parent_selection():
    parents = []
    for i in range(tornument_size):
        parents.append(individuals[0])
    parents = sort_by_fitness(parents)


def crossover(parents):
    child = Individual(0, 0, 0, 0)
    index_list = [0, 0, 1, 1]
    # shuffle index list
    child.genes = [parents[index_list[0]].genes[0],
                   parents[index_list[1]].genes[1],
                   parents[index_list[2]].genes[2],
                   parents[index_list[3]].genes[3]]
    return child


def mutation(child):
    # make a random number
    random = 5
    for i in range(4):
        if random % (1/mutation_rate) is 1:
            child.genes[i] += noise


def survival(population):
    population = sort_by_fitness(population)
    best_population = population[0:population_size]
    return best_population


number_of_generations = 5000
population_size = 50
tornument_size = 3
mutation_rate = 0.1
noise = 1
individuals = []
generate_initial_population()
calculate_fitness()
survival(individuals)
show_all_population()
