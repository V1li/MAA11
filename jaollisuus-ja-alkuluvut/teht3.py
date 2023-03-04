# Ratkaisu
import math


def onko_alkuluku(luku):
    if luku < 2:
        return False
    elif luku == 2:
        return True
    elif luku % 2 == 0:
        return False

    for jakaja in range(3, int(math.sqrt(luku)) + 1, 2):
        if luku % jakaja == 0:
            return False

    return True


# Lasketaan alkulukujen määrä välillä 1-1000
alkulukuja = 0
for luku in range(1, 1001):
    if onko_alkuluku(luku):
        alkulukuja += 1

print(alkulukuja)
