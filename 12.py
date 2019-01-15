import re
from collections import defaultdict

pat = re.compile(r'^(\d+) <-> (\d+(?:, \d+)*)$')

conns = defaultdict(set)

with open('12.txt') as f:
    for line in (l.strip() for l in f):
        #print(line)
        m = pat.match(line)
        n = int(m.group(1))
        for r in (int(x) for x in m.group(2).split(',')):
            conns[n].add(r)
            conns[r].add(n)

q = [0]
found = set(q)
while len(q) > 0:
    n = q.pop()
    if n != 0 and n in found:
        continue
    found.add(n)
    for r in conns[n]:
        q.append(r)

print(len(found))