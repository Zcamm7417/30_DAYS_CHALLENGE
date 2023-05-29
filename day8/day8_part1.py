# checking for the total number of visible trees
def visible_trees(grid):
    visible = 0
    n = len(grid)
    m = len(grid[0])

    # Check rows and columns
    for i in range(n):
        for j in range(m):
            left = all(grid[i][k] < grid[i][j] for k in range(j))  # left
            right = all(grid[i][k] < grid[i][j] for k in range(j + 1, m)) # right
            up = all(grid[k][j] < grid[i][j] for k in range(i)) # up
            down = all(grid[k][j] < grid[i][j] for k in range(i + 1, n)) # down

            if left or right or up or down:
                visible += 1

    return visible

with open("day8_data.txt", "r") as file:
    tree_map = file.read()
    grid = [[int(height) for height in row] for row in tree_map.split("\n")]

print(visible_trees(grid))
