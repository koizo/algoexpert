"""
https://www.algoexpert.io/questions/minimum-waiting-time
"""


def minimumWaitingTime(queries):
    # Write your code here.
    if len(queries) == 1:
        return 0

    queries.sort()
    time = 0
    sum = 0

    for i in range(1, len(queries)):
        sum = sum + queries[i - 1]
        time = time + sum

    return time
