# Ratkaisu
# Tätä sivusto ei hyväksynyt... En ymmärrä miksi???
import random

# Arvottavan suorakulmion rajat
x_min = 0
x_max = 2
y_min = 0
y_max = 4

# Alueen A pisteiden määrä
A_count = 0

# Arvottujen pisteiden määrä
total_count = 1000

# Arvotaan pisteitä suorakulmiosta B
for i in range(total_count):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    if y >= x * x:
        A_count += 1
    if (i + 1) % 10 == 0:
        # Tulostetaan tähän mennessä arvotut pisteet
        area_A = (A_count / (i+1)) * (x_max - x_min) * (y_max - y_min)
        print(A_count, area_A)

# Lasketaan lopullinen likiarvo alueen A pinta-alalle
area_A = (A_count / total_count) * (x_max - x_min) * (y_max - y_min)

# Tulostetaan lopullinen arvio pinta-alalle
print(area_A)
