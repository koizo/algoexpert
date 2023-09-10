"""
https://www.algoexpert.io/questions/best-seat
"""


def bestSeat(seats):
    # Write your code here.
    head, tail = 0, 0
    best_seats = 0
    current_seats = 0
    for i in range(len(seats)):
        if seats[i] == 1:
            if current_seats > best_seats:
                best_seats = current_seats
                tail = i
            current_seats = 0
            continue
        current_seats += 1

    if best_seats == 0:
        return -1

    location = best_seats // 2

    return tail - location - 1
