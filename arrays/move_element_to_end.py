"""
https://www.algoexpert.io/questions/move-element-to-end
"""


def moveElementToEnd(array, toMove):
    start = 0
    end = len(array) - 1

    while True:
        if start > end:
            break
        if array[start] == toMove:
            while True:
                if start > end:
                    break
                if array[end] == toMove:
                    end -= 1
                else:
                    array[start] = array[end]
                    array[end] = toMove
                    end -= 1
                    break

        start += 1

    return array
