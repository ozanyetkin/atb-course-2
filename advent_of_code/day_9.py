import numpy as np
# import matplotlib.pyplot as plt

with open("./inputs/day_9.txt") as f:
    data = f.readlines()

height_map = []
for d in data:
    row = [int(x) for x in d.replace("\n", "")]
    height_map.append(row)

# plt.imshow(np.array(height_map))
# plt.show()

height_map = np.array(height_map)

def neighbor_finder(i, j):
    neighbor_idx = []
    map_size_v, map_size_h = height_map.shape
    if i != 0:
        neighbor_idx.append((i - 1, j))
    if j != 0:
        neighbor_idx.append((i, j - 1))
    if i != map_size_v - 1:
        neighbor_idx.append((i + 1, j))
    if j != map_size_h - 1:
        neighbor_idx.append((i, j + 1))
    return neighbor_idx
    
def basin_finder(heights):
    basins = []
    basins_idx = []
    map_size_v, map_size_h = heights.shape
    for i in range(map_size_v):
        for j in range(map_size_h):
            current_position = heights[i][j]
            neighbor_idx = neighbor_finder(i, j)
            
            is_basin = True
            for index in neighbor_idx:
                if current_position >= heights[index]:
                    is_basin = False

            if is_basin:
                basins.append(current_position)
                basins_idx.append((i, j))
    return basins, basins_idx
            
# print(sum([x + 1 for x in basin_finder(height_map)]))
basins, basins_idx = basin_finder(height_map)
print(sum(basins) + len(basins))

def grow_basin(start_i, start_j, heights, basin_path=[], checkpoints=[]):
    if heights[start_i, start_j] == 9:
        return basin_path

    if (start_i, start_j) not in basin_path:
        basin_path.append((start_i, start_j))
    else:
        c_i, c_j = checkpoints[-1]
        return grow_basin(c_i, c_j, heights, basin_path)
    
    neighbor_idx = neighbor_finder(start_i, start_j)
    checkpoints += neighbor_idx
    for n_index in neighbor_idx:
        n_i, n_j = n_index
        return grow_basin(n_i, n_j, heights, basin_path)

print(basins_idx)
print(grow_basin(basins_idx[1][0], basins_idx[1][1], height_map))
