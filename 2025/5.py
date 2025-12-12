from aoc import *

inp,sam = l(5)

def parse_ranges(l):
    return [( int(x[:x.index('-')]), int(x[1+x.index('-'):])) for x in l]

def parse_num(l):
    return list(map(int, l))

def parse(l):
    i = l.index('')
    return(parse_ranges(l[:i]), parse_num(l[i+1:]))

a = parse(inp)
b = parse(sam)

def is_fresh(elem, r):
    for a in r:
        if elem >= a[0] and elem <= a[1]:
            return True
    return False

def solve(x):
    res = 0
    for i in x[1]:
        if is_fresh(i, x[0]):
            res += 1
    return res

print(solve(b))
print(solve(a))

def solve2(x):
    elems = sorted(x[0])
    res = 0
    largest = -1

    for elem in elems:
        if elem[0] > largest:
            res += elem[1]-elem[0]+1
            largest = elem[1]
        else:
            if elem[1] < largest:
                # fully contained
                continue
            else:
                res += elem[1] - largest 
                largest = elem[1]
    return res
    

print(solve2(b))
print(solve2(a))
