# Ratkaisu
lista = [5, 2, 3, 8, 1]
n = len(lista)

print(lista)

for i in range(n):
    for j in range(i, 0, -1):
        if lista[j - 1] > lista[j]:
            t = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = t
            print(lista)
        else:
            break
            