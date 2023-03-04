# Ratkaisu
def func(x):
    return x ** 2 + x + 2


n = 0

for i in range(1, 101):
    n += func(i)

print(n)
