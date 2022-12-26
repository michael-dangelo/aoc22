import functools
import re

with open('input.txt') as f:
    adjacency = {}
    flows = {}
    for line in f.read().splitlines():
        name, *targets = re.findall(r'[A-Z]{2}', line)
        flow = int(re.search(r'\d+', line)[0])
        adjacency[name] = targets
        flows[name] = flow

    valves = {name for name, flow in flows.items() if flow > 0}
    distance = {}
    for v in valves | {'AA'}:
        costs = {v: 0}
        stack = [v]
        visited = set()
        while stack:
            x = stack.pop(0)
            for t in adjacency[x]:
                if t not in visited:
                    visited.add(t)
                    costs[t] = costs[x] + 1
                    stack.append(t)
        for t, c in costs.items():
            if t != v:
                distance[(v, t)] = c

    def generate_paths(time, pos, valves):
        yield (pos,)
        for v in valves:
            t = time + distance[(pos, v)] + 1
            if t >= 26:
                yield tuple()
                continue
            for path in generate_paths(t, v, valves - {v}):
                yield (pos,) + path

    @functools.lru_cache(maxsize=None)
    def score_path(path):
        t = 0
        score = 0
        pos, *path = path
        for p in path:
            t += distance[(pos, p)] + 1
            if t >= 26:
                break
            score += flows[p] * (26 - t)
            pos = p
        return score

    paths = generate_paths(0, 'AA', valves)
    scored_paths = [(score_path(p), p) for p in generate_paths(0, 'AA', valves)]
    scored_paths = sorted(scored_paths, reverse=True)
    max_score = 0
    for s, p in scored_paths:
        for t, r in scored_paths:
            if s + t < max_score:
                break
            if not (set(p[1:]) & set(r[1:])):
                max_score = max(max_score, s + t)
    print(max_score)