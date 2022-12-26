import re


def compute_monkey(monkey):
    op = monkey['operator']
    if op == 'const':
        return monkey['constant']

    x, y = [compute_monkey(monkeys[a]) for a in monkey['operands']]
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x // y


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
            'operator': operator,
            'constant': int(expr) if expr.isnumeric() else None,
            'operands': operands if not expr.isnumeric() else None,
        }
print(compute_monkey(monkeys['root']))