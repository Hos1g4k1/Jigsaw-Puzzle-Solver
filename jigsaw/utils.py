import numpy as np
import sys

from jigsaw.fitness import dissimilarity_measure
from jigsaw.piece import Piece

import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook

class ImageAnalysis(object):

    dissimilarity_measures = {}
    best_match_table = {}

    @classmethod
    def analyze_image(cls, pieces):
        for piece in pieces:
            cls.best_match_table[piece.id] = {
                "T": [],
                "R": [],
                "D": [],
                "L": []
            }

        def update_best_match_table(first_piece, second_piece):
            measure = dissimilarity_measure(first_piece, second_piece, orientation)
            cls.put_dissimilarity((first_piece.id, second_piece.id), orientation, measure)
            cls.best_match_table[second_piece.id][orientation[0]].append((first_piece.id, measure))
            cls.best_match_table[first_piece.id][orientation[1]].append((second_piece.id, measure))

        iterations = len(pieces) - 1
        for first in range(iterations):
            print_progress(first, iterations - 1, prefix="=== Analyzing image:")
            for second in range(first + 1, len(pieces)):
                for orientation in ["LR", "TD"]:
                    update_best_match_table(pieces[first], pieces[second])
                    update_best_match_table(pieces[second], pieces[first])

        for piece in pieces:
            for orientation in ["T", "L", "R", "D"]:
                cls.best_match_table[piece.id][orientation].sort(key=lambda x: x[1])

    @classmethod
    def put_dissimilarity(cls, ids, orientation, value):
  
        if ids not in cls.dissimilarity_measures:
            cls.dissimilarity_measures[ids] = {}
        cls.dissimilarity_measures[ids][orientation] = value

    @classmethod
    def get_dissimilarity(cls, ids, orientation):
        return cls.dissimilarity_measures[ids][orientation]

    @classmethod
    def best_match(cls, piece, orientation):
        return cls.best_match_table[piece][orientation][0][0]

def flatten_image(image, piece_size, indexed=False):

    print(image.shape[0])
    print(piece_size)
    print(image.shape[1])

    rows, columns = image.shape[0] // piece_size, image.shape[1] // piece_size
    pieces = []

    for y in range(rows):
        for x in range(columns):
            left, top, w, h = x * piece_size, y * piece_size, (x + 1) * piece_size, (y + 1) * piece_size
            piece = np.empty((piece_size, piece_size, image.shape[2]))
            piece[:piece_size, :piece_size, :] = image[top:h, left:w, :]
            pieces.append(piece)

    if indexed:
        pieces = [Piece(value, index) for index, value in enumerate(pieces)]

    return pieces, rows, columns


def assemble_image(pieces, rows, columns):
    
    vertical_stack = []
    for i in range(rows):
        horizontal_stack = []
        for j in range(columns):
            horizontal_stack.append(pieces[i * columns + j])
        vertical_stack.append(np.hstack(horizontal_stack))
    return np.vstack(vertical_stack).astype(np.uint8)
    

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


class Plot(object):

    def __init__(self, image, title="Initial problem"):
        aspect_ratio = image.shape[0] / float(image.shape[1])

        width = 8
        height = width * aspect_ratio
        fig = plt.figure(figsize=(width, height), frameon=False)

        # Let image fill the figure
        ax = plt.Axes(fig, [0., 0., 1., .9])
        ax.set_axis_off()
        fig.add_axes(ax)

        self._current_image = ax.imshow(image, aspect="auto", animated=True)
        self.show_fittest(image, title)

    def show_fittest(self, image, title):
        plt.suptitle(title, fontsize=20)
        self._current_image.set_data(image)
        plt.draw()

        # Give pyplot 0.05s to draw image
        plt.pause(0.05)

def print_progress(iteration, total, prefix="", suffix="", decimals=1, bar_length=50):
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = "\033[32m█\033[0m" * filled_length + "\033[31m-\033[0m" * (bar_length - filled_length)

    sys.stdout.write("\r{0: <16} {1} {2}{3} {4}".format(prefix, bar, percents, "%", suffix))

    if iteration == total:
        sys.stdout.write("\n")
    sys.stdout.flush()
