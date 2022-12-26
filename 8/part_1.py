import numpy as np

with open('input.txt') as f:
    lines = np.array([[int(x) for x in line] for line in f.read().splitlines()])
    h, w = lines.shape
    vis_planes = [np.ones((h, w)) for _ in range(4)]
    for r in range(4):
        vis_plane = vis_planes[r]
        for i in range(h):
            row_max_height = -1
            for j in range(w):
                height = lines[i, j]
                if height <= row_max_height:
                    vis_plane[i, j] = 0
                row_max_height = max(row_max_height, height)
        lines = np.rot90(lines)
        vis_planes[r] = np.rot90(vis_plane, -r)

    visibility = np.stack(vis_planes)
    visibility = visibility.any(axis=0)
    print(np.count_nonzero(visibility))