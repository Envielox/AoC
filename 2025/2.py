from aoc import l

inp,sam = l(2)

def parse(l):
    w = l[0].split(',')
    return [(int(x[:x.index('-')]),int(x[1+x.index('-'):])) for x in w]

a = parse(inp)
b = parse(sam)

def is_double(x):
    w = str(x)
    if len(w) % 2 == 1:
        return False
    return w[:len(w)//2] == w[len(w)//2:]

def is_nth(w, n):
    if len(w) % n != 0:
        return False
    plen = len(w)//n
    pattern = w[:plen]
    return all( [pattern == w[pos:pos+plen] for pos in range(0,len(w),plen) ] )

def is_multiple(x):
    w = str(x)
    return any([is_nth(w, i) for i in range(2,1+len(w))])


def solve(l):
    res = set()
    for a,b in l:
        for i in range(a,b+1):
            if is_double(i):
                res.add(i)
    return sum(res)

print(solve(b))
print(solve(a))

def solve2(l):
    res = set()
    for a,b in l:
        for i in range(a,b+1):
            if is_multiple(i):
                res.add(i)
    return sum(res)


print(solve2(b))
print(solve2(a))
