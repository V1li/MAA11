# Ratkaisu
def func(i, j):
    return i ** 2 + j ** 2


for i in range(1, 51):
    for j in range(1, 51):
        if func(i, j) % 97 == 0:
            print(i, j)
