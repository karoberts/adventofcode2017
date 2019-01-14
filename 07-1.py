import re
from collections import defaultdict

pat = re.compile(r'^([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?$')

nodes = defaultdict(list)

with open('07.txt') as f:
    for line in (l.strip() for l in f):
        m = pat.match(line)
        k = m.group(1)
        if m.group(3):
            for s in (x.strip() for x in m.group(3).split(',')):
                nodes[s].append(k)

        if k not in nodes:
            nodes[k] = list()

    #print(nodes)
    for k, n in nodes.items():
        if len(n) == 0:
            print('part1', k)
