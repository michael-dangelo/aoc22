with open('input.txt') as f:
    print(max(sum(int(y) for y in x.split('\n') if y != '') for x in f.read().split('\n\n')))