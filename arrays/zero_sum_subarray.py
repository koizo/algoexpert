"""
https://www.algoexpert.io/questions/zero-sum-subarray
"""


def zeroSumSubarray(nums):
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == 0:
                return True
    return False
