from aoc import l

inp,sam = l(1)

def parse(a):
    return [(1 if x[0] == 'R' else -1) * int(x[1:]) for x in a]

b = parse(inp)

def solve(l):
    val = 50
    res = 0
    rem = 0
    for x in l:
        prev_val = val
        t = val + x
        val = t % 100
        dr = abs(t // 100) + (-1 if t < 0 and prev_val == 0 else 0) + (-1 if t >= 100 and val == 0 else 0)
        rem += dr
        if val == 0:
            res += 1
        # print("{} {}->{} ({}, {})".format(x, prev_val, val, t, dr))
    return res, rem

w = solve(b)
print(w)
print(sum(w))
