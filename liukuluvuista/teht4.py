# Ratkaisu
# Tätä sivusto ei arvostele automaattisesti. Joten tämä on vain esimerkki.

import math

a = 2
b = 5
c = -3

# Lasketaan diskriminantti
d = b**2 - 4*a*c

# Tarkistetaan, onko ratkaisuja
if d < 0:
    print("Ei reaalisia ratkaisuja")
elif d == 0:
    x = -b / (2*a)
    print("Yksi reaalinen ratkaisu:", x)
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Kaksi reaalista ratkaisua:", x1, x2)
