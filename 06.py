bank_data = '11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11'

banks = [int(x) for x in bank_data.split(',')]

def g_maxbank(banks):
    maxi = 0
    for i in range(1, len(banks)):
        if banks[i] > banks[maxi]: maxi = i
    return maxi

cfgs = set()
cycles = 0
look_for = None
p1 = True
while True:
    bank = g_maxbank(banks)
    blocks = banks[bank]
    banks[bank] = 0
    bank = (bank + 1) % len(banks)
    while blocks > 0:
        banks[bank] += 1
        blocks -= 1
        bank = (bank + 1) % len(banks)
    cycles += 1
    key = str(banks)
    if p1:
        if key in cfgs:
            print('part1', cycles)
            p1 = False
            cycles = 0
            look_for = key
        cfgs.add(key)
    else:
        if key == look_for:
            print('part2', cycles)
            break

    
