import sys
from collections import defaultdict

min_x = 0
max_x = 0
min_y = 0
max_y = 0

def print_grid(grid):
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            print(grid[x + y * 1j], end='')
        print()
    
with open('22.txt') as f:

    grid = defaultdict(lambda:'.')

    y = 0
    for line in (l.strip() for l in f):
        x = 0
        for c in line:
            grid[x + y * 1j] = c
            x += 1
        max_x = x
        y += 1
    max_y = y

    cur = max_x//2 + (max_y//2) * 1j

    #print_grid(grid)
    #print('cur',cur)

    ninfs = 0
    dir = 0 - 1j # up
    for burst in range(0, 10000000):
        if grid[cur] == '#':
            dir *= 1j # right
            grid[cur] = 'F'
        elif grid[cur] == '.':
            dir *= -1j # left
            grid[cur] = 'W'
        elif grid[cur] == 'F':
            dir *= -1 # 180
            grid[cur] = '.'
        elif grid[cur] == 'W':
            grid[cur] = '#'
            ninfs += 1

        cur += dir                

    print('part2', ninfs)


