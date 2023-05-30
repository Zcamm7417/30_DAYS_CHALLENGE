def move_right(grid, pos, steps):
    for i in range(steps):
        pos[1] += 1
        grid[pos[0]][pos[1]] = "#"
    return pos

def move_up(grid, pos, steps):
    for i in range(steps):
        pos[0] -= 1
        grid[pos[0]][pos[1]] = "#"
    return pos

def move_left(grid, pos, steps):
    for i in range(steps):
        pos[1] -= 1
        grid[pos[0]][pos[1]] = "#"
    return pos

def move_down(grid, pos, steps):
    for i in range(steps):
        pos[0] += 1
        grid[pos[0]][pos[1]] = "#"
    return pos

def print_grid(grid):
    for row in grid:
        print("".join(row))

# Initialize the grid and starting position
grid = [["." for _ in range(50)] for _ in range(50)]
pos = [25, 25]

# List of motions and steps
motions = [("R", 5), ("U", 8), ("L", 8), ("D", 3), ("R", 17), ("D", 10), ("L", 25), ("U", 20)]

# Perform the motions
for motion, steps in motions:
    if motion == "R":
        pos = move_right(grid, pos, steps)
    elif motion == "U":
        pos = move_up(grid, pos, steps)
    elif motion == "L":
        pos = move_left(grid, pos, steps)
    elif motion == "D":
        pos = move_down(grid, pos, steps)

# Clear all positions except the tail (9)
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] != "#":
            grid[row][col] = "."

# Print the final grid
print_grid(grid)

def count_tail_length(grid):
    tail_length = 0
    for row in range(grid):
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                tail_length += 1
    return tail_length
