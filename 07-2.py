
import re
from collections import defaultdict

pat = re.compile(r'^([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?$')

class Node(object):
    __slots__ = ('__value', '__ptrs', '__key')

    def __init__(self, key, value=''):
        self.__ptrs = []
        self.__key = key
        self.__value = value

    def add_child(self, node):
        self.__ptrs.append(node)

    def get_children(self):
        return self.__ptrs

    def get_value(self):
        return self.__value

    def get_key(self):
        return self.__key

    def set_value(self, c):
        self.__value = c

    def __str__(self):
        if len(self.__ptrs) == 0:
            return 'node(' + str(self.__value) + ')'
        return 'node(' + str(self.__value) + '[' + ','.join((str(s) for s in self.__ptrs)) + '])'

    def __repr__(self):
        return '<node(' + str(self.__value) + '[' + ','.join((str(s) for s in self.__ptrs)) + '])>'

    def printit(self):
        self.__printit(self, 0)

    def __printit(self, n, d):
        print('  ' * d, 'node(' + str(n.__key) + ':' + str(n.__value) + ')')
        for c in n.__ptrs:
            self.__printit(c, d + 1)

nodes = {}

def sum_tree(n):
    return n.get_value() + sum((sum_tree(s) for s in n.get_children()))

with open('07.txt') as f:
    for line in (l.strip() for l in f):
        m = pat.match(line)
        k = m.group(1)
        v = int(m.group(2))
        p = nodes[k] if k in nodes else Node(k)
        p.set_value(v)
        nodes[k] = p
        if m.group(3):
            for s in (x.strip() for x in m.group(3).split(',')):
                n = nodes[s] if s in nodes else Node(s)
                p.add_child(n)
                nodes[s] = n

    root = 'gynfwly'
    #root = 'tknk'
    #nodes[root].printit()
    n = nodes[root]
    last = None
    while True:
        ss = defaultdict(list)
        if len(n.get_children()) == 0:
            break
        for c in n.get_children():
            ss[sum_tree(c)].append(c)
        a = min(ss, key=lambda x:len(ss[x]))
        b = max(ss, key=lambda x:len(ss[x]))
        if a == b:
            print('part2', last[0][last[1]][0].get_value() - (last[1]-last[2]))
            break
        print(a, ss[a][0].get_key(), ss[a][0].get_value(), b, ss[b][0].get_key(), ss[b][0].get_value(), len(ss[b]))
        last = (ss, a, b)
        n = ss[a][0] 



