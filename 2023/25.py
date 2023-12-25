with(open('inp25.txt') as f) :
     raw=f.read()

raw2 = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

a = raw[:-1].split('\n')

from collections import defaultdict
b = defaultdict(list)

wires = []
elems = set()

for e in a:
    z, x = e.split(': ')
    for o in x.split(' '):
        b[z].append(o)
        b[o].append(z)
        elems.add(z)
        elems.add(o)
        wires.append((z,o))
nodes = list(elems)

def DFS(m, s):
    to_check = [s]
    visited = set()
    while len(to_check) > 0:
        e = to_check.pop()
        if e in visited:
            continue
        visited.add(e)
        for elem in m[e]:
            to_check.append(elem)
    return len(visited)

def DFS_with_removed(m, elems):
    cm = {k: v[:] for k, v in m.items()}
    for a,b in elems:
        cm[a].remove(b)
        cm[b].remove(a)
    return DFS(cm, next(iter(cm.keys())))

full_size = DFS_with_removed(b, [])

##for w1 in range(len(wires)-2):
##    print(w1)
##    for w2 in range(w1+1, len(wires)-1):
##        print(w1, w2)
##        for w3 in range(w2+1, len(wires)):
##            s = DFS_with_removed(b, [wires[w1], wires[w2], wires[w3]])
##            if s != full_size:
##                print(s, full_size-s, s*(full_size-s))
##                break

def BFS(m, s, t):
    to_check = [[s]]
    visited = set()
    while len(to_check) > 0:
        e = to_check.pop(0)
        if e[-1] in visited:
            continue
        visited.add(e[-1])
        if e[-1] == t:
            return e
        for elem in m[e[-1]]:
            if elem not in e:
                to_check.append(e + [elem])
    return None

def num_paths(m, s, t):
    paths = 0
    cm = {k: v[:] for k, v in m.items()}

    while True:
        p = BFS(cm, s, t)
        #print(p)
        if p is None:
            return paths
        paths += 1
        for i in range(len(p)-1):
            cm[p[i]].remove(p[i+1])
            cm[p[i+1]].remove(p[i])


paths = []
for i in range(1, len(nodes)):
    print(i)
    #if (nodes[0], nodes[i]) in wires or (nodes[1], nodes[0]) in wires:
    #    continue
    paths.append(num_paths(b, nodes[0], nodes[i]))
    
l3 = len([x for x in paths if x == 3])
l4 = len([x for x in paths if x > 3]) + 1
print(l3, l4, l3*l4)

    

