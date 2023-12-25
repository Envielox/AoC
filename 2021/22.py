with open('22.in') as f:
    a = [x[:-1] for x in f.readlines()]

b = []

for r in a:
    on, rest = r.split()
    xdesc,ydesc,zdesc = rest.split(',')
    x = xdesc[2:].split('..')
    y = ydesc[2:].split('..')
    z = zdesc[2:].split('..')
    t = (on, (int(x[0]), int(x[1])+1), (int(y[0]), int(y[1])+1), (int(z[0]), int(z[1])+1))
    b.append(t)


def mod(state, on, x,y,z):
    for i in range(x[0], x[1]):
        for j in range(y[0], y[1]):
            for k in range(z[0], z[1]):
                state[(i,j,k)] = on
    return state

state = {}
for s in b:
    if s[1][0] > 50 or s[1][0] < -50:
        break
    state = mod(state, *s)

print(len([x for x,v in state.items() if v == 'on']))


xses=set()
yses=set()
zses=set()
for e in b:
    xses.add(e[1][0])
    xses.add(e[1][1])
    yses.add(e[2][0])
    yses.add(e[2][1])
    zses.add(e[3][0])
    zses.add(e[3][1])

xs=list(xses)
xs.sort()
ys=list(yses)
ys.sort()
zs=list(zses)
zs.sort()

# convert
c = []
for e in b:
    n = (e[0],
         (xs.index(e[1][0]), xs.index(e[1][1])), 
         (ys.index(e[2][0]), ys.index(e[2][1])),
         (zs.index(e[3][0]), zs.index(e[3][1])))
    c.append(n)


state = {}
if True:
    for s in c:
        state = mod(state, *s)

def size(node):
    x, y, z = node
    xr = xs[x+1] - xs[x]
    yr = ys[y+1] - ys[y]
    zr = zs[z+1] - zs[z]
    return xr*yr*zr

if True:
    print(sum([size(x) for x,v in state.items() if v == 'on']))

