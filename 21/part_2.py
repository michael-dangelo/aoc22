import re


def compute_monkey(monkey, humn):
    if monkey['name'] == 'humn':
        if humn is None:
            raise RuntimeError()
        return humn

    op = monkey['operator']
    if op == 'const':
        return monkey['constant']

    x, y = [compute_monkey(monkeys[a], humn) for a in monkey['operands']]
    if monkey['name'] == 'root':
        return x == y
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y


monkeys = {}
with open('input.txt') as f:
    for line in f.read().splitlines():
        name, expr = [x.strip() for x in line.split(':')]
        if expr.isnumeric():
            operator = 'const'
        else:
            operator, = re.findall(r'[\+\-\*\/]', expr)
            operands = re.findall(r'[a-z]+', expr)
        monkeys[name] = {
            'name': name,
            'operator': operator,
            'constant': int(expr) if expr.isnumeric() else None,
            'operands': operands if not expr.isnumeric() else None,
        }
x, y = [monkeys[a] for a in monkeys['root']['operands']]
try:
    target = compute_monkey(x, humn=None)
    non_const = y
except RuntimeError:
    target = compute_monkey(y, humn=None)
    non_const = x
i = 0
d = 10000000000
cache = set()
while True:
    if i in cache:
        d //= 2
    cache.add(i)
    x = compute_monkey(non_const, humn=i + d)
    y = compute_monkey(non_const, humn=i - d)
    dx = abs(target - x)
    dy = abs(target - y)
    if dx == 0:
        result = i + d
        break
    elif dy == 0:
        result = i - d
        break
    elif dx < dy:
        i += d
    elif dy < dx:
        i -= d
print(result)