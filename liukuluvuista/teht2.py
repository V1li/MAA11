# Ratkaisu
import math


def f(x):
    return x - math.sqrt(5) < 10 ** -9 == x


x = 2.2360689774

if f(x):
    print("Likiarvo on oikein!")
else:
    print("Likiarvo on väärin!")
