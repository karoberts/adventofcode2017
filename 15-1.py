A, B = 722, 354
#A, B = 65, 8921

Af, Bf = 16807, 48271
def gen(prev, factor):
    return (prev * factor) % 0x7FFFFFFF

a = A
b = B
ct = 0
for p in range(0,40000000):
    a = gen(a, Af)
    b = gen(b, Bf)

    if (a & 0xFFFF) == (b & 0xFFFF):
        ct += 1
print('part1', ct)
