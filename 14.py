
def knot_hash(st):
    sizes = [ord(c) for c in st] + [17, 31, 73, 47, 23]

    items = [x for x in range(0,256)]

    def rev(items, pos, length):
        spot = (pos + length - 1) % len(items)
        for i in range(0, length):
            yield items[spot]
            spot -= 1
            if spot == -1:
                spot = len(items) - 1

    def apply(items, pos, length):
        reved = [x for x in rev(items, pos, length)]
        for i in range(0, length):
            items[pos] = reved[i]
            pos = (pos + 1) % len(items)

    def xor(items, p):
        x = items[p]
        for i in range(0, 15):
            p += 1
            x ^= items[p]
        return x

    skip = 0
    pos = 0
    for round in range(0, 64):
        for s in sizes:
            apply(items, pos, s)
            pos = (pos + s + skip) % len(items)
            skip += 1

    dense = [xor(items, p) for p in range(0, 256, 16)]

    #print(dense)

    return dense

def hexhash(dense):
    return ''.join(('{:02x}'.format(c) for c in dense))

key = 'nbysizxe'
nbits = 0
for row in range(0, 128):
    h = knot_hash(key + '-' + str(row))
    for hi in h:
        nbits += bin(hi).count('1')
print(nbits)