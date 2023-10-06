"""
https://www.algoexpert.io/questions/one-edit
"""


def oneEdit(stringOne, stringTwo):
    # Write your code here.
    lenOne = len(stringOne)
    lenTwo = len(stringTwo)

    if abs(lenOne - lenTwo) > 1:
        return False

    for i in range(min(lenOne, lenTwo)):
        if stringOne[i] != stringTwo[i]:

            if lenOne == lenTwo and stringOne[i + 1 :] != stringTwo[i + 1 :]:
                return False
            elif lenOne > lenTwo and stringOne[i + 1 :] != stringTwo[i:]:
                return False
            elif lenOne < lenTwo and stringOne[i:] != stringTwo[i + 1 :]:
                return False

    return True
