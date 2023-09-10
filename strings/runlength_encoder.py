"""
https://www.algoexpert.io/questions/run-length-encoding
"""


def runLengthEncoding(string):
    last_char = string[0]
    repetion = 1
    new_string = ""

    for i in range(1, len(string)):
        if string[i] == last_char:
            repetion += 1
            continue

        while repetion > 9:
            new_string += f"{9}{last_char}"
            repetion -= 9

        new_string += f"{repetion}{last_char}"
        last_char = string[i]
        repetion = 1

    while repetion > 9:
        new_string += f"{9}{last_char}"
        repetion -= 9
    new_string += f"{repetion}{last_char}"

    return new_string
