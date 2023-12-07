#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    output_list = []
    for row in matrix:
        square_element = []

        for element in row:
            square_element.append(element ** 2)
        output_list.append(square_element)

    return (output_list)
