depths = {
    0: 5,
    1: 2,
    2: 3,
    4: 4,
    6: 6,
    8: 4,
    10: 8,
    12: 6,
    14: 6,
    16: 14,
    18: 6,
    20: 8,
    22: 8,
    24: 10,
    26: 8,
    28: 8,
    30: 10,
    32: 8,
    34: 12,
    36: 9,
    38: 20,
    40: 12,
    42: 12,
    44: 12,
    46: 12,
    48: 12,
    50: 12,
    52: 12,
    54: 12,
    56: 14,
    58: 14,
    60: 14,
    62: 20,
    64: 14,
    66: 14,
    70: 14,
    72: 14,
    74: 14,
    76: 14,
    78: 14,
    80: 12,
    90: 30,
    92: 17,
    94: 18
}

#depths = { 0: 3, 1: 2, 4: 4, 6: 4 }

scanners = {k:[0,1] for k in depths.keys()}
for i in range(0, max(depths.keys())):
    if i not in depths:
        depths[i] = 0

me = -1
severity = 0
sp = 0
sd = 1
for i in range(0, max(depths.keys())+1):
    me += 1
    if me in scanners and scanners[me][sp] == 0:
        print('caught!', me)
        severity += (depths[me] * me)
    #print(i, [x[0] for x in scanners.values()], me)
    for s in scanners.keys():
        d = depths[s]
        if d == 0: continue
        if scanners[s][sd] == 1:
            if scanners[s][sp] == d - 1:
                scanners[s][sp] = d - 2
                scanners[s][sd] = -1
            else:
                scanners[s][sp] += 1
        else:
            if scanners[s][sp] == 0:
                scanners[s][sp] = 1
                scanners[s][sd] = 1
            else:
                scanners[s][sp] -= 1

print('part1', severity)