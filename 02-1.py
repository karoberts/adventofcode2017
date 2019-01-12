with open('02.txt') as f:
    diff = 0
    for line in (l.strip() for l in f):
        ns = list(sorted((int(x.strip()) for x in line.split())))
        diff += ns[-1] - ns[0]
    print(diff)
