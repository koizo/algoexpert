"""
https://www.algoexpert.io/questions/smallest-difference
"""


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    smallest = None
    answer = []
    for element in arrayOne:
        for element2 in arrayTwo:
            if smallest == None:
                smallest = abs(element - element2)
            if smallest > abs(element - element2):
                smallest = abs(element - element2)
                answer = [element, element2]
    return answer


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    i0 = 0
    i1 = 0

    smallest = float("inf")
    current = float("inf")
    pair = []

    while i0 < len(arrayOne) and i1 < len(arrayTwo):
        firstnum = arrayOne[i0]
        secnum = arrayTwo[i1]

        if firstnum == secnum:
            return [firstnum, secnum]

        current = abs(firstnum - secnum)

        if current < smallest:
            smallest = current
            pair = [firstnum, secnum]

        if firstnum < secnum:
            i0 += 1
        else:
            i1 += 1

    return pair
