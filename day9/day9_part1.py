def simulate_rope(motions):
    head = [0, 0]
    tail = [0, 0]
    visited = set()
    visited.add(tuple(tail))

    for direction, steps in motions:
        for _ in range(steps):
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1

        dx, dy = head[0] - tail[0], head[1] - tail[1]
        while abs(dx) > 1 or abs(dy) > 1:
            if dx != 0 and dy != 0:
                tail[0] += dx // abs(dx)
                tail[1] += dy // abs(dy)
            else:
                tail[0] += dx // max(abs(dx), abs(dy))
                tail[1] += dy // max(abs(dx), abs(dy))
            visited.add(tuple(tail))
            dx, dy = head[0] - tail[0], head[1] - tail[1]

    return len(visited)

def read_motions_from_file(file_path):
    motions = []
    with open(file_path, 'r') as file:
        for line in file:
            direction, steps = line.strip().split()
            motions.append((direction, int(steps)))
    return motions

# Read the motions from the file
file_path = 'day9_data.txt'
motions = read_motions_from_file(file_path)

print(simulate_rope(motions)) 