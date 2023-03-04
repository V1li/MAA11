# Ratkaisu
def onko_alkuluku(luku):
    if luku < 2:
        return False
    for jakaja in range(2, int(luku ** 0.5) + 1):
        if luku % jakaja == 0:
            return False
    return True


for i in range(3, 1000, 2):
    if onko_alkuluku(i) and onko_alkuluku(i + 2):
        print(i, i + 2)
