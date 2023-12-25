import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

with open('23.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

s = set()

for y, r in enumerate(b):
    for x, c in enumerate(r):
        if c == '#':
            s.add(x + 1j * y)

            
def p():
    r = [int(x.real) for x in s]
    i = [int(x.imag) for x in s]

    for y in range(min(i), max(i) + 1):
        for x in range(min(r), max(r) + 1):
            if x + 1j * y in s:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def neigh(p):
    n = [x+1j*y for x in range(-1, 2) for y in range(-1, 2)]
    return set([p + x for x in n if x != 0])

def has_neigh(p):
    n = neigh(p)
    return len(n.intersection(s)) > 0

dirs = [
    [-1-1j, -1j, +1-1j],
    [-1+1j, +1j, +1+1j],
    [-1-1j,  -1, -1+1j],
    [+1-1j,  +1, +1+1j],
]

def propose_move(p):
    for d in dirs:
        t = set([x + p for x in d])
        if len(t.intersection(s)) == 0:
            return d[1] + p

from collections import defaultdict

def round():
    to_move = [x for x in s if has_neigh(x)]
    proposals = [(propose_move(x), x) for x in to_move]
    proposals = [x for x in proposals if x[0] is not None]
    c = defaultdict(int)
    for p in proposals:
        c[p[0]] += 1

    res = 0
    for p in proposals:
        if c[p[0]] == 1:
            s.remove(p[1])
            s.add(p[0])
            res += 1
            
    global dirs
    dirs = dirs[1:] + [dirs[0]]
    return res
    
def score():
    r = [x.real for x in s]
    i = [x.imag for x in s]
    print(r)
    print(i)

    return (max(r) - min(r)+1) * (max(i) - min(i)+1) - len(s)

#p()
#for i in range(10):
#    print(i + 1)
#    round()
    #p()

i = 0
while round() != 0:
    i+= 1

print(i + 1)


    
