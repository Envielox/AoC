with(open('inp21.txt') as f) :
     raw=f.read()

raw2 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

a = raw[:-1].split('\n')

def get(l, pos):
    if pos.real < 0 or pos.real >= len(l[0]) or pos.imag < 0 or pos.imag >= len(l):
        return True
    return '#' == l[int(pos.imag)][int(pos.real)]

def get2(l, pos):
    return '#' == l[int(pos.imag) % len(l)][int(pos.real)%len(l[0])]

for y, row in enumerate(a):
    if 'S' in row:
        S = complex(row.index('S'), y)

def neigh(pos):
    return [x+pos for x in [1,-1,1j,-1j]]

def BFS(start=S, max_s=64, long=False):
    dists = {0:[start]}
    visited = set([start])
    for d in range(max_s):
        elems = dists[d]
        neighs = set([x for xs in map(neigh, elems) for x in xs if x not in visited])
        
        if long:
            res = [x for x in neighs if not get2(a, x)]
        else:
            res = [x for x in neighs if not get(a, x)]
        for x in res:
            visited.add(x)
        dists[d+1] = res
    return dists

def BFS2(start=S, long=False):
    elems = set([start])
    prev = set()
    while True:
        neighs = set([x for xs in map(neigh, elems) for x in xs if x not in prev])
        
        if long:
            res = [x for x in neighs if not get2(a, x)]
        else:
            res = [x for x in neighs if not get(a, x)]
        prev = dists
        elems = res
        yield elems

def solutions():
    g = BFS2(start=S, long=True)
    res = 1
    yield 1
    while True:
        odd = next(g)
        even = next(g)
        res += len(even)
        yield res

def interesting():
    s = solutions()
    for i in range(32):
        next(s)
    yield next(s)
    while True:
        for i in range(65):
            next(s)
        yield next(s)
        for i in range(64):
            next(s)
        yield next(s)
    

def get_even(d):
    res = set()
    for k, v in d.items():
        if k % 2 == 0:
            for x in v:
                res.add(x)
    return res

def get_odd(d):
    res = set()
    for k, v in d.items():
        if k % 2 == 1:
            for x in v:
                res.add(x)
    return res

def pp(l, d):
    for y in range(len(l)):
        s = ''
        for x in range(len(row)):
            if complex(x, y) in d:
                s = s + 'O'
            else:
                s = s + a[y][x]
        print(s)

def pp2(l,r, d):
    res = ''
    for y in range(-len(l) * r, len(l) * (r+1)):
        s = ''
        for x in range(-len(row)*r, len(l) * (r+1)):
            if complex(x, y) in d:
                s = s + 'O'
            else:
                s = s + a[y%len(l)][x%len(l[0])]
        res = res + s + '\n'
    with open('21out', 'w') as f:
        f.write(res)

e = get_even(BFS(start=S, max_s=64))
print(len(e))


vals = [3605, 32976, 90881, 178994,
        294805, 441660, 615377, 820974,
        1052597, 1316936, 1606465, 1929546,
        2276981, 2658804]
#vals.extend(map(int, "3064145 3504710 3967957 4467264 4988417 5546466 6125525 6742316 7379281 8054814 8749685 9483960 10236737 11029754 11840437".split(' ')))
center = BFS(start=S, max_s=65)
full = BFS(start=S, max_s=150)

center_even = get_even(center)
center_odd = get_odd(center)
full_even = get_even(full)
full_odd = get_odd(full)
sides_even = full_even.difference(center_even)
sides_odd = full_odd.difference(center_odd)


c_e = len(get_even(center))
c_n = len(get_odd(center))
s_e = len(get_even(full)) - c_e
s_n = len(get_odd(full)) - c_n

secret = 26501365
radius = secret // 131


def solve(s):
    e = 0
    n = 0
    for i in range(s+1):
        if i % 2 == 0:
            e = (i+1)**2
        else:
            n = (i+1)**2
    ff = 0 if s % 2 != 0 else s
    #ff = 0
    return (c_n * e + c_e*n) + (s_e + s_n) * (e+n-1) // 2 - ff


vals=list(map(int, "3710 32662 91404 178262 295746 440510 616736 819406 1054374 1314950 1608660 1927142".split(' ')))
print(vals)
print([solve(x) for x in range(len(vals))])
print(solve(radius))



vals2 = []
for i in range(0,100):
    r = len(get_odd(BFS(start=S, max_s=65+131*i, long=True)))
    print(i, r)
    vals2.append(r)

