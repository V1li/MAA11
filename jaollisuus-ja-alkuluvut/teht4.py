# Ratkaisu
def onko_alkuluku(luku):
    if luku < 2:
        return False

    for jakaja in range(2, int(luku ** 0.5) + 1):
        if luku % jakaja == 0:
            return False

    return True


summa = 0
for luku in range(1, 1001):
    if onko_alkuluku(luku):
        summa += luku

print(summa)
