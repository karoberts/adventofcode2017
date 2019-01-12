
n = 312051

x = 0
y = 0

sp_size = 3
i = 1    

def manhat_dist(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

def check(i, x, y):
    if i != n: return
    dist = manhat_dist(0, 0, x, y)
    print('part1', dist)

while i <= n:
    i += 1
    x += 1
    check(i, x, y)

    for j in range(0, sp_size - 2):
        i += 1
        y -= 1
        check(i, x, y)
    for j in range(0, sp_size - 1):
        i += 1
        x -= 1
        check(i, x, y)
    for j in range(0, sp_size - 1):
        i += 1
        y += 1
        check(i, x, y)
    for j in range(0, sp_size - 1):
        i += 1
        x += 1
        check(i, x, y)
    if i != sp_size ** 2:
        print('bad', i, sp_size, x,y)
        exit()

    sp_size += 2
        