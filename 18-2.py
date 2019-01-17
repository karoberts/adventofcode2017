from collections import defaultdict
import re

program = []
with open('18.txt') as f:

    for line in (l.strip() for l in f):
        if line.startswith('#'):
            continue

        m = line.split(' ')

        r1 = m[1]
        r2 = m[2] if len(m) > 2 else None

        n1 = int(r1) if re.match(r'^[\-]?\d+$', r1) else None
        n2 = int(r2) if r2 is not None and re.match(r'^[\-]?\d+$', r2) else None

        program.append({'op': m[0], 'args': m[1:], '1': r1, '2':r2, 'n1':n1, 'n2':n2, 'l': line})

ip = [0, 0]
blocked = [False, False]
q = [[], []]
sends = [0, 0]

regs = [defaultdict(lambda:0), defaultdict(lambda:0)]
regs[0]['p'] = 0
regs[1]['p'] = 1

stmts = 0
while True:
    for p in range(0, 2):
        othp = abs(p - 1)

        if ip[p] >= len(program) or ip[p] < 0:
            print(p, 'HALT')
            print('part2', sends[1])
            break

        stmts += 1
        pline = program[ip[p]]
        #print('ip={} {} {} ip='.format(p, ip, regs, pline['l']), end='')
        op = pline['op']
        v1 = regs[p][pline['1']] if pline['n1'] is None else pline['n1']
        v2 = regs[p][pline['2']] if pline['n2'] is None else pline['n2']
        r = pline['1']

        if op == 'snd':
            q[othp].insert(0, v1)
            sends[p] += 1
        elif op == 'set':
            regs[p][r] = v2
        elif op == 'add':
            regs[p][r] += v2
        elif op == 'mul':
            regs[p][r] *= v2
        elif op == 'mod':
            regs[p][r] %= v2
        elif op == 'rcv':
            if len(q[p]) == 0:
                blocked[p] = True
                if blocked[othp]:
                    print('DEADLOCK')
                    print('part2', sends[1])
                    exit()
                continue
            blocked[p] = False
            regs[p][r] = q[p].pop()
        elif op == 'jgz':
            if v1 > 0:
                ip[p] += v2 - 1

        #if regs['d'] > last_d:
            #last_d = regs['d']
            #print(ip, regs)

        ip[p] += 1

        #print(ip, regs, pline)

print(regs)
