from functools import lru_cache

OFFSETS = {
    '-': [(i, 0) for i in range(4)],
    '+': [(1, 2), *((i, 1) for i in range(3)), (1, 0)],
    'L': [(2, 2), (2, 1), *((i, 0) for i in range(3))],
    'I': [(0, i) for i in range(4)],
    'O': [(i, j) for i in range(2) for j in range(2)],
}


@lru_cache(maxsize=None)
def points(t, x, y):
    return [(x + i, y + j) for i, j in OFFSETS[t]]


def collides(r, rocks):
    r_points = set(points(**r))
    min_x = min(x for x, _ in r_points)
    max_x = max(x for x, _ in r_points)
    min_y = min(y for _, y in r_points)
    if min_x < 0 or max_x > 6 or min_y < 0:
        return True
    for o in rocks:
        if set(points(**o)) & r_points:
            return True
    return False


with open('input.txt') as f:
    jet, = f.read().splitlines()

ROCK_TYPES = ['-', '+', 'L', 'I', 'O']
rocks = []
jet_index = 0
for i in range(2022):
    r = {
        't': ROCK_TYPES[i % len(ROCK_TYPES)],
        'x': 2,
        'y': (4 + max(y for r in rocks for x, y in points(**r))) if rocks else 3,
    }
    jet_turn = True
    while True:
        x = r.copy()
        if jet_turn:
            x['x'] += 1 if jet[jet_index] == '>' else -1
            if not collides(x, rocks):
                r = x
            jet_turn = False
            jet_index = (jet_index + 1) % len(jet)
        else:
            jet_turn = True
            x['y'] -= 1
            if collides(x, rocks):
                break
            r = x
    rocks.append(r)
print(max(y for r in rocks for _, y in points(**r)) + 1)