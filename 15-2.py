A, B = 722, 354
#A, B = 65, 8921

Af, Bf = 16807, 48271
def gen(prev, factor):
    return (prev * factor) % 0x7FFFFFFF

a = A
b = B
ct = 0
for p in range(0,5000000):
    while True:
        a = (a * Af) % 0x7FFFFFFF
        #a = gen(a, Af)
        if a % 4 == 0: break

    while True:
        #b = gen(b, Bf)
        b = (b * Bf) % 0x7FFFFFFF
        if b % 8 == 0: break

    if (a & 0xFFFF) == (b & 0xFFFF):
        ct += 1
print('part2', ct)
