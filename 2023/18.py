with(open('inp18.txt') as f) :
     raw=f.read()

raw2 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

a = raw[:-1].split('\n')

b = []
for elem in a:
    x,y,z = elem.split(' ')
    b.append((x, int(y), z[2:-1]))

D = {
    'R': 1,
    'D': 1j,
    'L': -1,
    'U': -1j,
}

pos = 0
walls = set([pos])
for elem in b:
    d = D[elem[0]]
    for i in range(elem[1]):
        pos += d
        walls.add(pos)

xs = list(map(lambda x: x.real, walls))
ys = list(map(lambda y: y.imag, walls))
BOUNDS_X = (int(min(xs)), int(max(xs)+1))
BOUNDS_Y = (int(min(ys)), int(max(ys)+1))

def pp():
    for y in range(*BOUNDS_Y):
        s = ''
        for x in range(*BOUNDS_X):
            if complex(x, y) in walls:
                s = s + '#'
            else:
                s = s + '.'
        print(s)


def ff(start=complex(BOUNDS_X[0]-1, BOUNDS_Y[0]-1),walls=walls, BOUNDS_X=BOUNDS_X, BOUNDS_Y=BOUNDS_Y):
    to_check = set()
    to_check.add(start)
    visited = set()
    while len(to_check) > 0:
        elem = to_check.pop()
        if elem in visited:
            continue
        visited.add(elem)
        to_add = [elem + d for d in [1, -1, 1j, -1j]]
        to_add = [x for x in to_add if x.real >= BOUNDS_X[0]-1 and x.real <= BOUNDS_X[1]]
        to_add = [x for x in to_add if x.imag >= BOUNDS_Y[0]-1 and x.imag <= BOUNDS_Y[1]]
        to_add = [x for x in to_add if x not in walls ]
        for x in to_add:
            to_check.add(x)
    return visited

        
print((BOUNDS_X[1] - BOUNDS_X[0]+2)*(BOUNDS_Y[1]-BOUNDS_Y[0]+2) - len(ff()))

D = {
    '0': 1,
    '1': 1j,
    '2': -1,
    '3': -1j,
    }

c = [(D[x[5]], int(x[:5], 16)) for x in map(lambda x: x[2], b)]


pos = 0
corners = set([pos])
for elem in c:
    pos = pos + elem[0] * elem[1]
    corners.add(pos)

xs = sorted(set(map(lambda x: int(x.real), corners)))
ys = sorted(set(map(lambda y: int(y.imag), corners)))

tx = [(xs[0]-1, 1)] + [(x,1) for x in xs] + [(xs[i]+1, xs[i+1]-xs[i]-1) for i in range(len(xs)-1)] \
+ [(xs[-1]+1, 1)]
tx.sort()


ty = [(ys[0]-1, 1)] + [(y,1) for y in ys] + [(ys[i]+1, ys[i+1]-ys[i]-1) for i in range(len(ys)-1)] \
+ [(ys[-1]+1, 1)]
ty.sort()

pos = complex(tx.index((0,1)), ty.index((0,1)))
walls = set([pos])
for elem in c:
    dist = elem[1]
    while dist > 0:
        pos += elem[0]
        walls.add(pos)
        if elem[0] in [1, -1]:
            dist -= tx[int(pos.real)][1]
        elif elem[0] in [1j, -1j]:
            dist -= ty[int(pos.imag)][1]
        else:
            raise Exception('UNKNOWN dir: ' + str(elem[0]))
        
txs = list(map(lambda x: x.real, walls))
tys = list(map(lambda y: y.imag, walls))
BOUNDS_X = (int(min(txs)), int(max(txs)+1))
BOUNDS_Y = (int(min(tys)), int(max(tys)+1))

out = ff(start=complex(BOUNDS_X[0]-1, BOUNDS_Y[0]-1),walls=walls, BOUNDS_X=BOUNDS_X, BOUNDS_Y=BOUNDS_Y)

def area(c):
    return tx[int(c.real)][1] * ty[int(c.imag)][1]

area_out = sum(map(area, out))
print(area_out)
print((tx[-1][0] - tx[0][0]+1)*(ty[-1][0] - ty[0][0]+1) - area_out)

