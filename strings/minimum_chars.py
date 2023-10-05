"""
https://www.algoexpert.io/questions/minimum-characters-for-words
"""


def minimumCharactersForWords(words):
    # Write your code here.
    hashMap = {}
    allChars = []
    for word in words:
        tempHash = {}

        for char in word:
            tempHash[char] = tempHash[char] + 1 if char in tempHash else 1

        for char in tempHash:
            hashMap[char] = (
                max(hashMap[char], tempHash[char])
                if char in hashMap
                else tempHash[char]
            )

    return unpack_list(hashMap)


def unpack_list(d):
    result = []
    for k, v in d.items():
        for i in range(v):
            result.append(k)
    return result
