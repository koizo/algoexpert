"""
https://www.algoexpert.io/questions/caesar-cipher-encryptor
"""


def caesarCipherEncryptor(string, key):
    # Write your code here.
    alph = "abcdefghijklmnopqrstuvwxyz"
    total = len(alph)
    new_string = ""

    while key > total:
        key -= total

    for i in range(len(string)):
        char_idx = alph.find(string[i])
        char_idx = char_idx + key - total if char_idx + key >= total else char_idx + key
        new_string += alph[char_idx]

    return new_string
