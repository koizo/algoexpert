"""
https://www.algoexpert.io/questions/array-of-products
"""


def arrayOfProducts(array):
    # Write your code here.
    result = []
    startRow, endRow = 0, len(array) - 1
    currentIdx = 0

    while currentIdx <= endRow:
        product = 1
        leftidx = currentIdx - 1
        while leftidx >= 0:
            product = product * array[leftidx]
            leftidx -= 1
        rightidx = currentIdx + 1
        while rightidx <= endRow:
            product = product * array[rightidx]
            rightidx += 1

        currentIdx += 1
        result.append(product)

    return result
