from aoc import l

inp,sam = l(3)

def parse(l):
    return [list(map(int,x)) for x in l]

a = parse(inp)
b = parse(sam)

def get_best(l):
    m = max(l[:-1])
    i = l.index(m)
    m2 = max(l[i+1:])
    return m * 10 + m2

#for x in b:
#   print(get_best2(x, 12))

def solve(x):
    return sum(map(get_best, x))


#print(solve(b))
print(solve(a))

def get_best2(l, n):
    if n == 1:
        return max(l)
    m = max(l[:-(n-1)])
    i = l.index(m)
    return m * 10**(n-1) + get_best2(l[i+1:], n-1)

def solve2(x):
    return sum(map(lambda x: get_best2(x, 12), x))


#print(solve2(b))
print(solve2(a))
