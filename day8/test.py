def read_input(input_str):
    return [list(map(int, row)) for row in input_str.splitlines()]

def is_visible(grid, row, col, dr, dc):
    height = grid[row][col]
    while 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
        row += dr
        col += dc
        if grid[row][col] >= height:
            return False
    return True

def scenic_score(grid, row, col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    score = 1
    for dr, dc in directions:
        visible_trees = 0
        r, c = row + dr, col + dc
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            visible_trees += 1
            if grid[r][c] >= grid[row][col]:
                break
            r += dr
            c += dc
        score *= visible_trees
    return score

def solve(input_str):
    grid = read_input(input_str)
    visible_trees = 0
    max_scenic_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if any(is_visible(grid, row, col, dr, dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]):
                visible_trees += 1
            max_scenic_score = max(max_scenic_score, scenic_score(grid, row, col))

    return visible_trees, max_scenic_score
with open("day8_data.txt", "r") as file:
    tree_map = file.read()
    grid = [[int(height) for height in row] for row in tree_map.split("\n")]


input_str = "30373\n25512\n65332\n33549\n35390"
visible_trees, max_scenic_score = solve(input_str)
print(f"Visible trees: {visible_trees}")
print(f"Highest scenic score: {max_scenic_score}")
