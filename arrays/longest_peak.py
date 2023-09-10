"""
https://www.algoexpert.io/questions/longest-peak
"""


def longestPeak(array):

    maxpeak = 0

    for i in range(1, len(array) - 1):
        # is it a peak value
        if array[i] > array[i - 1] and array[i] > array[i + 1]:

            leftidx = i
            while leftidx > 0 and array[leftidx - 1] < array[leftidx]:
                leftidx -= 1

            rightidx = i
            while rightidx < len(array) - 1 and array[rightidx + 1] < array[rightidx]:
                rightidx += 1

            peaksize = rightidx - leftidx + 1
            if peaksize > maxpeak:
                maxpeak = peaksize
        else:
            continue

    return maxpeak
