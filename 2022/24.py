import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

with open('24.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = [x[1:-1] for x in b[1:-1]]

height = len(c)
width = len(c[0])
m = {}

for y, r in enumerate(c):
    for x, v in enumerate(r):
        m[x + 1j * y] = v

def inmap(p):
    if p.real < 0:
        return False
    if p.real >= width:
        return False
    
    if p.imag < 0:
        return False
    if p.imag >= height:
        return False
    return True
    

def get_neigh(p):
    return [x+p for x in [1, -1, 1j, -1j] if inmap(x+p)]
    
def mod(p):
    return (p.real % width) + 1j * (p.imag % height)

def is_blocked(p, t):
    if p == -1j:
        return False
    if p == width-1+1j*(height):
        return False
    if m[mod(p + t)] == '<':
        return True
    if m[mod(p - t)] == '>':
        return True
    if m[mod(p + 1j*t)] == '^':
        return True
    if m[mod(p - 1j*t)] == 'v':
        return True
    return False

from queue import PriorityQueue
def astar(t = 0, start=-1j, end=(width-1)+1j*(height-1)):
    q = PriorityQueue()
    visited = set()
    q.put((t-start.real - start.imag, t, start.real, start.imag))
    while not q.empty():
        e = q.get()
        if e in visited:
            continue
        visited.add(e)
        p = e[2] + 1j*e[3]
        #print("Elem: {}, len: {}".format(e, q.qsize()))
        if p == end:
            return e
        n = get_neigh(p) + [p]
        unblocked = [x for x in n if not is_blocked(x, e[1] + 1)]
        for u in unblocked:
            q.put((e[1] + 1 - u.real - u.imag, e[1] + 1, u.real, u.imag))

#print(astar()[1] + 1)
#print(astar(242, (width-1)+1j*height, 0)[1] + 1)
print(astar(478, -1j)[1] + 1)


