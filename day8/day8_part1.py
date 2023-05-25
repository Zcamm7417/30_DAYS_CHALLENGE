def count_visible_trees(tree_map):
    rows = len(tree_map)
    cols = len(tree_map[0])
    # print(cols)

    visible_trees = 0

    # Check visibility in each row
    for row in tree_map:
        max_height = 0
        visible = 0
        
        for height in row:
            if height > max_height:
                visible += 1
                max_height = height
            
        visible_trees += visible
    # Check visibility in each column
    for col in range(cols):
        max_height = 0
        visible = 0

        for row in range(rows):
            height = tree_map[row][col]

            if height > max_height:
                visible += 1
                max_height = height

        visible_trees += visible

    return visible_trees

# tree_map = [
#     [3, 0, 3, 7, 3],
#     [2, 5, 5, 1, 2],
#     [6, 5, 3, 3, 2],
#     [3, 3, 5, 4, 9],
#     [3, 5, 3, 9, 0]
# ]
with open("day8_data.txt", "r") as file:
    tree_map = file.read()
    tree_map = [[int(height) for height in row] for row in tree_map.split("\n")]
    # tree_map = [[int(height) for height in row.split()] for row in tree_map.split("\n")]


    # print(tree_map)
# print(tree_map)
visible_count = count_visible_trees(tree_map)
print(f"The number of visible trees is: {visible_count}")
