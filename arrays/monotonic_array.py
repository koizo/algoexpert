"""
https://www.algoexpert.io/questions/monotonic-array
"""


def isMonotonic(array):

    lastval = None
    order = None

    for element in array:
        if lastval is None:
            lastval = element
            continue

        if order is None:
            if lastval > element:
                order = 1
            if lastval < element:
                order = 0
            continue

        if order == 0 and element < lastval:
            return False
        if order == 1 and element > lastval:
            return False
        lastval = element

    return True


def isMonotonic(array):
    # Write your code here.
    inc = True
    dec = True

    for i in range(len(array) - 1):
        inc = inc and array[i] <= array[i + 1]
        dec = dec and array[i] >= array[i + 1]
    return inc or dec
