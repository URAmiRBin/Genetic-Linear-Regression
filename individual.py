from functions import mean_square_error


class Individual:
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
