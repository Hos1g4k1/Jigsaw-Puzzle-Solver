import numpy as np

'''
	Posmatramo dva dela slagalice i racunamo fitness kao 
	razliku vrednosti piksela na ivicama. Dakle, oduzimamo vrednosti
	piksela desne ivice jednog dela od vrednosti piksela leve. Slican
	princip vazi i kada se posmetraju delovi odozgo na dole
'''

def dissimilarity_measure(first_piece, second_piece, orientation="LR"):
    
    rows, columns, _ = first_piece.shape()
    color_difference = None

    if orientation == "LR":
        color_difference = first_piece[:rows, columns - 1, :] - second_piece[:rows, 0, :]

    if orientation == "TD":
        color_difference = first_piece[rows - 1, :columns, :] - second_piece[0, :columns, :]
        
    #TODO Ovde imamo vise mera, treba razbiti na posebne funkcije

    squared_color_difference = np.power(color_difference / 255.0, 2)
    color_difference_per_row = np.sum(squared_color_difference, axis=1)
    total_difference = np.sum(color_difference_per_row, axis=0)

    value = np.sqrt(total_difference)

    return value
