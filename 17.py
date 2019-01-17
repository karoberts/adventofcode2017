import sys
import dllist

steps = 359
#steps = 3

ls = dllist.dllist()
cur = ls.insert(0)
zero = cur

def jumpnext(cur, js):
    for j in range(0, js):
        if cur.next is None: cur = cur.list.first
        else: cur = cur.next
    return cur

for i in range(1, 2018):
    jumps = steps if steps < len(ls) else steps - len(ls) % steps
    cur = jumpnext(cur, jumps)
    ls.insert(i, after = cur)
    cur = cur.next
    #print(cur, ls)

print('part1', cur.next.value)

spin_len = 1
cur_pos = 0
after_zero = -1
for i in range(1, 50000000):
    jumps = steps
    while jumps > spin_len:
        jumps -= spin_len
    if cur_pos + jumps >= spin_len: 
        jumps -= (spin_len - cur_pos)
        cur_pos = jumps
    else:
       cur_pos += jumps
    if cur_pos == 0:
        #print(i)
        after_zero = i
    spin_len += 1
    cur_pos += 1
print('part2', after_zero)
exit()

# I eventually realized (thanks to reddit thread) that I don't need to store the whole list, just keep track of length and position
ls = dllist.dllist()
cur = ls.insert(0)
zero = cur

last_zero = -1
for i in range(1, 50000000):
    jumps = steps if steps < len(ls) else steps - len(ls) % steps
    cur = jumpnext(cur, jumps)
    ls.insert(i, after = cur)
    cur = cur.next
    #print(cur, ls)
    z = jumpnext(zero, 1).value
    if z != last_zero:
        print(i, z)
        last_zero = z
        sys.stdout.flush()
    if i % 100000 == 0:
        print(i)
        sys.stdout.flush()

print('part2', jumpnext(zero, 1).value)

"""
this is the sequence, but I don't see the pattern, took 15 mins to process
1 1
2 2
3 3
4 4
5 5
6 6
11 11
12 12
26 26
168 168
191 191
261 261
531 531
2616 2616
117908 117908
182477 182477
455678 455678
2345315 2345315
6693248 6693248
9190833 9190833
22074523 22074523
39479736 39479736
"""