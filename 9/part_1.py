import math


def distance(p, q):
    return math.sqrt(sum((px - qx) ** 2 for px, qx in zip(p, q)))


with open('input.txt') as f:
    lines = f.read().splitlines()
    head = [0, 0]
    tail = [0, 0]
    visited = {tuple(tail)}
    for line in lines:
        direction, amount = line.split()
        for _ in range(int(amount)):
            if direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            elif direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            if distance(head, tail) >= 2:
                hx, hy = head
                tx, ty = tail
                if hx > tx:
                    tail[0] += 1
                elif hx < tx:
                    tail[0] -= 1
                if hy > ty:
                    tail[1] += 1
                elif hy < ty:
                    tail[1] -= 1
            visited.add(tuple(tail))
    print(len(visited))