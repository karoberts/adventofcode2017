with open('02.txt') as f:
    diff = 0
    divdiff = 0
    for line in (l.strip() for l in f):
        ns = list(sorted((int(x.strip()) for x in line.split())))
        diff += ns[-1] - ns[0]
        done = False
        for i in range(0, len(ns)):
            for j in range(i + 1, len(ns)):
                if ns[j] % ns[i] == 0:
                    #print(ns[j], ns[i])
                    divdiff += (ns[j] // ns[i])
                    done = True
                    break
            if done: break
    print('part1', diff)
    print('part2', divdiff)
