from __future__ import print_function
from operator import attrgetter
from jigsaw.utils import flatten_image, assemble_image
from jigsaw.selection import roulette_selection, tournament_selection
from jigsaw.crossover import Crossover
from jigsaw.chromosome import Chromosome
from jigsaw.utils import ImageAnalysis, Plot, print_progress

class GeneticAlgorithm(object):

    TERMINATION_THRESHOLD = 10

    def __init__(self, image, piece_size, population_size, generations, elite_size=2):
        self._image = image
        self._piece_size = piece_size
        self._generations = generations
        self._elite_size = elite_size
        pieces, rows, columns = flatten_image(image, piece_size, indexed=True)
        self._population = [Chromosome(pieces, rows, columns) for _ in range(population_size)]
        self._pieces = pieces

    def start_evolution(self, verbose):
        print("=== Pieces:      {}\n".format(len(self._pieces)))

        ImageAnalysis.analyze_image(self._pieces)

        best = None
        best_fitness_score = float("-inf")
        termination_counter = 0

        for generation in range(self._generations):
            print_progress(generation, self._generations - 1, prefix="=== Solving puzzle: ")

            new_population = []

            # Elitizam
            elite = sorted(self._population, key=attrgetter("fitness"))[-self._elite_size:]
            new_population.extend(elite)

            selected_parents = tournament_selection(self._population, elites=self._elite_size)

            for first_parent, second_parent in selected_parents:
                crossover = Crossover(first_parent, second_parent)
                crossover.run()
                child = crossover.child()
                new_population.append(child)

            best = max(self._population, key=attrgetter("fitness"))

            if best.fitness <= best_fitness_score:
                termination_counter += 1
            else:
                best_fitness_score = best.fitness

            if termination_counter == self.TERMINATION_THRESHOLD:
                print("\n\n=== GA terminated")
                print("=== There was no improvement for {} generations".format(self.TERMINATION_THRESHOLD))
                return best

            self._population = new_population

            if verbose:
                plot.show_fittest(best.to_image(), "Generation: {} / {}".format(generation + 1, self._generations))

        return best
