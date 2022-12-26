def neighbours(pos, end, size, blizzards):
    OFFSETS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    result = set()
    x, y = pos
    h, w = size
    candidates = [pos] + [(x + i, y + j) for i, j in OFFSETS]
    for s, t in candidates:
        if (s, t) == end:
            result.add((s, t))
            continue
        if s <= 0 or s >= h - 1 or t <= 0 or t >= w - 1:
            continue
        if (s, t) in {(x, y) for x, y, _ in blizzards}:
            continue
        result.add((s, t))
    return result


def move_blizzards(blizzards, time, size):
    h, w = size
    result = []
    for x, y, facing in blizzards:
        if facing == '^':
            x = (((x - 1) - time) % (h - 2)) + 1
        elif facing == 'v':
            x = (((x - 1) + time) % (h - 2)) + 1
        elif facing == '<':
            y = (((y - 1) - time) % (w - 2)) + 1
        elif facing == '>':
            y = (((y - 1) + time) % (w - 2)) + 1
        result.append((x, y, facing))
    return result


with open('input.txt') as f:
    lines = f.read().splitlines()
    h = len(lines)
    w = len(lines[0])
    pos = 0, lines[0].index('.')
    end = h - 1, lines[-1].index('.')
    blizzards = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in ['^', 'v', '<', '>']:
                blizzards.append((i, j, c))
    visited = set([(pos, 0)])
    queue = [(pos, 0)]
    while queue:
        v, t = queue.pop(0)
        if v == end:
            print(t)
            break
        b = move_blizzards(blizzards, t + 1, (h, w))
        for n in neighbours(v, end, (h, w), b):
            if (n, t + 1) not in visited:
                visited.add((n, t + 1))
                queue.append((n, t + 1))