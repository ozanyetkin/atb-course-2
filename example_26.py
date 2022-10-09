maze1 = [
    [0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

# Initialize another maze that is not solvable
maze2 = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
]

# Just in case, create a bigger maze and test the function
maze3 = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
]

def find_neighbors(cell_index, maze):
    neighbors = {}
    i, j = cell_index
    if i != 0:
        neighbor_u = maze[i - 1][j]
    else:
        neighbor_u = 1
    if j != 0:
        neighbor_l = maze[i][j - 1]
    else:
        neighbor_l = 1
    if j != len(maze[0]) - 1:
        neighbor_r = maze[i][j + 1]
    else:
        neighbor_r = 1
    if i != len(maze) - 1:
        neighbor_d = maze[i + 1][j]
    else:
        neighbor_d = 1

    neighbors[(i - 1, j)] = neighbor_u
    neighbors[(i, j - 1)] = neighbor_l
    neighbors[(i, j + 1)] = neighbor_r
    neighbors[(i + 1, j)] = neighbor_d
    return neighbors

def walker(current_index, finish_index, maze, checkpoints = []):
    i, j = current_index
    maze[i][j] = 1
    
    if current_index == finish_index:
        return True
    
    neighbors = find_neighbors(current_index, maze)    
    for neighbor in neighbors:
        if neighbors[neighbor] == 0:
            walker(neighbor, finish_index, maze)

    if sum(neighbors.values()) < 3:
        checkpoints.append(current_index)
    elif sum(neighbors.values()) == 4:
        checkpoints.reverse()
        walker(checkpoints.pop(), finish_index, maze)

# print(find_neighbors((4, 5), maze1))
# print(find_neighbors((2, 7), maze1))
# print(find_neighbors((0, 4), maze1))
# print(find_neighbors((0, 0), maze1))

maze_solved = maze1
print(walker((0, 0), (len(maze_solved) - 1, len(maze_solved[0]) - 1), maze_solved))