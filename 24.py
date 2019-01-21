import sys
from collections import defaultdict
from copy import deepcopy

max_bridge = 0

def maxsum(comps):
    s = sum(comps.keys())
    s += sum((0 if len(x) == 0 else max(x) for x in comps.values()))
    return s // 2

def dfs(comps, lp, sm, depth):
    global max_bridge

    #if maxsum(comps) + sm < max_bridge:
        #return -9999999999

    sums = []
    for p in comps[lp]:
        if depth == 0:
            print('trying 0/{}'.format(p))
        comps_ = deepcopy(comps)
        comps_[lp].remove(p)
        if lp in comps_[p]:
            comps_[p].remove(lp)
        sums.append(dfs(comps_, p, sm + p + lp, depth + 1))
    if len(sums) == 0:
        if sm > max_bridge:
            #print('bridge:', sm, depth)
            #sys.stdout.flush()
            max_bridge = sm
    return sm if len(sums) == 0 else max(sums)

with open('24.txt') as f:

    comps = defaultdict(set)
    for line in (l.strip() for l in f):
        pins = [int(i) for i in line.split('/')]
        if pins[1] in comps[pins[0]]: exit()
        if pins[0] in comps[pins[1]]: exit()
        comps[pins[0]].add(pins[1])
        comps[pins[1]].add(pins[0])

    #print(comps)

    #{19, 16, 43, 5}
    ret = dfs(comps, 0, 0, 0)
    print('part1', ret)

# < 2009
# > 776

# bridge: 776 29