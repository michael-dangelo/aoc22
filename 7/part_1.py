with open('input.txt') as f:
    lines = f.read().splitlines()
    fs = {}
    pwd = fs
    for line in lines:
        if line.startswith('$ cd'):
            target = line.split()[-1]
            if target == '/':
                pwd = fs
            elif target == '..':
                pwd = pwd['__parent__']
            else:
                pwd = pwd[target]
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            dir_name = line.split()[-1]
            if not pwd.get(dir_name):
                pwd[dir_name] = {'__parent__': pwd}
        else:
            size, filename = line.split()
            pwd[filename] = int(size)

    final_sum = 0

    def compute_directory_size(directory):
        global final_sum
        total_size = 0
        for k, v in directory.items():
            if k == '__parent__':
                continue
            if isinstance(v, int):
                total_size += v
            else:
                total_size += compute_directory_size(v)
        if total_size <= 100_000:
            final_sum += total_size
        return total_size

    compute_directory_size(fs)
    print(final_sum)