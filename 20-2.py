import re
import sys
from collections import defaultdict
from itertools import count

points = []
with open('20.txt') as f:
    pat = re.compile(r'^p=<([\-\d]+),([\-\d]+),([\-\d]+)>, v=<([\-\d]+),([\-\d]+),([\-\d]+)>, a=<([\-\d]+),([\-\d]+),([\-\d]+)>$')

    for line in (l.strip() for l in f):
        m = pat.match(line)
        points.append({'p':[int(m.group(1)), int(m.group(2)), int(m.group(3))],
                       'v':[int(m.group(4)), int(m.group(5)), int(m.group(6))],
                       'a':(int(m.group(7)), int(m.group(8)), int(m.group(9))),
                       'id':len(points),
                       'alive': True
                       })

def key(p): return str(p['p'])

for round in range(0, 100):
    locs = defaultdict(list)
    found = False
    for p in points:
        if not p['alive']: continue
        for i in range(0, 3):
            p['v'][i] += p['a'][i]
            p['p'][i] += p['v'][i]
        k = key(p)
        if k in locs:
            found = True
        locs[k].append(p['id'])

    if found:
        for k, v in filter(lambda x:len(x[1]) > 1, locs.items()):
            print('COLLIDE', k, v)
            for p in v:
                points[p]['alive'] = False
            print(round, 'remaining', sum(1 for x in points if x['alive']))
            sys.stdout.flush()

    