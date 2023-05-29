def simulate_rope(motions):
    rope_length = 10
    rope = [0] * rope_length
    r_value = 0
    l_value = 0
    u_value = 0
    d_value = 0
    visited = set()
    tail_positions = set()

    for direction, steps in motions:
        for _ in range(steps):
            rope.insert(0, rope.pop())
            if direction == 'R':
                r_value += 1
            elif direction == 'L':
                l_value += 1
            elif direction == 'U':
                u_value += 1
            elif direction == 'D':
                d_value += 1
        
        visited.add(tuple(rope))
        tail_positions.add(tuple(rope[-1:]))
    print(r_value, l_value, u_value, d_value)
    return len(tail_positions)


# Example motions for the larger rope
motions = [('R', 5), ('U', 8), ('L', 8), ('D', 3), ('R', 17), ('D', 10), ('L', 25), ('U', 20)]

num_paths = simulate_rope(motions)
print("Number of paths visited by the tail:", num_paths)
