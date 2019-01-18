import re
from itertools import islice

points = []
with open('20.txt') as f:
    pat = re.compile(r'^p=<([\-\d]+),([\-\d]+),([\-\d]+)>, v=<([\-\d]+),([\-\d]+),([\-\d]+)>, a=<([\-\d]+),([\-\d]+),([\-\d]+)>$')

    for line in (l.strip() for l in f):
        m = pat.match(line)
        points.append({'p':[int(m.group(1)), int(m.group(2)), int(m.group(3))],
                       'v':[int(m.group(4)), int(m.group(5)), int(m.group(6))],
                       'a':(int(m.group(7)), int(m.group(8)), int(m.group(9))),
                       'd':0,
                       'id':len(points)
                       })

def manhat_dist(p):
    return abs(p[0]) + abs(p[1]) + abs(p[2])

def get_min():
    min_d = 999999999
    min_i = -1
    for i, p in enumerate(points):
        if p['d'] < min_d:
            min_d = p['d']
            min_i = i
    return min_i

# < 223

lowest = -1
for round in range(0, 1000):
    for p in points:
        for i in range(0, 3):
            p['v'][i] += p['a'][i]
            p['p'][i] += p['v'][i]
        p['d'] = manhat_dist(p['p'])
    min_i = get_min()
    if min_i != lowest:
        print('==>', min_i)
        lowest = min_i

    """
    if round % 100 == 0:
        print('round', round)
        for p in islice(sorted(points, key=lambda x:x['d']), 3):
            print('  ', p['id'], p['d'])
    """

for p in islice(sorted(points, key=lambda x:x['d']), 3):
    print('  ', p['id'], p['d'])
