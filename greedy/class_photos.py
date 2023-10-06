"""
https://www.algoexpert.io/questions/class-photos
"""


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    blueTeam, redTeam = True, True

    for idx in range(len(blueShirtHeights)):
        if blueShirtHeights[idx] <= redShirtHeights[idx]:
            blueTeam = False
        if redShirtHeights[idx] <= blueShirtHeights[idx]:
            redTeam = False

    return True if redTeam == True or blueTeam == True else False
