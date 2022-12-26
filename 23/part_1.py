from collections import Counter

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

OFFSETS = {
    NORTH: {(-1, -1), (-1, 0), (-1, 1)},
    SOUTH: {(1, -1), (1, 0), (1, 1)},
    WEST: {(-1, -1), (0, -1), (1, -1)},
    EAST: {(-1, 1), (0, 1), (1, 1)},
}


def neighbours(elf, direction=None):
    x, y = elf
    if direction is not None:
        return {(x + i, y + j) for i, j in OFFSETS[direction]}
    return {(x + i, y + j) for p in OFFSETS.values() for i, j in p}


def move(elf, direction):
    x, y = elf
    if direction == NORTH:
        x -= 1
    elif direction == SOUTH:
        x += 1
    elif direction == WEST:
        y -= 1
    elif direction == EAST:
        y += 1
    return x, y


elves = set()
with open('input.txt') as f:
    for i, line in enumerate(f.read().splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                elves.add((i, j))

direction = NORTH
for _ in range(10):
    moves = {}
    for elf in elves:
        if not (elves & neighbours(elf)):
            continue
        for i in range(4):
            d = (direction + i) % 4
            if not (elves & neighbours(elf, d)):
                moves[elf] = d
                break
    if len(moves) == 0:
        'no elves need to move'
        break
    targets = {elf: move(elf, d) for elf, d in moves.items()}
    illegal_targets = {target for target, count in Counter(targets.values()).items() if count > 1}
    for elf, target in targets.items():
        if target not in illegal_targets:
            elves.remove(elf)
            elves.add(target)
    direction = (direction + 1) % 4
min_x = min(x for x, _ in elves)
max_x = max(x for x, _ in elves)
min_y = min(y for _, y in elves)
max_y = max(y for _, y in elves)
area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(area - len(elves))