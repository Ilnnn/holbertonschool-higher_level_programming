#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Returns:
        list of lists: new matrix with divided values
    """
    if not isinstance (matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integer/floats"
        )

    row_lenghts = None

    for row in matrix:
        if not isinstance (row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integer/floats"
                )
        if row_lenghts is None:
            row_lenghts = len(row)
        elif len(row) != row_lenghts:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be matrix (list of lists) of integers"
                )
    if not isinstance(div, (int float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix == []

    for row in matrix:
        new_row == []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    
    return new_matrix
