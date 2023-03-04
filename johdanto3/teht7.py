# Ratkaisu
n = 99 ** 99
summa = 0

while n > 0:
    summa += n % 10
    n //= 10

print(summa)
