def simulate_rope(motions):
    head = [[0, 0] for _ in range(10)]
    tail = [[0, 0] for _ in range(10)]
    visited = set()
    for nut_idx in range(10):
        visited.add(tuple(tail[nut_idx]))

    for direction, steps in motions:
        for _ in range(steps):
            if direction == 'R':
                for nut_idx in range(10):
                    head[nut_idx][0] += 1
            elif direction == 'L':
                for nut_idx in range(10):
                    head[nut_idx][0] -= 1
            elif direction == 'U':
                for nut_idx in range(10):
                    head[nut_idx][1] += 1
            elif direction == 'D':
                for nut_idx in range(10):
                    head[nut_idx][1] -= 1

        for nut_idx in range(10):
            dx, dy = head[nut_idx][0] - tail[nut_idx][0], head[nut_idx][1] - tail[nut_idx][1]
            while abs(dx) > 1 or abs(dy) > 1:
                if dx != 0 and dy != 0:
                    tail[nut_idx][0] += dx // abs(dx)
                    tail[nut_idx][1] += dy // abs(dy)
                else:
                    tail[nut_idx][0] += dx // max(abs(dx), abs(dy))
                    tail[nut_idx][1] += dy // max(abs(dx), abs(dy))
                visited.add(tuple(tail[nut_idx]))
                dx, dy = head[nut_idx][0] - tail[nut_idx][0], head[nut_idx][1] - tail[nut_idx][1]

    return len(visited)

def read_motions_from_file(file_path):
    motions = []
    with open(file_path, 'r') as file:
        for line in file:
            direction, steps = line.strip().split()
            motions.append((direction, int(steps)))
    return motions

# Read the motions from the file
file_path = 'testdata.txt'
motions = read_motions_from_file(file_path)

print(simulate_rope(motions))
