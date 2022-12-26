from collections import defaultdict

with open('input.txt') as f:
    stacks, moves = (x.splitlines() for x in f.read().split('\n\n'))
    state_dict = defaultdict(list)
    for line in stacks:
        cur = 0
        idx = line.find('[', cur)
        while idx != -1:
            state_dict[idx // 4].insert(0, line[idx + 1])
            cur = idx + 1
            idx = line.find('[', cur)
    state = [state_dict[i] for i in range(len(state_dict))]

    for line in moves:
        amount, source, target = (int(x) for x in line.split()[1::2])
        for _ in range(amount):
            if not state[source - 1]:
                break
            state[target - 1].append(state[source - 1].pop())

    print("".join([x.pop() for x in state if x]))