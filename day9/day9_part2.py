def simulate_rope(motions):
    # Initialize rope positions
    positions = {(0, 0): set(range(1, 11))}
    
    # Iterate through each motion
    for motion in motions:
        direction, steps = motion[0], int(motion[1:])
        
        # Update head position
        head = next((pos for pos, knots in positions.items() if 0 in knots), None)
        if head is None:
            break
        new_head = move_position(head, direction, steps)
        
        # Determine positions covered by the head
        new_positions = set()
        for pos, knots in positions.items():
            if pos == head or 0 in knots:
                continue
            if is_adjacent(pos, new_head) or pos[0] == new_head[0] or pos[1] == new_head[1]:
                new_positions.add(pos)
        
        # Update tail positions
        tail = next((pos for pos, knots in positions.items() if 0 in knots), None)
        if tail is None:
            break
        new_positions.add(tail)
        
        # Update positions dictionary
        positions[new_head] = positions[head] - {0}
        positions[head] = set()
        
        # Remove covered positions
        for pos in new_positions:
            positions.pop(pos, None)
        
        # Add new positions
        positions[new_head].add(0)
        for pos in new_positions:
            positions[pos].add(0)
        
    # Count unique positions visited by the tail
    visited_positions = set()
    for knots in positions.values():
        visited_positions.update(knots)
    
    return len(visited_positions)

def move_position(position, direction, steps):
    x, y = position
    if direction == 'R':
        return x + steps, y
    elif direction == 'L':
        return x - steps, y
    elif direction == 'U':
        return x, y - steps
    elif direction == 'D':
        return x, y + steps

def is_adjacent(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

# Example series of motions
motions = [
    'R5',
    'U8',
    'L8',
    'D3',
    'R17',
    'D10',
    'L25',
    'U20'
]

result = simulate_rope(motions)
print("Number of positions visited by the tail:", result)
