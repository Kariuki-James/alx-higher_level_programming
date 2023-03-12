#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    for row in matrix:
        for index, col in enumerate(row):
            if index > 0:
                print(' ', end='')

            print("{:d}".format(col), end='')
        print()
