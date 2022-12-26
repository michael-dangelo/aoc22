def char_priority(char):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27


with open('input.txt') as f:
    lines = f.read().splitlines()
    priorities = []
    for a, b, c in [lines[i:i + 3] for i in range(0, len(lines), 3)]:
        a, b, c = set(a), set(b), set(c)
        common, = a.intersection(b).intersection(c)
        priorities.append(char_priority(common))
    print(sum(priorities))