with open('input.txt') as f:
    lines = f.read().splitlines()
    x = 1
    clock = 1
    signal_sum = 0
    for line in lines:
        if line == 'noop':
            if clock % 40 == 20:
                signal_sum += clock * x
            clock += 1
        else:
            _, increment = line.split()
            if clock % 40 in [19, 20]:
                signal_sum += x * (clock + (0 if clock % 40 == 20 else 1))
            x += int(increment)
            clock += 2
    print(signal_sum)