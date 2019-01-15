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

def find_group(tgt):
    q = [tgt]
    found = set(q)
    while len(q) > 0:
        n = q.pop()
        if n != tgt and n in found:
            continue
        found.add(n)
        for r in conns[n]:
            if n == r: continue
            q.append(r)
    return found

with_zero = find_group(0)
print('part1', len(with_zero))

groups = []
for n in conns.keys():
    found = False
    for g in groups:
        if n in g:
            found = True
            break
    if not found:
        g = find_group(n)
        #print('new group, size', len(g))
        groups.append(g)

print('part2', len(groups))