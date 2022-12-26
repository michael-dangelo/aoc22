import numpy as np


def vector_score(v):
    score = 0
    for x in v[1:]:
        score += 1
        if x >= v[0]:
            break
    return score


with open('input.txt') as f:
    trees = np.array([[int(x) for x in line] for line in f.read().splitlines()])
    h, w = trees.shape
    max_score = 0
    for i in range(h):
        for j in range(w):
            score = (
                vector_score(np.flip(trees[:i + 1, j])) *
                vector_score(trees[i:, j]) *
                vector_score(np.flip(trees[i, :j + 1])) *
                vector_score(trees[i, j:])
            )
            max_score = max(max_score, score)
    print(max_score)