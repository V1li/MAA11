# Ratkaisu
n = 30
n_1 = 1
n_2 = 1
count = 0

if n == 1:
    print(n_1)
else:
    while count < n:
        print(n_1)
        nth = n_1 + n_2
        n_1 = n_2
        n_2 = nth
        count += 1
        