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


for i in range(1, 101):
    print(i, collatz(i))
    