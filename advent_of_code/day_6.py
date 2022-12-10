import numpy as np
from collections import Counter, defaultdict

with open("./inputs/day_6.txt") as f:
    data = f.readline()

population = [int(fish) for fish in data.split(",")]

# population = [3,4,3,1,2]

"""
day = 1
target = 256
while day <= (target % 7):
    for i in range(len(population)):
        if population[i] == 0:
            population.append(8)
            population[i] = 6
        else:
            population[i] -= 1
    day += 1

population_count = 0
week = 1
while week <= (target // 7):
    newborn_count = 0
    newborn = []
    for fish in population[::-1]:
        if fish <= 6:
            break
        else:
            newborn_count += 1
            newborn.append(fish - 7)
    population_count = len(population) + (len(population) - newborn_count)
    old_population = population[0:len(population) - newborn_count]

    population =  old_population + newborn + new_population
    week += 1

print(population_count)
"""
def zero_generator():
    return 0

fish_count = defaultdict(zero_generator)
fish_count.update(Counter(population))


for day in range(256):
    newborns = fish_count[0]
    fish_count[0] = fish_count[1]
    fish_count[1] = fish_count[2]
    fish_count[2] = fish_count[3]
    fish_count[3] = fish_count[4]
    fish_count[4] = fish_count[5]
    fish_count[5] = fish_count[6]
    fish_count[6] = fish_count[7] + newborns
    fish_count[7] = fish_count[8]
    fish_count[8] = newborns

print(fish_count)
print(sum(fish_count.values()))
