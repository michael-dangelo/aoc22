import numpy as np

EMPTY = 0
OPEN = 1
WALL = 2

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

# Face configuration for test.txt.
TEST_FACES = {
    'size': 4,
    1: {
        'i': 0,
        'j': 2,
        RIGHT: (6, RIGHT),
        DOWN: (4, UP),
        LEFT: (3, UP),
        UP: (2, UP),
    },
    2: {
        'i': 1,
        'j': 0,
        RIGHT: (3, LEFT),
        DOWN: (5, DOWN),
        LEFT: (6, DOWN),
        UP: (1, UP),
    },
    3: {
        'i': 1,
        'j': 1,
        RIGHT: (4, LEFT),
        DOWN: (5, LEFT),
        LEFT: (2, RIGHT),
        UP: (1, LEFT),
    },
    4: {
        'i': 1,
        'j': 2,
        RIGHT: (6, UP),
        DOWN: (5, UP),
        LEFT: (3, RIGHT),
        UP: (1, DOWN),
    },
    5: {
        'i': 2,
        'j': 2,
        RIGHT: (6, LEFT),
        DOWN: (2, DOWN),
        LEFT: (3, DOWN),
        UP: (4, DOWN),
    },
    6: {
        'i': 2,
        'j': 3,
        RIGHT: (1, RIGHT),
        DOWN: (2, LEFT),
        LEFT: (5, RIGHT),
        UP: (4, RIGHT)
    }
}

# Face configuration for input.txt.
FACES = {
    'size': 50,
    1: {
        'i': 0,
        'j': 1,
        RIGHT: (2, LEFT),
        DOWN: (3, UP),
        LEFT: (4, LEFT),
        UP: (6, LEFT),
    },
    2: {
        'i': 0,
        'j': 2,
        RIGHT: (5, RIGHT),
        DOWN: (3, RIGHT),
        LEFT: (1, RIGHT),
        UP: (6, DOWN),
    },
    3: {
        'i': 1,
        'j': 1,
        RIGHT: (2, DOWN),
        DOWN: (5, UP),
        LEFT: (4, UP),
        UP: (1, DOWN),
    },
    4: {
        'i': 2,
        'j': 0,
        RIGHT: (5, LEFT),
        DOWN: (6, UP),
        LEFT: (1, LEFT),
        UP: (3, LEFT),
    },
    5: {
        'i': 2,
        'j': 1,
        RIGHT: (2, RIGHT),
        DOWN: (6, RIGHT),
        LEFT: (4, RIGHT),
        UP: (3, DOWN),
    },
    6: {
        'i': 3,
        'j': 0,
        RIGHT: (5, DOWN),
        DOWN: (2, UP),
        LEFT: (1, UP),
        UP: (4, DOWN),
    },
}

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


def transfer_to_face(i, j, facing):
    # FACES = TEST_FACES
    size = FACES['size']
    for face in range(1, 7):
        f = FACES[face]
        if i // size == f['i'] and j // size == f['j']:
            src_face = face
            dst_face_name, dst_edge = f[facing]
            break
    rotation = (facing - dst_edge) % 4
    dst_face = FACES[dst_face_name]
    if rotation == 0:
        if facing == RIGHT:
            i = (dst_face['i'] * size) + size - 1 - (i % size)
        elif facing == DOWN:
            j = (dst_face['j'] * size) + size - 1 - (j % size)
        elif facing == LEFT:
            i = (dst_face['i'] * size) + size - 1 - (i % size)
        elif facing == UP:
            j = (dst_face['j'] * size) + size - 1 - (j % size)
        facing = (facing + 2) % 4
    elif rotation == 1:
        if facing == RIGHT:
            j = (dst_face['j'] * size) + size - 1 - (i % size)
        elif facing == DOWN:
            i = (dst_face['i'] * size) + (j % size)
        elif facing == LEFT:
            j = (dst_face['j'] * size) + size - 1 - (i % size)
        elif facing == UP:
            i = (dst_face['i'] * size) + (j % size)
        facing = (facing + rotation) % 4
    elif rotation == 2:
        if facing == RIGHT:
            i = (dst_face['i'] * size) + (i % size)
        elif facing == DOWN:
            j = (dst_face['j'] * size) + (j % size)
        elif facing == LEFT:
            i = (dst_face['i'] * size) + (i % size)
        elif facing == UP:
            j = (dst_face['j'] * size) + (j % size)
    elif rotation == 3:
        if facing == RIGHT:
            j = (dst_face['j'] * size) + (i % size)
        elif facing == DOWN:
            i = ((dst_face['i'] + 1) * size) - 1 - (j % size)
        elif facing == LEFT:
            j = (dst_face['j'] * size) + (i % size)
        elif facing == UP:
            i = ((dst_face['i'] + 1) * size) - 1 - (j % size)
        facing = (facing + rotation) % 4
    if facing == RIGHT:
        j = (dst_face['j'] * size)
    elif facing == DOWN:
        i = (dst_face['i'] * size)
    elif facing == LEFT:
        j = ((dst_face['j'] + 1) * size) - 1
    elif facing == UP:
        i = ((dst_face['i'] + 1) * size) - 1
    return i, j, facing


for order in orders:
    if order == 'R':
        facing = (facing + 1) % 4
        continue
    elif order == 'L':
        facing = (facing - 1) % 4
        continue
    for _ in range(order):
        ti, tj = pos
        tfacing = facing
        if facing == RIGHT:
            tj += 1
        elif facing == DOWN:
            ti += 1
        elif facing == LEFT:
            tj -= 1
        elif facing == UP:
            ti -= 1
        if ti < 0 or tj < 0 or ti >= h or tj >= w or grid[ti, tj] == EMPTY:
            ti, tj, tfacing = transfer_to_face(*pos, facing)
        if grid[(ti, tj)] == WALL:
            break
        pos = ti, tj
        facing = tfacing

x, y = pos
row_score = (x + 1) * 1000
col_score = (y + 1) * 4
print(sum((row_score, col_score, facing)))