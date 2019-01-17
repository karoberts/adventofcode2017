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

ip = 0

regs = defaultdict(lambda:0)

stmts = 0
last_freq = -1
while True:
    if ip >= len(program) or ip < 0:
        print('HALT')
        break

    stmts += 1
    pline = program[ip]
    #print('ip={} {} {} ip='.format(ip, regs, pline['l']), end='')
    op = pline['op']
    v1 = regs[pline['1']] if pline['n1'] is None else pline['n1']
    v2 = regs[pline['2']] if pline['n2'] is None else pline['n2']
    r = pline['1']

    if op == 'snd':
        last_freq = v1
    elif op == 'set':
        regs[r] = v2
    elif op == 'add':
        regs[r] += v2
    elif op == 'mul':
        regs[r] *= v2
    elif op == 'mod':
        regs[r] %= v2
    elif op == 'rcv':
        if v1 > 0:
            regs[r] = last_freq
            print('part1', last_freq)
            exit()
    elif op == 'jgz':
        if v1 > 0:
            ip += v2 - 1

    #if regs['d'] > last_d:
        #last_d = regs['d']
        #print(ip, regs)

    ip += 1

    #print(ip, regs, pline)

print(regs)
