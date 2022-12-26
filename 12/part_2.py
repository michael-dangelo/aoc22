import numpy as np


def height(char):
    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'
    return ord(char)


def in_bounds(p, grid):
    h, w = grid.shape
    x, y = p
    return 0 <= x < h and 0 <= y < w


def neighbours(p, grid):
    x, y = p
    n = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [a for a in n if in_bounds(a, grid)]


with open('input.txt') as f:
    grid = np.array([list(line) for line in f.read().splitlines()])
    h, w = grid.shape
    stack = [(i, j) for i in range(h) for j in range(w)]
    distance = {(i, j): float('inf') for i in range(h) for j in range(w)}
    previous = {(i, j): None for i in range(h) for j in range(w)}
    distance[tuple(x.item() for x in np.where(grid == 'E'))] = 0
    while stack:
        a = sorted(stack, key=lambda p: distance[p])[0]
        stack.remove(a)
        for nx, ny in neighbours(a, grid):
            n = (nx, ny)
            if n not in stack or height(grid[a]) > height(grid[n]) + 1:
                continue
            new_distance = distance[a] + 1
            if new_distance < distance[n]:
                distance[n] = new_distance
                previous[n] = a

    end_positions = list(zip(*np.where(grid == 'a')))
    end_positions.append(tuple(x.item() for x in np.where(grid == 'S')))
    min_moves = float('inf')
    for pos in end_positions:
        if not previous[pos]:
            continue
        path = []
        while pos:
            path.insert(0, pos)
            pos = previous[pos]
        min_moves = min(min_moves, len(path) - 1)
    print(min_moves)