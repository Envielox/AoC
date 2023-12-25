import re

with open('5.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

s = b.index('')

stack = b[:s]
ops = b[s+1:]

cols = [x for x in stack[-1].split(' ') if x != '']

crates = {}
for c in cols:
    elem = stack[-1].index(c)
    single_stack = [row[elem] for row in stack[-2::-1] if row[elem] != ' ']
    crates[c] = single_stack

pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
op = [pattern.match(x).groups() for x in ops]

def step(num, fro, to):
    for x in range(int(num)):
        crates[to].append(crates[fro].pop())

def step2(num, fro, to):
    crates[to].extend(crates[fro][-int(num):])
    for x in range(int(num)):
        crates[fro].pop()

for o in op:
    step2(*o)

res = []
for k,v in crates.items():
    res.append(v[-1])

print(''.join(res))
