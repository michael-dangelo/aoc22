DECRYPTION_KEY = 811589153

with open('input.txt') as f:
    values = [int(line) * DECRYPTION_KEY for line in f.read().splitlines()]
n = len(values)
indexes = list(range(n))

for _ in range(10):
    for i in range(n):
        move = values[i]
        start = indexes.index(i)
        new_index = (start + move) % (n - 1)
        indexes.insert(new_index, indexes.pop(start))

ordered = [values[i] for i in indexes]
zero_idx = ordered.index(0)
print(sum(ordered[(zero_idx + i) % n] for i in [1000, 2000, 3000]))