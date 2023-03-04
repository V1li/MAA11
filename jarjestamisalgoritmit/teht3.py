# Ratkaisu
lista = [32, 18, 19, 25, 6, 47, 13, 49, 41, 1, 24, 15, 26, 5, 48, 21, 30, 50, 33, 9, 35, 2, 11, 20, 22, 40, 31, 45, 44, 12, 39, 3, 34, 7, 29, 10, 28, 42, 16, 23, 4, 17, 38, 27, 8, 43, 14, 46, 37, 36]
n = len(lista)
laskuri = 0

for i in range(n):
    for j in range(i, 0, -1):
        laskuri += 1
        if lista[j - 1] > lista[j]:
            t = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = t
        else:
            break

print(laskuri)
