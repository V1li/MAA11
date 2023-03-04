# Ratkaisu
n = 1
suurin = 100
pienin = 1

while n <= 100:
    if n % 2 == 0:
        print(suurin)
        suurin -= 1
    else:
        print(pienin)
        pienin += 1
    n += 1
    