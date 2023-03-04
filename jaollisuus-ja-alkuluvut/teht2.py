# Ratkaisu
import math
from time import time


def onko_alkuluku(luku):
    if luku < 2:
        return False
    elif luku == 2:
        return True
    elif luku % 2 == 0:
        return False
    else:
        jakaja_raja = int(math.sqrt(luku)) + 1
        for jakaja in range(3, jakaja_raja, 2):
            if luku % jakaja == 0:
                return False
        return True


n = 30000001
alkuaika = time()
print(onko_alkuluku(n))
loppuaika = time()

print("Aikaa kului sekunteina:")
print(loppuaika - alkuaika)
