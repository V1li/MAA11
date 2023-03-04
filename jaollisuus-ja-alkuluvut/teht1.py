# Ratkaisu
a = 210592578
b = 120065279

while b:
    a, b = b, a % b

print(a)
