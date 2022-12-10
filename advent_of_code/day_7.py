with open("./inputs/day_7.txt") as f:
    data = f.readline()

positions = [int(crab) for crab in data.split(",")]

position_avg = sum(positions) / len(positions)
position_common = max(positions,key=positions.count)

starting_position = round((position_avg + position_common) / 2)

"""
def fuel_calculator(start):
    total_cost = 0
    for crab in positions:
        total_cost += abs(start - crab)
    return total_cost

"""

def fuel_calculator(start):
    total_cost = 0
    for crab in positions:
        n = abs(start - crab)
        total_cost += n * (n + 1) // 2
    return total_cost


if fuel_calculator(starting_position) > fuel_calculator(starting_position + 1):
    direction = 1
else:
    direction = -1

while fuel_calculator(starting_position) > fuel_calculator(starting_position + direction):
    starting_position += direction

print(fuel_calculator(starting_position))
