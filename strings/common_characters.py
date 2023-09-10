"""
https://www.algoexpert.io/questions/common-characters
"""


def commonCharacters(strings):
    # Write your code here.
    result = []
    first = strings.pop(0)
    size = len(strings)

    for char in first:
        count = 0
        for arr in strings:
            if char not in arr:
                continue
            count += 1
        if count == size:
            if char not in result:
                result.append(char)

    return result
