import re

from pulp import (
    LpMaximize,
    LpProblem,
    LpStatus,
    lpSum,
    LpVariable,
    PULP_CBC_CMD,
    value
)

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
PASS = 4


def max_geodes_for_blueprint(blueprint):
    HORIZON = 24
    time = list(range(1, HORIZON + 1))
    problem = LpProblem(f"Blueprint_{blueprint['id']}", LpMaximize)
    build_ore = LpVariable.dicts("build_ore", time, cat="Binary")
    build_clay = LpVariable.dicts("build_clay", time, cat="Binary")
    build_obsidian = LpVariable.dicts("build_obsidian", time, cat="Binary")
    build_geode = LpVariable.dicts("build_geode", time, cat="Binary")
    time_plus_1 = list(range(1, HORIZON + 2))
    ore = LpVariable.dicts("ore", time_plus_1, lowBound=0, cat="Integer")
    ore_bots = LpVariable.dicts("ore_bots", time_plus_1, lowBound=0, cat='Integer')
    clay = LpVariable.dicts("clay", time_plus_1, lowBound=0, cat="Integer")
    clay_bots = LpVariable.dicts("clay_bots", time_plus_1, lowBound=0, cat='Integer')
    obsidian = LpVariable.dicts("obsidian", time_plus_1, lowBound=0, cat="Integer")
    obsidian_bots = LpVariable.dicts("obsidian_bots", time_plus_1, lowBound=0, cat='Integer')
    geodes = LpVariable.dicts("geodes", time_plus_1, lowBound=0, cat="Integer")
    geode_bots = LpVariable.dicts("geode_bots", time_plus_1, lowBound=0, cat='Integer')
    ore[1] = 0
    ore_bots[1] = 1
    clay[1] = 0
    clay_bots[1] = 0
    obsidian[1] = 0
    obsidian_bots[1] = 0
    geodes[1] = 0
    geode_bots[1] = 0
    for i in time:
        # Can only build one bot at a time.
        problem += build_ore[i] + build_clay[i] + build_obsidian[i] + build_geode[i] <= 1
        # Can only build a bot if we have the resources at the start of the turn.
        problem += (
            ore[i]
            - (build_ore[i] * blueprint[ORE][ORE])
            - (build_clay[i] * blueprint[CLAY][ORE])
            - (build_obsidian[i] * blueprint[OBSIDIAN][ORE])
            - (build_geode[i] * blueprint[GEODE][ORE])
        ) >= 0
        problem += clay[i] - (build_obsidian[i] * blueprint[OBSIDIAN][CLAY]) >= 0
        problem += obsidian[i] - (build_geode[i] * blueprint[GEODE][OBSIDIAN]) >= 0
        # Bot transitions.
        problem += ore_bots[i + 1] == ore_bots[i] + build_ore[i]
        problem += clay_bots[i + 1] == clay_bots[i] + build_clay[i]
        problem += obsidian_bots[i + 1] == obsidian_bots[i] + build_obsidian[i]
        problem += geode_bots[i + 1] == geode_bots[i] + build_geode[i]
        # Resource transitions.
        problem += ore[i + 1] == (
            ore[i]
            + ore_bots[i]
            - (build_ore[i] * blueprint[ORE][ORE])
            - (build_clay[i] * blueprint[CLAY][ORE])
            - (build_obsidian[i] * blueprint[OBSIDIAN][ORE])
            - (build_geode[i] * blueprint[GEODE][ORE])
        )
        problem += clay[i + 1] == clay[i] + clay_bots[i] - (build_obsidian[i] * blueprint[OBSIDIAN][CLAY])
        problem += obsidian[i + 1] == obsidian[i] + obsidian_bots[i] - (build_geode[i] * blueprint[GEODE][OBSIDIAN])
        problem += geodes[i + 1] == geodes[i] + geode_bots[i]
    problem += geodes[HORIZON + 1]
    problem.solve(PULP_CBC_CMD(msg=False))
    return int(value(problem.objective))


blueprints = []
with open('input.txt') as f:
    for line in f.read().splitlines():
        bp_id, ore_bot_ore, clay_bot_ore, obs_bot_ore, obs_bot_clay, geo_bot_ore, geo_bot_obs = [
            int(x) for x in re.findall(r'\d+', line)
        ]
        blueprints.append({
            'id': bp_id,
            ORE: {ORE: ore_bot_ore},
            CLAY: {ORE: clay_bot_ore},
            OBSIDIAN: {ORE: obs_bot_ore, CLAY: obs_bot_clay},
            GEODE: {ORE: geo_bot_ore, OBSIDIAN: geo_bot_obs},
        })
print(sum(b['id'] * max_geodes_for_blueprint(b) for b in blueprints))