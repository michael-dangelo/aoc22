from functools import lru_cache

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

lava = np.zeros((max_loc + 1,) * 3)
for p in points:
    lava[p] = 1

def out_of_bounds(p):
    return any(x < 0 or x > max_loc for x in p)

def is_airpocket(p):
    visited = set()
    queue = [p]
    while queue:
        a = queue.pop(0)
        for o in OFFSETS:
            r = tuple(x + i for x, i in zip(a, o))
            if out_of_bounds(r):
                return False
            if lava[r] or r in visited:
                continue
            visited.add(r)
            queue.append(r)
    return True

count = 0
for x in range(max_loc + 1):
    for y in range(max_loc + 1):
        for z in range(max_loc + 1):
            if not lava[x, y, z]:
                continue
            for a, b, c in OFFSETS:
                p = x + a, y + b, z + c
                if out_of_bounds(p) or (not lava[p] and not is_airpocket(p)):
                    count += 1
print(count)