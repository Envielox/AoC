with(open('inp17.txt') as f) :
     raw=f.read()

raw2 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

a = raw[:-1].split('\n')

b = [[int(elem) for elem in row] for row in a]

def get(a,pos):
    if pos.real < 0 or pos.real >= len(a[0]) or pos.imag < 0 or pos.imag >= len(a):
        return 10e6
    return a[int(pos.imag)][int(pos.real)] 

from queue import PriorityQueue

TARGET = complex(len(a[0])-1, len(a)-1)

def T(c):
    return (c.real, c.imag)

def UT(c):
    return complex(c[0], c[1])

def astar_d(pos):
    return abs(TARGET - pos)

def dj(delta_spec=(1,4)):
    pq = PriorityQueue()
    pq.put((astar_d(0), 0, T(0), T(1))) # cost, dist, pos, direction we entered from
    pq.put((astar_d(0), 0, T(0), T(1j)))
    visited = set()
    costs = {}
    while not pq.empty():
        _, dist, p, di = pq.get()
        if (p, di) in visited:
            continue
        visited.add((p, di))
        pos = UT(p)
        direction = UT(di)
        #print(dist, pos, direction)
        costs[(pos, direction)]= dist
        if pos == TARGET:
            return dist, costs
        for d in [direction * 1j, direction * -1j]:            
            cost = dist
            for delta in range(1, delta_spec[1]):
                npos = d * delta + pos
                cost += get(b, npos)
                if delta < delta_spec[0]:
                    continue
                pq.put((astar_d(npos) + cost, cost, T(npos), T(d)))
    return -1, costs

def g1(dic, pos):
    res = {}
    for k, v in dic.items():
        if k[0] == pos:
            res[k[1]] = v
    return res

x, y = dj()
print(x)
x2, y2 = dj(delta_spec=(4,11))
print(x2)

        
