import numpy as np

with open('input.txt') as f:
    rocks = []
    for line in f.read().splitlines():
        vertices = [tuple(int(x) for x in v.split(',')) for v in line.split(' -> ')]
        for a, b in zip(vertices, vertices[1:]):
            ax, ay = a
            bx, by = b
            if ax == bx:
                for y in range(min(ay, by), max(ay, by) + 1):
                    rocks.append([ax, y])
            else:
                for x in range(min(ax, bx), max(ax, bx) + 1):
                    rocks.append([x, ay])

    grid = np.zeros((10_000, 10_000))
    max_y = float('-inf')
    for x, y in rocks:
        grid[x, y] = 1
        max_y = max(max_y, y)
    grid[:, max_y + 2] = 1

    sand_count = 0
    sand = (500, 0)
    grid[sand] = 2
    while True:
        sx, sy = sand
        if grid[(sx, sy + 1)] == 0:
            grid[sand] = 0
            sand = (sx, sy + 1)
            grid[sand] = 2
            continue
        if grid[sx - 1, sy + 1] == 0:
            grid[sand] = 0
            sand = (sx - 1, sy + 1)
            grid[sand] = 2
            continue
        if grid[sx + 1, sy + 1] == 0:
            grid[sand] = 0
            sand = (sx + 1, sy + 1)
            grid[sand] = 2
            continue
        sand_count += 1
        if sand == (500, 0):
            break
        sand = (500, 0)
    print(sand_count)