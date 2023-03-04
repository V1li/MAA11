# Ratkaisu
def func(n):
    x = n
    virhe = 1e-9
    while abs(x ** 3 - 2) > virhe:
        x = x - (x ** 3 - 2) / (3 * x ** 2)
    return x


print(func(2))
