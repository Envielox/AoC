with(open('inp16.txt') as f) :
     raw=f.read()

raw2 = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

a = raw[:-1].split('\n')

def get(l, pos):
    return a[int(pos.imag)][int(pos.real)]

def out(pos):
    return pos.real < 0 or pos.real >= len(a[0]) or pos.imag < 0 or pos.imag >= len(a)

def f(posd):
    return [x for x in posd if not out(x[0])]

def n(pos, d, e):
    if e == '.':
        return [(pos+d, d)]
    elif e == '\\':
        nd = d.imag + 1j*d.real
        return [(pos+nd, nd)]
    elif e == '/':
        nd = -1 * d.imag + -1 * 1j * d.real
        return [(pos+nd, nd)]
    elif e == '-':
        if d in [1, -1]:
            return [(pos+d, d)]
        else:
            return [(pos+d*1j, d*1j), (pos+d*-1j, d*-1j)]
    elif e == '|':
        if d in [1j, -1j]:
            return [(pos+d, d)]
        else:
            return [(pos+d*1j, d*1j), (pos+d*-1j, d*-1j)]
    else:
        raise Exception("unknown element: " + e)

def nex(pos, d):
    e = get(a, pos)
    return f(n(pos,d,e))

def pp(se):
    for y in range(len(a)):
        s = ""
        for x in range(len(a[0])):
            if x + 1j*y in se:
                s = s +'#'
            else:
                s = s + get(a, (x+1j*y))
        print(s)
    

def go(start = (0,1)):
    to_visit = set()
    to_visit.add(start)
    visited = set()

    while len(to_visit) > 0:
        x = to_visit.pop()
        if x in visited:
            continue
        visited.add(x)
    
        #print("in: ", x)
        #pp(set([x[0] for x in visited]))

        for elem in nex(*x):
            to_visit.add(elem)
            # print(elem)
    return visited
    
res = set([x[0] for x in go()])

print(len(res))

starts = [(x, 1j) for x in range(len(a))] + \
         [(x+1j*(len(a[0])-1), -1j) for x in range(len(a))] + \
         [(1j*x, 1) for x in range(len(a[0]))] + \
         [((len(a)-1) + 1j*x, -1) for x in range(len(a[0]))]
    

energy = [len(set([x[0] for x in go(pos)])) for pos in starts]
print(max(energy))


