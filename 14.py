
def knot_hash(st):
    sizes = [ord(c) for c in st] + [17, 31, 73, 47, 23]

    items = [x for x in range(0,256)]

    def rev(items, pos, length):
        spot = (pos + length - 1) % len(items)
        for i in range(0, length):
            yield items[spot]
            spot -= 1
            if spot == -1:
                spot = len(items) - 1

    def apply(items, pos, length):
        reved = [x for x in rev(items, pos, length)]
        for i in range(0, length):
            items[pos] = reved[i]
            pos = (pos + 1) % len(items)

    def xor(items, p):
        x = items[p]
        for i in range(0, 15):
            p += 1
            x ^= items[p]
        return x

    skip = 0
    pos = 0
    for round in range(0, 64):
        for s in sizes:
            apply(items, pos, s)
            pos = (pos + s + skip) % len(items)
            skip += 1

    dense = [xor(items, p) for p in range(0, 256, 16)]

    #print(dense)

    return dense

def hexhash(dense):
    return ''.join(('{:02x}'.format(c) for c in dense))

def k(x,y): return str(x) + ',' + str(y)

key = 'nbysizxe'
#key = 'flqrgnkx'
nbits = 0

grid = {}

y = 0
for row in range(0, 128):
    h = knot_hash(key + '-' + str(row))
    x = 0
    for hi in h:
        binstr = '{:0>8}'.format(bin(hi)[2:])
        nbits += binstr.count('1')
        for xd in range(0, 8):
            grid[k(x + xd,y)] = binstr[xd] == '1'
        x += 8
    y += 1

print('part1', nbits)

group_ctr = 0

def expand(x,y,grid):
    global group_ctr
    q = [(x,y)]

    while len(q) > 0:
        n = q.pop()
        tests = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for t in tests:
            tx = n[0] + t[0]
            ty = n[1] + t[1]
            if tx < 0 or tx > 127 or ty < 0 or ty > 127: continue
            tk = k(tx, ty)
            if isinstance(grid[tk], bool) and grid[tk]:
                #print('adding to group {} at {},{}'.format(group_ctr, tx,ty))
                grid[tk] = group_ctr
                q.append((tx, ty))

for y in range(0, 128):
    for x in range(0, 128):
        ck = k(x,y)
        if isinstance(grid[ck], bool) and grid[ck]:
            group_ctr += 1
            #print('new group ({}) at {},{}'.format(group_ctr,x,y))
            expand(x,y, grid)

print('part2', group_ctr)