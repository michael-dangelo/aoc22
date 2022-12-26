class CorrectOrder(Exception):
    pass


class IncorrectOrder(Exception):
    pass


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            raise CorrectOrder
        if a == b:
            return
        if a > b:
            raise IncorrectOrder
    elif isinstance(a, list) and isinstance(b, list):
        a = a.copy()
        b = b.copy()
        for _ in range(max(len(a), len(b))):
            try:
                x = a.pop(0)
            except IndexError:
                raise CorrectOrder
            try:
                y = b.pop(0)
            except IndexError:
                raise IncorrectOrder
            compare(x, y)
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])


with open('input.txt') as f:
    lines = f.read().splitlines()
    packets = [eval(line) for line in lines if line != '']
    packets.extend([[[2]], [[6]]])
    n = len(packets)
    for i in range(n):
        is_sorted = True
        for j in range(n - i - 1):
            try:
                compare(packets[j], packets[j + 1])
            except CorrectOrder:
                pass
            except IncorrectOrder:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
                is_sorted = False
        if is_sorted:
            break
    result = 1
    for i, p in enumerate(packets, start=1):
        if p in [[[2]], [[6]]]:
            result *= i
    print(result)