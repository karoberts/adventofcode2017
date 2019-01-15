sizes = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]
#sizes = [3, 4, 1, 5]

items = [x for x in range(0,256)]
#items = [x for x in range(0,5)]

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

skip = 0
pos = 0
for s in sizes:
    apply(items, pos, s)
    pos = (pos + s + skip) % len(items)
    skip += 1

print(items)
print(items[0] * items[1])
