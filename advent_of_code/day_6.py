with open("./inputs/day_6.txt") as f:
    data = f.readline()

# population = [int(fish) for fish in data.split(",")]

population = [3,4,3,1,2]
day = 1
newborn = []
while day <= 80:
    for i in range(len(population)):
        if population[i] == 0:
            newborn.append(9)
            population[i] = 6
        else:
            population[i] -= 1
    for i in range(len(newborn)):
        try:
            if newborn[i] == 0:
                population.append(6)
                newborn.remove(newborn[i])
                newborn.append(9)
                newborn[i] -= 1
            elif newborn[i] > 0:
                newborn[i] -= 1
        except IndexError:
            pass
    day += 1

print(len(population) + len(newborn))