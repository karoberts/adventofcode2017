
with open('11.txt') as f:
    dirs = f.readline().strip().split(',')

"""
https://www.redblobgames.com/grids/hexagons/  <- axial coordinates
https://gamedevelopment.tutsplus.com/tutorials/hexagonal-character-movement-using-axial-coordinates--cms-29035   <- axial manhattan dist
  \ n  /       \0,-1/  
nw +--+ ne -1,0 +--+ 1,-1
  /    \       /    \  
-+      +-   -+      +-
  \    /       \    /  
sw +--+ se -1,1 +--+ 1,0
  / s  \       /0,1 \  
"""

def axial_manhat(i,j):
    di=i-0
    dj=j-0
    j -= (i//2)
    si=-1 if di < 0 else 1
    sj=-1 if dj < 0 else 1
    absi=di*si
    absj=dj*sj
    return max(absi, absj) if si != sj else absi + absj

axial_directions = {
    'se':(+1, 0), 'ne':(+1, -1), 'n':(0, -1), 
    'nw':(-1, 0), 'sw':(-1, +1), 's':(0, +1)
}

hx = 0
hy = 0
max_dist = -1
for d in dirs:
    delt = axial_directions[d]
    hx += delt[0]
    hy += delt[1]
    dist = axial_manhat(hx, hy)
    if dist > max_dist:
        max_dist = dist

print(hx, hy)
print('part1', axial_manhat(hx, hy))
print('part2', max_dist)