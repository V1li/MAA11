# Ratkaisu
lista = [32, 18, 19, 25, 6, 47, 13, 49, 41, 1, 24, 15, 26, 5, 48, 21, 30, 50, 33, 9, 35, 2, 11, 20, 22, 40, 31, 45, 44, 12, 39, 3, 34, 7, 29, 10, 28, 42, 16, 23, 4, 17, 38, 27, 8, 43, 14, 46, 37, 36]

n = len(lista)
laskuri = 0

while True:
    muutettu = False
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            muutettu = True
        laskuri += 1
    if not muutettu:
        break

print(laskuri)
