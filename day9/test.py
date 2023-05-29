def unique_places_visited(moves, initial_state):
    rows = len(initial_state)
    cols = len(initial_state[0])
    x, y = 0, 0
    # Find the initial position of 's'
    for i in range(rows):
        for j in range(cols):
            if initial_state[i][j] == 's':
                x, y = i, j
                break

    tail_positions = []
    for i in range(rows):
        for j in range(cols):
            if initial_state[i][j].isdigit():
                tail_positions.append((i, j))

    visited = set()
    tail_idx = 0

    for move in moves:
        direction, steps = move[0], int(move[2])

        for _ in range(steps):
            visited.add((x, y))  # Add the current position to visited

            if direction == 'R':
                y = (y + 1) % cols  # Move right
            elif direction == 'L':
                y = (y - 1 + cols) % cols  # Move left
            elif direction == 'U':
                x = (x - 1 + rows) % rows  # Move up
            elif direction == 'D':
                x = (x + 1) % rows  # Move down

            if tail_idx < len(tail_positions):
                tail_x, tail_y = tail_positions[tail_idx]
                if (x, y) == (tail_x, tail_y):
                    tail_idx += 1

                    if tail_idx == len(tail_positions):
                        # All tail positions have been visited, no need to continue
                        return len(visited)

    return len(visited)


# Test the function with the given moves and initial state
moves = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]
initial_state = [
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '............H.............',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................',
    '..........................'
]

result = unique_places_visited(moves, initial_state)
print(f"Number of unique places visited by the tail: {result}")
