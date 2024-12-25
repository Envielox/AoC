input_file="inp12.txt"
sample_file="sample12.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)


from collections import defaultdict

f = {}

for y, row in enumerate(a):
    for x, elem in enumerate(row):
        f[x+y*1j] = elem
        
def in_map(pos):
    return pos.real >= 0 and pos.real < len(a) and pos.imag >= 0 and pos.imag < len(a[0])

def print_m(vals):
    for row in range(len(a)):
        l = ''
        for col in range(len(a[0])):
            p = (col + row*1j)
            if p in vals:
                l += '#'
            else:
                l += a[row][col]
        print(l)


def dfs(s):
    visited = set()
    to_visit = set([s])
    while len(to_visit) > 0:
        x = to_visit.pop()
        if x in visited:
            continue
        for d in [1, -1, 1j, -1j]:
            if in_map(d+x) and f[x] == f[x+d]:
                to_visit.add(x+d)
        visited.add(x)
    return visited
        

def peri(s):
    w = set()
    for d in [1, -1, 1j, -1j]:
        w.update(set([x+d for x in s]))
    return w.difference(s)

def peri_len(s):
    p = peri(s)
    res = 0
    for elem in p:
        for d in [1, -1, 1j, -1j]:
            if elem + d in s:
                res += 1
    return res

visited = set()
res = 0
for elem in f:
    if elem in visited:
        continue
    d = dfs(elem)
    res += len(d) * peri_len(d)
    visited.update(d)


print(res)


def side_len(s):
    p = peri(s)
    res = set()
    for elem in p:
        for d in [1, -1, 1j, -1j]:
            if elem + d in s:
                res.add((elem, elem+d)) # peri, inside
    to_remove = set()
    for elem in res:
        if elem in to_remove:
            continue
        for d in [1,-1, 1j, -1j]:
            idx = 1
            while (elem[0] + d*idx, elem[1] + d*idx) in res:
                to_remove.add((elem[0] + d*idx, elem[1] + d*idx))
                idx += 1
    return len(res) - len(to_remove)


visited = set()
res = 0
for elem in f:
    if elem in visited:
        continue
    d = dfs(elem)
    res += len(d) * side_len(d)
    visited.update(d)


print(res)
















