import random
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np


class Polynomial:
    def __init__(self, a, b, c, d):
        self.genes = [a, b, c, d]
        self.fitness = -1

    def update_fitness(self):
        self.fitness = 1/(1 + mean_square_error(self))

    def show_genes(self):
        print(self.genes[0], "x^3 + ", self.genes[1], "x^2 + ", self.genes[2], "x + ", self.genes[3])

    def show_fitness(self):
        print(self.fitness)

    def get_result(self, x):
        return (self.genes[0] * pow(x, 3)) \
               + (self.genes[1] * pow(x, 2))\
               + (self.genes[2] * pow(x, 1))\
               + (self.genes[3] * pow(x, 0))


def mean_square_error(individual):
    total_error = 0
    for i in range(len(data)):
        total_error += abs(data[i] - individual.get_result(i))
    return total_error/len(data)


def sort_by_fitness(population):
    population.sort(key=lambda x: x.fitness)
    return population


def get_input(address):
    points = []
    with open(address) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for item in range(len(row)):
                points.append(float(row[item]))
    return points


def generate_initial_population():
    population = []
    for i in range(population_size):
        coefficients = [random.randint(0, 5),
                        random.randint(0, 5),
                        random.randint(0, 5),
                        random.randint(0, 5)]
        instance = Polynomial(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        population.append(instance)
    return population


def calculate_fitness(population):
    for item in population:
        item.update_fitness()


def show_all_population(population):
    for item in population:
        item.show_genes()
        item.show_fitness()
    print("======================")


def parent_selection(population):
    parents = []
    for i in range(population_size):
        tournament = []
        for j in range(tournament_size):
            tournament.append(population[random.randint(0, len(individuals) - 1)])
        tournament = sort_by_fitness(tournament)
        parents.append(tournament[1])
    return parents


def crossover(parents):
    child = Polynomial(0, 0, 0, 0)
    index_list = [0, 0, 1, 1]
    random.shuffle(index_list)
    child.genes = [parents[index_list[0]].genes[0],
                   parents[index_list[1]].genes[1],
                   parents[index_list[2]].genes[2],
                   parents[index_list[3]].genes[3]]
    return child


def mutation(mutant):
    for index in range(len(mutant.genes)):
        rand = random.randint(1, 11)
        if rand % (1/mutation_rate) == 1:
            mutant.genes[index] += noise
    return mutant


def survival(population):
    population = sort_by_fitness(population)
    best_population = population[int(population_size * 0.5):int(population_size * 1.5)]
    return best_population


def genetic(population):
    best_fitness = []
    worst_fitness = []
    for counter in range(number_of_generations):
        population = parent_selection(population)
        for i in range(0, population_size, 2):
            parent = [population[i], population[i + 1]]
            child = mutation(crossover(parent))
            child.update_fitness()
            population.append(child)
        population = survival(population)
        best_fitness.append(population[-1].fitness)
        worst_fitness.append(population[0].fitness)
    # draw_fitness(best_fitness, worst_fitness)
    population[population_size - 1].show_genes()
    population[population_size - 1].show_fitness()
    return population


def draw_fitness(best, worst):
    xs = []
    ybs = []
    yws = []
    for i in range(number_of_generations):
        xs.append(i)
        ybs.append(best[i])
        yws.append(worst[i])
    plt.scatter(xs, ybs)
    plt.scatter(xs, yws)
    plt.show()


def draw_data():
    xs = []
    ys = []
    best = individuals[-1]
    a = best.genes[0]
    b = best.genes[1]
    c = best.genes[2]
    d = best.genes[3]
    x = np.linspace(0, 100, 256, endpoint=True)
    y = (a * (x * x * x)) + (b * (x * x) + (c * x) + d)
    plt.plot(x, y, '-g', label=r'$y')
    axes = plt.gca()
    axes.set_xlim([x.min(), x.max()])
    axes.set_ylim([y.min(), y.max()])
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(0, len(data)):
        xs.append(i)
        ys.append(data[i])
    plt.scatter(xs, ys)
    plt.show()


number_of_generations = 5000
population_size = 50
tournament_size = 2
mutation_rate = 0.1
noise = 0.1

input_address = sys.argv[1]
data = get_input(input_address)

individuals = generate_initial_population()
calculate_fitness(individuals)
individuals = genetic(individuals)
draw_data()
