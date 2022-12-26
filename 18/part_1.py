import numpy as np

OFFSETS = [
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
]

points = []
max_loc = 0
with open('input.txt') as f:
    for line in f.read().splitlines():
        x, y, z = (int(a) for a in line.split(','))
        points.append((x, y, z))
        max_loc = max(max_loc, x, y, z)

space = np.zeros((max_loc + 1,) * 3)
for p in points:
    space[p] = 1

def out_of_bounds(p):
    return any(x < 0 or x > max_loc for x in p)

count = 0
for x in range(max_loc + 1):
    for y in range(max_loc + 1):
        for z in range(max_loc + 1):
            if not space[x, y, z]:
                continue
            for a, b, c in OFFSETS:
                t, u, v = x + a, y + b, z + c
                if out_of_bounds((t, u, v)) or not space[t, u, v]:
                    count += 1
print(count)