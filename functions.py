from individual import Individual


def mean_square_error(individial):
    given_data = get_input()
    total_error = 0
    for i in range(len(given_data)):
        total_error += abs(given_data[i] - individial.get_result(i))
    return total_error/len(given_data)


def sort_by_fitness(individuals):
    return individuals


def get_input():
    return [1, 2, 3, 4, 5]
