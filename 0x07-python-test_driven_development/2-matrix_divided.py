#!/usr/bin/python3
"""Defines a function that divides a matrix"""


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix

    Args:
        matrix (list): a list of lists of integers or floats.
        div (float): all elements of the matrix are divided by this number.
            ->div is rounded to 2 decimal places during the division.

    Returns:
        A new matrix with the results.
    '''
    if not isinstance(matrix, list) or \
    not all(isinstance(row, list) for row in matrix) or \
    not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        message = "Each row of the matrix must have the same size"
        raise TypeError(message)

    if type(div) not in (int, float):
        message = "div must be a number"
        raise TypeError(message)
    if div == 0:
        message = "division by zero"
        raise ZeroDivisionError(message)
    
    return [[round(elem / div, 2) for elem in row] for row in matrix]
