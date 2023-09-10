"""
https://www.algoexpert.io/questions/sorted-squared-array
"""


def sortedSquaredArray(array):
    # Write your code here.
    square_array = []
    for element in array:
        square_array.append(element * element)

    return sorted(square_array)
