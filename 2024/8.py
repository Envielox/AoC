input_file="inp8.txt"
sample_file="sample8.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

from collections import defaultdict

ant = defaultdict(set)

for y, row in enumerate(a):
    for x, elem in enumerate(row):
        if elem != '.':
            ant[elem].add(x+y*1j)
        
def in_map(a, pos):
    return pos.real >= 0 and pos.real < len(a) and pos.imag >= 0 and pos.imag < len(a[0])

def get_nodes(ants):
    res = set()
    for a1 in ants:
        for a2 in ants:
            if a1 == a2:
                continue
            d = a1 - a2
            res.add(a1+d)
            res.add(a2-d)
    return res

nodes = {k: get_nodes(v) for k,v in ant.items()}

all_nodes = set()
for k,v in nodes.items():
    all_nodes = all_nodes.union(v)
all_nodes_in_map = list(filter(lambda p: in_map(a, p), all_nodes))


##for row in range(len(a)):
##    l = ''
##    for col in range(len(a[0])):
##        p = (col + row*1j)
##        if p in all_nodes_in_map:
##            l += '#'
##        else:
##            l += a[row][col]
##    print(l)

print(len(all_nodes_in_map))

def get_nodes2(ants):
    res = set()
    for a1 in ants:
        for a2 in ants:
            if a1 == a2:
                continue
            d = a1 - a2
            sp = a1
            while (in_map(a, sp)):
                res.add(sp)
                sp += d
            sp = a2
            while (in_map(a, sp)):
                res.add(sp)
                sp -= d
    return res



nodes2 = {k: get_nodes2(v) for k,v in ant.items()}

all_nodes2 = set()
for k,v in nodes2.items():
    all_nodes2 = all_nodes2.union(v)

print(len(all_nodes2))

def print(vals):
    for row in range(len(a)):
        l = ''
        for col in range(len(a[0])):
            p = (col + row*1j)
            if p in vals:
                l += '#'
            else:
                l += a[row][col]
        print(l)
