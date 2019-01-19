import sys

def key(x,y): return '{},{}'.format(x,y)

size = 3

def print_grid(grid):
    for y in range(0, size):
        for x in range(0, size):
            print('.' if grid[key(x,y)] == 0 else '#', end='')
        print()

def match(grid, x, y, rule):
    if len(rule) == 6:
        return grid[key(x,y)] == rule[0] and \
           grid[key(x + 1, y)] == rule[1] and \
           grid[key(x, y + 1)] == rule[2] and \
           grid[key(x + 1, y + 1)] == rule[3]
    else:
        return grid[key(x,y)] == rule[0] and \
           grid[key(x + 1, y)] == rule[1] and \
           grid[key(x + 2, y)] == rule[2] and \
           grid[key(x, y + 1)] == rule[3] and \
           grid[key(x + 2, y + 1)] == rule[5] and \
           grid[key(x, y + 2)] == rule[6] and \
           grid[key(x + 1, y + 2)] == rule[7] and \
           grid[key(x + 2, y + 2)] == rule[8]
    pass

def to01(c): return 0 if c == '.' else 1

def match_set(x, y, gx, gy, ms, msize, grid, new_grid):
    if msize == 2:
        for r in ms:
            if match(grid, x, y, r):
                #print('g {},{} from {},{} matched rule {}'.format(gx,gy,x,y,r[5]))
                rp = 0
                for ny in range(gy * 3, gy * 3 + 3):
                    for nx in range(gx * 3, gx * 3 + 3):
                        new_grid[key(nx, ny)] = to01(r[4][rp])
                        rp += 1
                break
    else:
        for r in ms:
            if grid[key(x + 1, y + 1)] != r[4]:
                continue
            if match(grid, x, y, r):
                #print('g {},{} from {},{} matched rule {}'.format(gx,gy,x,y,r[10]))
                rp = 0
                for ny in range(gy * 4, gy * 4 + 4):
                    for nx in range(gx * 4, gx * 4 + 4):
                        new_grid[key(nx, ny)] = to01(r[9][rp])
                        rp += 1
                break

def hflip_2(l):
    return [l[2], l[3], l[0], l[1]]
def vflip_2(l):
    return [l[1], l[0], l[3], l[2]]
def rot_2(l):
    return [l[2], l[0], l[3], l[1]]

def add_2(l, o, ls, s, li):
    if str(l) in s: return
    ls.append(l + [o, li])
    s.add(str(l))
def add_2p(l, o, ls, s, li):
    add_2(l, o, ls, s, li)
    add_2(vflip_2(l), o, ls, s, li)
    add_2(hflip_2(l), o, ls, s, li)
    add_2(hflip_2(vflip_2(l)), o, ls, s, li)

def hflip_3(l):
    return [l[6], l[7], l[8], l[3], l[4], l[5], l[0], l[1], l[2]]
def vflip_3(l):
    return [l[2], l[1], l[0], l[5], l[4], l[3], l[8], l[7], l[6]]
def rot_3(l):
    return [l[6], l[3], l[0], l[7], l[4], l[1], l[8], l[5], l[2]]

def add_3(l, o, ls, s, li):
    if str(l) in s: return
    ls.append(l + [o, li])
    s.add(str(l))
def add_3p(l, o, ls, s, li):
    add_3(l, o, ls, s, li)
    add_3(vflip_3(l), o, ls, s, li)
    add_3(hflip_3(l), o, ls, s, li)
    add_3(hflip_3(vflip_3(l)), o, ls, s, li)

with open('21.txt') as f:

    _2s = []
    _2set = set()
    _3s = []
    _3set = set()
    li = 0
    for line in (l.strip() for l in f):
        s = line.split(' => ')
        i = s[0].split('/')
        o = ''.join(s[1].split('/'))
        if len(i) == 2:
            l = [0] * 4
            l[0] = to01(i[0][0])
            l[1] = to01(i[0][1])
            l[2] = to01(i[1][0])
            l[3] = to01(i[1][1])
            add_2p(l, o, _2s, _2set, li)
            add_2p(rot_2(l), o, _2s, _2set, li)
            add_2p(rot_2(rot_2(l)), o, _2s, _2set, li)
            add_2p(rot_2(rot_2(rot_2(l))), o, _2s, _2set, li)
        else:
            l = [0] * 9
            l[0] = to01(i[0][0])
            l[1] = to01(i[0][1])
            l[2] = to01(i[0][2])
            l[3] = to01(i[1][0])
            l[4] = to01(i[1][1])
            l[5] = to01(i[1][2])
            l[6] = to01(i[2][0])
            l[7] = to01(i[2][1])
            l[8] = to01(i[2][2])
            add_3p(l, o, _3s, _3set, li)
            add_3p(rot_3(l), o, _3s, _3set, li)
            add_3p(rot_3(rot_3(l)), o, _3s, _3set, li)
            add_3p(rot_3(rot_3(rot_3(l))), o, _3s, _3set, li)
        li += 1

    """
    .#.
    ..#
    ###
    """
    grid = {'0,0':0, '1,0':1, '2,0':0,  '0,1':0, '1,1':0, '2,1':1,  '0,2':1, '1,2':1, '2,2': 1}
    print_grid(grid)

    for i in range(0, 18):
        new_grid = {}
        if size % 2 == 0:
            #print('2=>3')
            for y in range(0, size, 2):
                for x in range(0, size, 2):
                    match_set(x, y, x // 2, y // 2, _2s, 2, grid, new_grid)
            size = (size // 2) * 3
            pass
        else:
            #print('3=>4')
            for y in range(0, size, 3):
                for x in range(0, size, 3):
                    match_set(x, y, x // 3, y // 3, _3s, 3, grid, new_grid)
            size = (size // 3) * 4
            pass
        grid = new_grid
        print('  iter', i, sum(grid.values()), 'size', size)
        if i == 4:
            print('part1', sum(grid.values()))
        sys.stdout.flush()
        #print_grid(grid)

print('part2', sum(grid.values()))
