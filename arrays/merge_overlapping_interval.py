"""
https://www.algoexpert.io/questions/merge-overlapping-intervals
"""


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda i: i[0])
    return_list = []
    last_interval = None
    for i in range(len(intervals)):
        if last_interval is None:
            last_interval = intervals[i]
            continue
        if intervals[i][0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], intervals[i][1])
        else:
            return_list.append(last_interval)
            last_interval = intervals[i]

    return_list.append(last_interval)
    return return_list
