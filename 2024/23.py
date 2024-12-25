input_file="inp23.txt"
sample_file="sample23.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

from collections import defaultdict

b=defaultdict(set)

for x in a:
    w = x.split('-')
    b[w[0]].add(w[1])
    b[w[1]].add(w[0])

res = set()

for k,v in b.items():
    if k[0] != 't':
        continue
    for elem in v:
        for elem2 in v:
            if elem >= elem2:
                continue
            if elem2 in b[elem]:
                res.add(tuple(sorted([k, elem, elem2])))

print(len(res))

def n_1_clique(l):
    res = set()
    for q in l:
        for k, v in b.items():
            if set(q).intersection(v) == set(q):
                z = list(q)
                z.append(k)
                res.add(tuple(sorted(z)))
    return res


# due how data is constructed target clique uses all neighboors of a single vertex except one
# we could have just checked for every vertex if all it's neighboors minus one consist of a clique


all_elems = [k for k in b]
c0 = set([(k,) for k in all_elems])

cliques = [c0]

for i in range(12):
    print(i)
    cliques.append(n_1_clique(cliques[-1]))

for elem in cliques[-1]:
    print(','.join(elem))
