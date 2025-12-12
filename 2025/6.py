from aoc import *
from itertools import groupby


inp,sam = l(6)

def parse(l):
    num = [list(map(int,x.split())) for x in l[:-1]]
    ops = l[-1].split()
    return (num, ops)

a = parse(inp)
b = parse(sam)

def solve(l):
    vals = l[0][0][:]
    for row in l[0][1:]:
        for i, v in enumerate(row):
            if l[1][i] == '+':
                vals[i] += v
            else:
                vals[i] *= v
    return sum(vals)

print(solve(b))
print(solve(a))

def rotate(l):
    res = [[0] * len(l) for x in range(len(l[0]))]
    for y, row in enumerate(l):
        for x, val in enumerate(row):
            res[x][y] = val
    return res

def parse2(l):
    raw_inp = list(map(lambda x: ''.join(x).strip(), rotate(l[:-1])))
    new_inp = [list(group) for key, group in groupby(raw_inp, key=bool) if key]
    
    num = [list(map(int, x)) for x in new_inp]
    ops = l[-1].split()
    return (num, ops)

def product(l):
    if len(l) == 0:
        return 1
    return l[0] * product(l[1:])

def solve2(l):
    vals = [0] * len(l[0])
    for i, elems in enumerate(l[0]):
        if l[1][i] == '+':
            vals[i] = sum(elems)
        else:
            vals[i] = product(elems)
    return sum(vals)

c = parse2(inp)
d = parse2(sam)

print(solve2(d))
print(solve2(c))
