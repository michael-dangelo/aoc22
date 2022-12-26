def draw_pixel(crt, x, i, j):
    if j in [x - 1, x, x + 1]:
        crt[i][j] = '#'
    j += 1
    if j == 40:
        j = 0
        i += 1
    return i, j


with open('input.txt') as f:
    lines = f.read().splitlines()
    x = 1
    crt = [['.'] * 40 for _ in range(6)]
    i = 0
    j = 0
    for line in lines:
        if line == 'noop':
            i, j = draw_pixel(crt, x, i, j)
        else:
            for _ in range(2):
                i, j = draw_pixel(crt, x, i, j)
            _, increment = line.split()
            x += int(increment)
    for row in crt:
        print("".join(row))