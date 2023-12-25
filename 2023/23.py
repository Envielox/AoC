with(open('inp23.txt') as f) :
     raw=f.read()

raw2 = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

a = raw[:-1].split('\n')

S = (1, 0)
E = (len(a)-2, len(a[0])-1)

def get(a, p):
    try:
        return a[p[1]][p[0]]
    except IndexError as e:
        print(p)
        raise e
    
def neigh(pos):
    return [(pos[0] + d[0], pos[1] + d[1]) for d in [(1,0), (-1,0), (0,1), (0,-1)]]

def get_neigh(pos):
    return [get(a, p) for p in neigh(pos)]

def is_cross(pos):
    return len([x for x in get_neigh(pos) if x == '#']) < 2

corners = [(x,y) for y in range(1,len(a)-1) for x in range(1,len(a[0])-1) if get(a, (x,y)) != '#' and is_cross((x,y))]

def pp():
    for y in range(len(a)):
        s = []
        for x in range(len(a[0])):
            s.append('X' if (x,y) in corners else get(a,(x,y)))
        print(''.join(s))


def find_end(start, d):
    prev = start
    pos = (start[0] + d[0], start[1] + d[1])
    if get(a, pos) == '#':
        return None
    l = 1
    while pos not in corners and pos != E and pos != S:
        n = [x for x in neigh(pos) if x != prev]
        nps = [x for x in n if get(a,x) != '#']
        if len(nps) == 0:
            print(pos)
        np = nps[0]

        prev = pos
        pos = np
        l += 1
    return -1 if pos == E else -2 if pos == S else corners.index(pos), l

ends = [(find_end(c, (1,0)), find_end(c,(0,1))) for c in corners] 
ends2 = [(find_end(c, (1,0)), find_end(c,(0,1)), find_end(c,(-1,0)), find_end(c,(0,-1))) for c in corners] 

start = find_end(S, (0,1))
        
def DFS():

    to_check = [(start[0], start[1])] # (position, length)
    res = 0
    while len(to_check) > 0:
        (pos, l) = to_check.pop()
        if pos == -1:
            if l > res:
                res = l
            continue
        c = ends[pos]
        if c[0] is not None:
            to_check.append((c[0][0], l + c[0][1]))
        if c[1] is not None:
            to_check.append((c[1][0], l + c[1][1]))

    return res

def DFS2():
    to_check = [(start[0], [], start[1])] # (position, list of visited, length)
    res = 0
    while len(to_check) > 0:
        (pos, visited, l) = to_check.pop()
        if pos in visited:
            continue
        if pos == -2:
            continue
        if pos == -1:
            if l > res:
                res = l
                print(res, pos, visited)
            continue
        c = ends2[pos]
        if c[0] is not None:
            to_check.append((c[0][0], visited + [pos], l + c[0][1]))
        if c[1] is not None:
            to_check.append((c[1][0], visited + [pos], l + c[1][1]))

        if c[2] is not None:
            to_check.append((c[2][0], visited + [pos], l + c[2][1]))
        if c[3] is not None:
            to_check.append((c[3][0], visited + [pos], l + c[3][1]))

    return res



print(DFS())
print(DFS2())

