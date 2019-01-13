with open('05.txt') as f:
    insts = [int(x.strip()) for x in f]

    part = 2

    ip = 0
    jumps = 0
    while ip >= 0 and ip < len(insts):
        #print(jumps, ip, insts[ip])
        jmp = insts[ip]
        if part == 1:
            insts[ip] += 1
        elif part == 2:
            if insts[ip] >= 3:
                insts[ip] -= 1
            else:
                insts[ip] += 1
        jumps += 1
        ip += jmp

        #if jumps % 100000 == 0:
            #print('j', jumps)

    print('ip =', ip)
    print('jumps =', jumps)