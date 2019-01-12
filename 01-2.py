with open('01.txt') as f:
    line = f.readline().strip()
    skip = len(line) // 2

    sum = 0
    for i in range(0, len(line)):
        if line[i] == line[(i + skip) % len(line)]:
            sum += int(line[i])

    print(sum)