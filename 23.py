from collections import defaultdict
import re
import sys

program = []
with open('23.txt') as f:

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
nmuls = 0
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

    if op[0] == '#':
        ip += 1
        continue

    if op == 'set':
        regs[r] = v2
    elif op == 'sub':
        regs[r] -= v2
    elif op == 'mul':
        regs[r] *= v2
        nmuls += 1
    elif op == 'jnz':
        if v1 != 0:
            ip += v2 - 1

    ip += 1

    #print(ip, regs, pline)

#print(regs)
print('part1', nmuls)

def isprime(n):
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# see 23-program.py
# through some considerable analysis, discovered that the program is counting how many numbers
# between 107900 and 124900 (every 17) are not prime
print('part2', sum((1 for b in range(107900, 124901, 17) if not isprime(b))))