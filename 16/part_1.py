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

    def Q(time, pos, seen):
        if time >= 30 or valves == seen:
            return 0
        unseen = valves - seen
        max_score = 0
        for v in unseen:
            d = distance[(pos, v)]
            new_time = time + d + 1
            if new_time >= 30:
                continue
            new_seen = seen.copy()
            new_seen.add(v)
            score = flows[v] * (30 - new_time)
            score += Q(new_time, v, new_seen)
            max_score = max(max_score, score)
        return max_score

    print(Q(0, 'AA', set()))