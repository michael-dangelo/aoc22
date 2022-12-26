import re

with open('input.txt') as f:
    ROW = 2_000_000
    lines = f.read().splitlines()
    known = set()
    blocked = set()
    for line in lines:
        sx, sy, bx, by = [int(x) for x in re.findall(r'-?\d+', line)]
        known.update([(sx, sy), (bx, by)])
        extent = abs(sx - bx) + abs(sy - by) - abs(ROW - sy)
        if extent <= 0:
            continue
        for i in range(-extent, extent + 1):
            blocked.add((sx + i, ROW))
    print(len(blocked - known))