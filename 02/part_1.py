SHAPE_SCORES = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

OUTCOME_SCORES = {
    ('A', 'X'): 3,  # Rock Rock
    ('A', 'Y'): 6,  # Rock Paper
    ('A', 'Z'): 0,  # Rock Scissors
    ('B', 'X'): 0,  # Paper Rock
    ('B', 'Y'): 3,  # Paper Paper
    ('B', 'Z'): 6,  # Paper Scissors
    ('C', 'X'): 6,  # Scissors Rock
    ('C', 'Y'): 0,  # Scissors Paper
    ('C', 'Z'): 3,  # Scissors Scissors
}

with open('input.txt') as f:
    rounds = [x.split() for x in f.readlines()]
    print(sum(SHAPE_SCORES[ours] + OUTCOME_SCORES[theirs, ours] for theirs, ours in rounds))