"""
https://www.algoexpert.io/questions/reverse-words-in-string
"""


def reverseWordsInString(string):
    # Write your code here.
    words = []
    pointer = 0

    for i in range(len(string)):

        if string[i] == " ":
            words.insert(0, string[pointer:i])
            pointer = i
        elif string[pointer] == " ":
            words.insert(0, " ")
            pointer = i

    words.insert(0, string[pointer:])

    return "".join(words)
