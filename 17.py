import dllist

steps = 359
#steps = 3

ls = dllist.dllist()
cur = ls.insert(0)

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