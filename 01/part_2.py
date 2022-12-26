with open('input.txt') as f:
    print(sum(sorted((sum(int(y) for y in x.split('\n') if y != '') for x in f.read().split('\n\n')), reverse=True)[:3]))