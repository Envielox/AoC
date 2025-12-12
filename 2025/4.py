from aoc import *

inp,sam = l(4)

a = parse_complex(inp, lambda x: x == '@')
b = parse_complex(sam, lambda x: x == '@')

def get_neigh(elem, l):
    return [elem + x for x in C_NEIGH if elem + x in l]

def get_neigh_cnt(elem, l):
    res = 0
    for n in get_neigh(elem, l):
        res += 1
    return res

def is_accessible(elem, l):
    return get_neigh_cnt(elem, l) < 4

def solve(l):
    res = 0
    for elem in l:
        if is_accessible(elem, l):
            res += 1
    return res

print(solve(b))
print(solve(a))

def solve2(l):
    res = 0
    remaining = l.copy()
    to_consider = l.copy()
    while len(to_consider) > 0:
        w = to_consider.pop()
        if is_accessible(w, remaining):
            remaining.remove(w)
            for n in get_neigh(w, remaining):
                to_consider.add(n)
    return len(l) - len(remaining)

print(solve2(b))
print(solve2(a))

        
