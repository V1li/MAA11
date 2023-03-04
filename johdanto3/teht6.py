# Ratkaisu
def collatz(n):
    c = 1
    while n != 1:
        c += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return c


suurin_askelmaara = 0
suurin_n = 0

for n in range(1, 1000):
    askelmaara = collatz(n)
    if askelmaara > suurin_askelmaara:
        suurin_askelmaara = askelmaara
        suurin_n = n

print(suurin_askelmaara)
