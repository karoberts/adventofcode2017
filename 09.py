
with open('09.txt') as f:
    l = f.readline().strip()

    groups = []
    score = 0
    count = 0

    gbg = False
    p = 0
    while p < len(l):
        c = l[p]
        if not gbg:
            if c == '{':
                score += len(groups) + 1
                groups.append(p)
            elif c == '}':
                groups.pop()
            elif c == '<':
                gbg = True
            elif c == '!':
                p += 1
        elif c == '>':
            gbg = False
        elif c == '!':
            p += 1
        else:
            count += 1

        p += 1

    print('part1', score)
    print('part2', count)