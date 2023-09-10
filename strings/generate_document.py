"""
https://www.algoexpert.io/questions/generate-document
"""


def generateDocument(characters, document):
    for char in document:
        firstIdx = characters.find(char)
        if firstIdx == -1:
            return False
        characters = characters[:firstIdx] + characters[firstIdx + 1 :]
    return True
