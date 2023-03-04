# Ratkaisu
import random


def simulate():
    total = 0
    rolls = 0
    while total < 20:
        total += random.randint(1, 6)
        rolls += 1
    return rolls


sims = 1000
total = 0
for i in range(sims):
    total += simulate()

average_rolls = total / sims
print(average_rolls)
