import re


def distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


def perimeter(x, y, radius):
    for i in range(radius + 1, 0, -1):
        x_offset = radius + 1 - i
        yield from [
            (x + x_offset, y + i),
            (x - x_offset, y + i),
            (x + x_offset, y - i),
            (x - x_offset, y - i),
        ]


with open('input.txt') as f:
    MAX = 4_000_000
    sensors = []
    for line in f.read().splitlines():
        sx, sy, bx, by = [int(x) for x in re.findall(r'-?\d+', line)]
        radius = distance(sx, sy, bx, by)
        sensors.append((sx, sy, radius))

    for sx, sy, radius in sensors:
        for px, py in perimeter(sx, sy, radius):
            if px < 0 or px >= MAX or py < 0 or py >= MAX:
                continue
            for tx, ty, tradius in sensors:
                if (tx, ty) == (sx, sy):
                    continue
                if distance(tx, ty, px, py) <= tradius:
                   break
            else:
                print(px * 4_000_000 + py)
                exit()