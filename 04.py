with open('04.txt') as f:
    valid1 = 0
    valid2 = 0
    for line in (l.strip() for l in f):
        tot1 = [x.strip() for x in line.split()]
        tot2 = [''.join(sorted(x.strip())) for x in line.split()]
        uni1 = set(tot1)
        uni2 = set(tot2)
        valid1 += 1 if len(tot1) == len(uni1) else 0
        valid2 += 1 if len(tot2) == len(uni2) else 0
    print('part1', valid1)
    print('part2', valid2)