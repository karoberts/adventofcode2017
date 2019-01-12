with open('01.txt') as f:
    line = f.readline().strip()

    sum = 0
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            sum += int(line[i])
    if line[-1] == line[0]:
        sum += int(line[0])

    print(sum)