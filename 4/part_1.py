def parse_range(a):
    return [int(x) for x in a.split('-')]


def range_contains(a, b):
    a_min, a_max = a
    b_min, b_max = b
    return  a_min <= b_min and a_max >= b_max


with open('input.txt') as f:
    lines = f.read().splitlines()
    containing_lines = 0
    for line in lines:
        a, b = (parse_range(x) for x in line.split(','))
        if range_contains(a, b) or range_contains(b, a):
            containing_lines += 1
    print(containing_lines)