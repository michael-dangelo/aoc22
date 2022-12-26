with open('input.txt') as f:
    stream = f.read().strip()
    for i in range(len(stream)):
        packet = stream[i:i + 4]
        if len(packet) == len(set(packet)):
            print(i + 4)
            break