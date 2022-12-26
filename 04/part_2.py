def parse_range(a):
    return [int(x) for x in a.split('-')]


def range_overlaps(a, b):
    a_min, a_max = a
    b_min, b_max = b
    return  a_min <= b_max and b_min <= a_max


with open('input.txt') as f:
    lines = f.read().splitlines()
    overlap_lines = 0
    for line in lines:
        a, b = (parse_range(x) for x in line.split(','))
        if range_overlaps(a, b):
            overlap_lines += 1
    print(overlap_lines)