"""
https://www.algoexpert.io/questions/transpose-matrix
"""


def transposeMatrix(matrix):
    # Write your code here.
    transpose = []
    rows = len(matrix)
    col = len(matrix[0])
    for x in range(col):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][x])
        transpose.append(new_row)
    return transpose
