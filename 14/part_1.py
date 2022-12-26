import numpy as np

with open('input.txt') as f:
    rocks = []
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')
    for line in f.read().splitlines():
        vertices = [tuple(int(x) for x in v.split(',')) for v in line.split(' -> ')]
        for (ax, ay), (bx, by) in zip(vertices, vertices[1:]):
            if ax == bx:
                for y in range(min(ay, by), max(ay, by) + 1):
                    rocks.append((ax, y))
            else:
                for x in range(min(ax, bx), max(ax, bx) + 1):
                    rocks.append((x, ay))
            min_x = min(min_x, min(ax, bx))
            min_y = min(min_y, min(ay, by))
            max_x = max(max_x, max(ax, bx))
            max_y = max(max_y, max(ay, by))

    grid = np.zeros((max_x + 1, max_y + 1))
    for x, y in rocks:
        grid[x, y] = 1

    sand_count = 0
    sand = (500, 0)
    grid[sand] = 2
    while True:
        sx, sy = sand
        if sy + 1 > max_y:
            break
        if grid[(sx, sy + 1)] == 0:
            grid[sand] = 0
            sand = (sx, sy + 1)
            grid[sand] = 2
            continue
        if sx - 1 < min_x:
            break
        if grid[sx - 1, sy + 1] == 0:
            grid[sand] = 0
            sand = (sx - 1, sy + 1)
            grid[sand] = 2
            continue
        if sx + 1 > max_x:
            break
        if grid[sx + 1, sy + 1] == 0:
            grid[sand] = 0
            sand = (sx + 1, sy + 1)
            grid[sand] = 2
            continue
        sand = (500, 0)
        sand_count += 1

    print(sand_count)