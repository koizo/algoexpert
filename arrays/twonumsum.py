"""
https://www.algoexpert.io/questions/two-number-sum
"""


def twoNumberSum(array, targetSum):
    # Write your code here.
    number = None
    solution = []

    for num in array:
        for num2 in array:
            if num == num2:
                continue

            if num + num2 == targetSum:
                if num not in solution and num2 not in solution:
                    solution.append(num)
                    solution.append(num2)

    return solution
