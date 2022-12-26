import numpy as np

EMPTY = 0
OPEN = 1
WALL = 2

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

with open('input.txt') as f:
    rows = []
    lines = f.read().splitlines()
    for idx, line in enumerate(lines):
        if not line:
            moves = lines[idx + 1]
            break
        rows.append(line)
h = len(rows)
w = max(len(r) for r in rows)
grid = np.zeros((h, w))
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == '.':
            grid[i, j] = OPEN
        elif c == '#':
            grid[i, j] = WALL

orders = []
while moves:
    m, *moves = moves
    if m in ['L', 'R']:
        orders.append(m)
    else:
        try:
            next_l = moves.index('L')
        except ValueError:
            next_l = len(moves)
        try:
            next_r = moves.index('R')
        except ValueError:
            next_r = len(moves)
        next_turn = min(next_l, next_r)
        orders.append(int(m + ''.join(moves[:min(next_l, next_r)])))
        moves = moves[min(next_l, next_r):]

for j in range(w):
    if grid[0, j] == OPEN:
        pos = 0, j
        break
facing = RIGHT

for order in orders:
    if order == 'R':
        facing = (facing + 1) % 4
        continue
    elif order == 'L':
        facing = (facing - 1) % 4
        continue
    for _ in range(order):
        ti, tj = pos
        if facing == RIGHT:
            tj += 1
            if tj >= w or grid[ti, tj] == EMPTY:
                tj = 0
                while grid[ti, tj] == EMPTY:
                    tj += 1
        elif facing == DOWN:
            ti += 1
            if ti >= h or grid[ti, tj] == EMPTY:
                ti = 0
                while grid[ti, tj] == EMPTY:
                    ti += 1
        elif facing == LEFT:
            tj -= 1
            if tj < 0 or grid[ti, tj] == EMPTY:
                tj = w - 1
                while grid[ti, tj] == EMPTY:
                    tj -= 1
        elif facing == UP:
            ti -= 1
            if ti < 0 or grid[ti, tj] == EMPTY:
                ti = h - 1
                while grid[ti, tj] == EMPTY:
                    ti -= 1
        if grid[(ti, tj)] == WALL:
            break
        pos = ti, tj

x, y = pos
row_score = (x + 1) * 1000
col_score = (y + 1) * 4
print(sum((row_score, col_score, facing)))