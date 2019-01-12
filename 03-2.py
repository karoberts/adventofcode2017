
n = 312051

x = 0
y = 0

sp_size = 3
i = 1    

grid = {'0,0':1}

def key(x,y):
    return str(x) + ',' + str(y)

def calcit(x,y):
    s = 0
    tests = [(-1,-1), (0,-1), (1,-1),  (1,0),(1,1),  (0,1),(-1,1),  (-1,0)]
    for t in tests:
        tx = x + t[0]
        ty = y + t[1]
        k = key(tx,ty)
        if k in grid:
            s += grid[k]
    print(s)
    if s > n:
        print('part2', s)
        exit()
    return s

def check(x, y):
    grid[key(x,y)] = calcit(x,y)

while True:
    x += 1
    check(x, y)

    for j in range(0, sp_size - 2):
        y -= 1
        check(x, y)
    for j in range(0, sp_size - 1):
        x -= 1
        check(x, y)
    for j in range(0, sp_size - 1):
        y += 1
        check(x, y)
    for j in range(0, sp_size - 1):
        x += 1
        check(x, y)

    sp_size += 2
        