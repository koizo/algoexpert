"""
https://www.algoexpert.io/questions/longest-palindromic-substring
"""


def longestPalindromicSubstring(string):
    longest = ""

    for i in range(len(string)):
        for j in range(i, len(string)):
            to_test = string[i : j + 1]
            if isPalindrome(to_test) and len(to_test) > len(longest):
                longest = to_test

    return longest


def isPalindrome(string):
    return string == string[::-1]
