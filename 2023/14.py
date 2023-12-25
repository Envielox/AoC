with(open('inp14.txt') as f) :
     raw=f.read()

raw2 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

a = raw[:-1].split('\n')


def score(r, num):
    s = 0
    for i in range(num):
        s += r - i
    return s

res = 0
store = [0 for x in range(len(a[0]))]
for rx, row in enumerate(a[::-1]):
    #print(store, res)
    for i, e in enumerate(row):
        if e == 'O':
            #print('found O ', rx, res)
            store[i] += 1
        elif e == '#':
            res += score( rx, store[i])
            #print(rx,i,store[i], res)
            store[i] = 0
            

for elem in store:
    res += score(len(a), elem)

print(res)

def points(l):
    T = len(l)
    res = 0
    for r in l:
        for elem in r:
            if elem == 'O':
                res += T
        T -= 1
    return res


def move_n(l):
    res = [ ['.' for x in elem] for elem in l]
    store = [0] * len(l[0])

    rx = len(l)
    for row in l[::-1]:
        rx -= 1
        for i, e in enumerate(row):
            if e == 'O':
                store[i] += 1
            elif e == '#':
                for idx in range(store[i]):
                    res[rx+1+idx][i] = 'O'
                store[i] = 0
                res[rx][i] = '#'

    for i, elem in enumerate(store):
        for idx in range(elem):
            res[rx+idx][i] = 'O'
    
    return res

def move_s(l):
    return move_n(l[::-1])[::-1]

def move_w(l):
    tmp = [ [l[y][x] for y in range(len(l)) ] for x in range(len(l[0]))]
    after = move_n(tmp)
    res = [ [after[y][x] for y in range(len(after)) ] for x in range(len(after[0]))]    
    return res

def move_e(l):
    tmp = [elem[::-1] for elem in l]
    after = move_w(tmp)
    res = [elem[::-1] for elem in after]
    return res

def pp(l):
    for r in l:
        print(''.join(r))
        
print(points(move_n(a)))

def iteration(l):
    t1 = move_n(l)
    t2 = move_w(t1)
    t3 = move_s(t2)
    t4 = move_e(t3)
    return t4

def iteration_n(l, n):
    x = l
    for i in range(n):
        x = iteration(x)
    return x

def join2(l):
    return ''.join([ ''.join([x for x in row]) for row in l])

def ff(l):
    x = l
    step = 0
    visited = {}
    while join2(x) not in visited:
        visited[join2(x)] = step
        step += 1
        x = iteration(x)
    return x, step, visited[join2(x)]

TARGET = 1000000000
elem, sec, first = ff(a)
cycle_len = sec - first

remain = TARGET - first
after_cycle = remain % cycle_len
final = iteration_n(elem, after_cycle)

print(points(final))
