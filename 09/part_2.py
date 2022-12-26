import math


def distance(p, q):
    return math.sqrt(sum((px - qx) ** 2 for px, qx in zip(p, q)))


with open('input.txt') as f:
    lines = f.read().splitlines()
    positions = [[0, 0] for _ in range(10)]
    head, tail = positions[0], positions[-1]
    visited = {tuple(tail)}
    for line in lines:
        direction, amount = line.split()
        for _ in range(int(amount)):
            if direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            elif direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            for prev, cur in zip(positions, positions[1:]):
                if distance(prev, cur) >= 2:
                    px, py = prev
                    cx, cy = cur
                    if px > cx:
                        cur[0] += 1
                    elif px < cx:
                        cur[0] -= 1
                    if py > cy:
                        cur[1] += 1
                    elif py < cy:
                        cur[1] -= 1
            visited.add(tuple(tail))
    print(len(visited))