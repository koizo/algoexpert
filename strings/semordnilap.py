"""
https://www.algoexpert.io/questions/semordnilap
"""


def semordnilap(words):
    result = []
    while words:
        word = words.pop(0)
        if word[::-1] in words and word not in result:
            result.append([word, word[::-1]])
    return result
