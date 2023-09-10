"""
https://www.algoexpert.io/questions/three-number-sum
"""


def threeNumberSum(array, targetSum):
    # Write your code here.
    answers = []

    for element in array:
        for element2 in array:
            if element == element2:
                break
            for element3 in array:
                if element2 == element3:
                    break
                if element + element2 + element3 == targetSum:
                    answers.append(sorted([element, element2, element3]))
    return sorted(answers)


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif sum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets
