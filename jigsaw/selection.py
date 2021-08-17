import random
import bisect
import numpy as np

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

'''
Odabir turnirske ili ruletske selekcije
'''

def roulette_selection(population, elites=4):

    fitness_values = [individual.fitness for individual in population]
    probability_intervals = [sum(fitness_values[:i + 1]) for i in range(len(fitness_values))]

    def select_individual():
        random_select = random.uniform(0, probability_intervals[-1])
        selected_index = bisect.bisect_left(probability_intervals, random_select)
        return population[selected_index]

    selected = []
    for i in xrange(len(population) - elites):
        first, second = select_individual(), select_individual()
        selected.append((first, second))

    return selected
    
def tournament_selection(population, elites=4):

    tournament_size = 5
    
    def select_individual():
        random_select = random.sample(population, tournament_size)
        fitness_values = [individual.fitness for individual in random_select]
        index_max = np.argmax(fitness_values)
        
        return random_select[index_max]
        

    selected = []
    for i in xrange(len(population) - elites):
        first, second = select_individual(), select_individual()
        selected.append((first, second))

    return selected
