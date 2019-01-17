import re
from collections import Counter
from itertools import takewhile

pat = re.compile(r'^([xsp])([a-z]|\d+)(?:/([a-z]|\d+))?$')

pw = 'abcdefghijklmnop'
#pw = 'abcde'

def rotright(p, s):
    np = ''
    s = s % len(p)
    for i in range(len(p) - s, len(p)):
        np += p[i]
    for i in range(0, len(p) - s):
        np += p[i]
    return np

def rotleft(p, s):
    np = ''
    s = s % len(p)
    for i in range(s, len(p)):
        np += p[i]
    for i in range(0, s):
        np += p[i]
    return np

def swap(p, ia, ib):
    ta = ia
    ia = min(ia, ib)
    ib = max(ta, ib)
    return p[:ia] + p[ib] + p[ia+1:ib] + p[ia] + p[ib+1:]

with open('16.txt') as f:
    for cmd in f.readline().split(','):
        #print(cmd)
        m = pat.match(cmd)
        if m.group(1) == 'x':
            pw = swap(pw, int(m.group(2)), int(m.group(3)))
        elif m.group(1) == 'p':
            pw = swap(pw, pw.find(m.group(2)), pw.find(m.group(3)))
        elif m.group(1) == 's':
            pw = rotright(pw, int(m.group(2)))
        #print(pw)

print('part1', pw)

