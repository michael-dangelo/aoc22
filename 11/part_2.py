import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()
    monkeys = [{} for _ in range((len(lines) + 1) // 7)]
    for i, m in enumerate(monkeys):
        m.update({
            'items': [int(x) for x in lines[i * 7 + 1].replace(',', '').split()[2:]],
            'op': lines[i * 7 + 2].split()[-2],
            'amount': lines[i * 7 + 2].split()[-1],
            'test': int(lines[i * 7 + 3].split()[-1]),
            'true': int(lines[i * 7 + 4].split()[-1]),
            'false': int(lines[i * 7 + 5].split()[-1]),
            'inspected': 0,
        })

    common_mod = np.prod([x['test'] for x in monkeys], dtype=np.int64)
    for r in range(10_000):
        for m in monkeys:
            for item in m['items']:
                item %= common_mod
                amount = item if m['amount'] == 'old' else int(m['amount'])
                if m['op'] == '*':
                    worry = item * amount
                else:
                    worry = item + amount
                worry %= common_mod
                if worry % m['test'] == 0:
                    monkeys[m['true']]['items'].append(worry)
                else:
                    monkeys[m['false']]['items'].append(worry)
                m['inspected'] += 1
            m['items'].clear()

    sorted_monkeys = sorted(monkeys, key=lambda m: m['inspected'], reverse=True)
    print(sorted_monkeys[0]['inspected'] * sorted_monkeys[1]['inspected'])