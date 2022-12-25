import numpy as np
from collections import Counter

with open("./inputs/day_11.txt") as f:
    data = f.readlines()

matrix = []
for d in data:
    rows = []
    for char in d.replace("\n", ""):
        rows.append(int(char))
    matrix.append(rows)

octopuses = np.array(matrix)

def neighbor_finder(i, j):
    neighbor_idx = []
    map_size_v, map_size_h = octopuses.shape
    if i != 0:
        neighbor_idx.append((i - 1, j))
    if j != 0:
        neighbor_idx.append((i, j - 1))
    if i != map_size_v - 1:
        neighbor_idx.append((i + 1, j))
    if j != map_size_h - 1:
        neighbor_idx.append((i, j + 1))

    if i != 0 and j != map_size_h - 1:
        neighbor_idx.append((i - 1, j + 1))
    if i != map_size_v - 1 and j != map_size_h - 1:
        neighbor_idx.append((i + 1, j + 1))
    if j != 0 and i != map_size_v - 1:
        neighbor_idx.append((i + 1, j - 1))
    if i != 0 and j != 0:
        neighbor_idx.append((i - 1, j - 1))
    return neighbor_idx

def chain_reaction(start_i, start_j, octopus_map):
    if octopus_map[start_i, start_j] <= 9:
        return octopus_map
    else:
        octopus_map[start_i, start_j] = 0

        neighbor_ids = neighbor_finder(start_i, start_j)
        for n_id in neighbor_ids:
            if octopus_map[n_id[0], n_id[1]] != 0:
                octopus_map[n_id[0], n_id[1]] += 1

        neighbor_values = []
        neighbor_keys = []
        for n_id in neighbor_ids:
            neighbor_values.append(octopus_map[n_id[0], n_id[1]])
            neighbor_keys.append((n_id[0], n_id[1]))
        
        sorted_neighbor_ids = [x for _, x in sorted(zip(neighbor_values, neighbor_keys),reverse=True)]
        try:
            explosion_count = dict(Counter(neighbor_values))[10]
        except KeyError:
            explosion_count = 0
        exploded_count = 0
        
        for n_id in sorted_neighbor_ids:
            exploded_count += 1
            return chain_reaction(n_id[0], n_id[1], octopus_map)

add_day = np.ones(octopuses.shape, dtype=int)

print(octopuses + add_day * 2)
print(chain_reaction(4, 9, octopuses + add_day * 2))