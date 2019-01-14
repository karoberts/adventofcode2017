
import re
from collections import defaultdict

pat = re.compile(r'^([a-z]+) (inc|dec) ([\-\d]+) if ([a-z]+) (<|>|==|!=|<=|>=) ([\-\d]+)$')

regs = defaultdict(lambda:0)

with open('08.txt') as f:
    for line in (l.strip() for l in f):
        m = pat.match(line)
        cond_v = regs[m.group(4)]        
        cond_c = int(m.group(6))
        process = False
        if m.group(5) == '<': process = cond_v < cond_c
        elif m.group(5) == '<=': process = cond_v <= cond_c
        elif m.group(5) == '>': process = cond_v > cond_c
        elif m.group(5) == '>=': process = cond_v >= cond_c
        elif m.group(5) == '==': process = cond_v == cond_c
        elif m.group(5) == '!=': process = cond_v != cond_c

        if process:
            delt = int(m.group(3))
            delt *= -1 if m.group(2) == 'dec' else 1
            regs[m.group(1)] += delt

max_reg = max(regs, key=lambda x:regs[x])
print(max_reg, regs[max_reg])
        
