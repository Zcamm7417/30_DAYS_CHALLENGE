# checking for the highest scenic score in the visible trees.

def scenic_score(grid, row, col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    score = 1
    for dr, dc in directions:
        visible_trees = 0
        r, c = row + dr, col + dc
        # scenic_score function to consider only the first tree that is the same height or taller than the tree under consideration.
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            visible_trees += 1
            if grid[r][c] >= grid[row][col]:
                break
            r += dr
            c += dc
        score *= visible_trees
    return score

def highest_scenic_score(grid):
    max_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = scenic_score(grid, row, col)
            max_score = max(max_score, score)

    return max_score

with open("day8_data.txt", "r") as file:
    tree_map = file.read()
    grid = [[int(height) for height in row] for row in tree_map.split("\n")]

print(highest_scenic_score(grid))  # Output: 8
