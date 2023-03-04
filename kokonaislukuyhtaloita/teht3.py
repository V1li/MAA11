# Ratkaisu
def func(i, j, n):
    return i ** 2 + j ** 2 == n ** 2


for i in range(1, 31):
    for j in range(1, 31):
        for n in range(1, 31):
            if func(i, j, n):
                print(i, j, n)
