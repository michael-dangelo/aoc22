SHAPE_SCORES = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

MATCHUP_SCORES = {
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

OUTCOME_SCORES = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}


def move_for_outcome(theirs, outcome):
    for (t, o), score in MATCHUP_SCORES.items():
        if t == theirs and score == OUTCOME_SCORES[outcome]:
            return o


with open('input.txt') as f:
    rounds = [x.split() for x in f.readlines()]
    scores = []
    for theirs, outcome in rounds:
        ours = move_for_outcome(theirs, outcome)
        scores.append(SHAPE_SCORES[ours] + MATCHUP_SCORES[theirs, ours])
    print(sum(scores))