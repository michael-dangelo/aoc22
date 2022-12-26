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
    indexes = []
    for i in range(len(lines) // 3):
        x = eval(lines[i * 3])
        y = eval(lines[i * 3 + 1])
        try:
            compare(x, y)
        except CorrectOrder:
            indexes.append(i + 1)
        except IncorrectOrder:
            pass
    print(sum(indexes))