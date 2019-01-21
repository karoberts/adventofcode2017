from collections import defaultdict

state = 'A'
diag = 12994925

states = {
    'A': [(1, 1, 'B'), (0, -1, 'F')],
    'B': [(0, 1, 'C'), (0, 1, 'D')],
    'C': [(1, -1, 'D'), (1, 1, 'E')],
    'D': [(0, -1, 'E'), (0, -1, 'D')],
    'E': [(0, 1, 'A'), (1, 1, 'C')],
    'F': [(1, -1, 'A'), (1, 1, 'A')]
}

tape = defaultdict(lambda:0)
cur = 0

for d in range(0, diag):
    curv = tape[cur]
    s = states[state]
    tape[cur] = s[curv][0]
    cur += s[curv][1]
    state = s[curv][2]

print(sum(tape.values()))