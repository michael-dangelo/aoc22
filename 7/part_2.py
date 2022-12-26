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

    minimum_size = float('inf')

    def compute_directory_size(directory, minimum_deletion=None):
        global minimum_size
        total_size = 0
        for k, v in directory.items():
            if k == '__parent__':
                continue
            if isinstance(v, int):
                total_size += v
            else:
                total_size += compute_directory_size(v, minimum_deletion)
        if minimum_deletion and total_size >= minimum_deletion:
            minimum_size = min(minimum_size, total_size)
        return total_size

    root_size = compute_directory_size(fs)
    compute_directory_size(fs, minimum_deletion=root_size - 40_000_000)
    print(minimum_size)