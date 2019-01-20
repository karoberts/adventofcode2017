import sys
from collections import defaultdict

def key(x,y): return '{},{}'.format(x,y)

min_x = 0
max_x = 0
min_y = 0
max_y = 0

def print_grid(grid):
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            print(grid[key(x,y)], end='')
        print()
    
right = {
 (0, -1): ( 1,  0),
 (1,  0): ( 0,  1),
 (0,  1): (-1,  0),
 (-1, 0): ( 0, -1)}

left = {
 (0, -1): (-1,  0),
 (-1, 0): ( 0,  1),
 (0,  1): ( 1,  0),
 ( 1, 0): ( 0, -1)}

with open('22.txt') as f:

    grid = defaultdict(lambda:'.')

    y = 0
    for line in (l.strip() for l in f):
        x = 0
        for c in line:
            grid[key(x,y)] = c
            x += 1
        max_x = x
        y += 1
    max_y = y

    cx = max_x // 2
    cy = max_x // 2

    print_grid(grid)
    print('cur',cx,cy)

    ninfs = 0
    dir = (0, -1) # up
    for burst in range(0, 10000):
        k = key(cx, cy)
        if grid[k] == '#': dir = right[dir]
        else: dir = left[dir]

        if grid[k] == '.':
            ninfs += 1
            grid[k] = '#'
        else:
            grid[k] = '.'

        cx += dir[0]
        cy += dir[1]

    print('part1', ninfs)

