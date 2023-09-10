"""
https://www.algoexpert.io/questions/palindrome-check
"""


def isPalindrome(string):
    s, e = 0, len(string) - 1

    while s <= e:
        if string[e] == string[s]:
            s += 1
            e -= 1
            continue
        return False
    return True
