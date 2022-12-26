def char_priority(char):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27


with open('input.txt') as f:
    lines = f.readlines()
    priorities = []
    for line in lines:
        mid = len(line) // 2
        a, b = set(line[:mid]), set(line[mid:])
        common, = a.intersection(b)
        priorities.append(char_priority(common))
    print(sum(priorities))