"""
https://www.algoexpert.io/questions/group-anagrams
"""


def groupAnagrams(words):

    sorted_words = {}
    for word in words:
        sword = "".join(sorted(word))
        if sword in sorted_words:
            sorted_words[sword].append(word)
        else:
            sorted_words[sword] = [word]

    return list(sorted_words.values())
