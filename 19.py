from collections import defaultdict

grid = defaultdict(lambda:' ')

def key(x,y): return '{},{}'.format(x,y)

with open('19.txt') as f:
    max_x = -1
    y = 0
    for line in f:
        x = 0
        for c in line:
            grid[key(x,y)] = c
            x += 1
        max_x = x
        y += 1

start_x = -1
for x in range(0, max_x):
    if grid[key(x,0)] == '|':
        start_x = x
        break

dir = [0, 1]
lets = set([chr(a) for a in range(ord('A'), ord('Z') + 1)])
going = set(['|', '-', '+'])

px = start_x
py = 0
path = ''
steps = 0
while True:
    k = key(px, py)
    c = grid[k]
    steps += 1

    #print(k, dir, c)

    if c in lets:
        path += c

    kn = key(px + dir[0], py + dir[1])
    cn = grid[kn]

    if cn in going or cn in lets:
        px += dir[0]
        py += dir[1]
        continue

    if dir[1] != 0:
        kn = key(px - 1, py)
        cn = grid[kn]
        if cn in going or cn in lets:
            dir[0] = -1
            dir[1] = 0
            px -= 1
            continue
        kn = key(px + 1, py)
        cn = grid[kn]
        if cn in going or cn in lets:
            dir[0] = 1
            dir[1] = 0
            px += 1
            continue
        print('going up/down no path')
        break
    else:
        kn = key(px, py - 1)
        cn = grid[kn]
        if cn in going or cn in lets:
            dir[0] = 0
            dir[1] = -1
            py -= 1
            continue
        kn = key(px, py + 1)
        cn = grid[kn]
        if cn in going or cn in lets:
            dir[0] = 0
            dir[1] = 1
            py += 1
            continue
        print('going right/left no path')
        break

print('part1', path)
print('part2', steps)