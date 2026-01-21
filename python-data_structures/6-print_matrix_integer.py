#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        row_string = ""

        for number in row:
            row_string += "{:d}".format(number)
        
        if number != row[-1]:
            row_string += " "

        print (row_string)
