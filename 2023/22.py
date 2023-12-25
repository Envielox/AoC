with(open('inp22.txt') as f) :
     raw=f.read()

raw2 = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

a = raw[:-1].split('\n')

b = [tuple(map(lambda x: tuple(map(int, x.split(','))), row.split('~')
               ) ) for row in a]

xs = [x[0][0] for x in b] + [x[1][0] for x in b]
ys = [x[0][1] for x in b] + [x[1][1] for x in b]

W = max(xs)+1
H = max(ys)+1

c = sorted(b, key=lambda x: x[0][2])

g = [ [(0, -1) for c in range(W)] for r in range(H)]
rests = {}
rh = {}

def horizontal_profile(block):
    if block[0][2] != block[1][2]:
        return [(block[0][0], block[0][1])]
    if block[0][0] == block[1][0]:
        return [(block[0][0], i) for i in range(block[0][1],block[1][1]+1)]
    if block[0][1] == block[1][1]:
        return [(i, block[0][1]) for i in range(block[0][0],block[1][0]+1)]
    raise Exception('Bad block')

def fall(idx):
    block = c[idx]
    hp = horizontal_profile(block)  
    height = max([g[pos[1]][pos[0]][0] for pos in hp])
    below = [g[y][x][1] for x,y in hp if g[y][x][0] == height] if height != 0 else []
    rests[idx] = below
    rh[idx] = height + 1
    if len(hp) != 1:
        for pos in hp:
            g[pos[1]][pos[0]] = (height+1, idx)
    else:
        delta_h = block[1][2] - block[0][2]
        g[block[0][1]][block[0][0]] = (height + 1 + delta_h, idx)

def solve(DEBUG=False):
    for i in range(len(c)):
        fall(i)
        if DEBUG:
            print(c[i])
            for r in g: print(r)
            print()
        yield
s = solve(False)
list(s)

critical = [0] * len(c)
for k, v in rests.items():
    if len(set(v)) == 1:
        critical[v[0]] += 1

print(len([x for x in critical if x == 0]))

above = {k: [] for k in range(len(c))}

for k, v in rests.items():
    for elem in v:
        above[elem].append(k)

from queue import PriorityQueue

def drop(idx):
    d = set([idx])
    c = PriorityQueue()
    list(map(lambda x: c.put((rh[x], x)), above[idx]))
    visited = set()
    while not c.empty():
        _, elem = c.get()
        if elem in visited:
            continue
        visited.add(elem)
        #print(elem)
        r = [x for x in rests[elem] if x not in d]
        if len(r) > 0:
            continue
        d.add(elem)
        list(map(lambda x: c.put((rh[x], x)), above[elem]))
    return len(d)

res = 0
for i in range(len(c)):
    res += drop(i) - 1
    print(i, res)
print(res)
        

    

