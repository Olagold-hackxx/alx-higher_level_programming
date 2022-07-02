#!/usr/bin/python3

def matrix_divided(matrix, div):
    error_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_msg2 = "Each row of the matrix must have the same size"

    if (not isinstance(matrix, list) or matrix == [] or
            (not all(isinstance(row, list) for row in matrix))):
        raise TypeError(error_msg1)
    if all(type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError(error_msg1)
    if all(len(matrix[0]) != len(row) for row in matrix):
        raise TypeError(error_msg2)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    matrix_div_result = []
    for i in range(len(matrix)):
        if len(matrix[i]) is not length:
            raise TypeError(error_msg2)
        matrix_div_result.append([])
        for row in matrix[i]:
            if type(row) is int or type(row) is float:
                matrix_div_result[i].append(round(row / div, 2))
            else:
                raise TypeError(error_msg1)
    return matrix_div_result
