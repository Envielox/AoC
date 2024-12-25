input_file="inp5.txt"
sample_file="sample5.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

rules = [ (int((v := x.split('|'))[0]), int(v[1])) for x in a[:a.index('')] ]
pages = [ [int(v) for v in x.split(',')] for x in a[a.index('')+1:] ]

def validate_pages(p, r):
    for rule in r:
        # print ("{} {} {} {}".format(rule, p, rule[0] in p, rule[1] in p))
        if rule[0] in p and rule[1] in p:
            r0 = p.index(rule[0])
            r1 = p.index(rule[1])
            if r0 > r1:
                return False
    return True


def fix_pages(p, r):
    neigh = {x: [] for x in p}
    #print(neigh)
    for rule in r:
        if rule[0] in p and rule[1] in p:
            neigh[rule[0]].append(rule[1])

    to_be_visited = set(p)
    result = []
    def visit(elem):
        if elem not in to_be_visited:
            return
        #print(neigh)
        #print("visiting {}".format(elem))
        for n in neigh[elem]:
            visit(n)
        result.insert(0, elem)
        if elem in to_be_visited:
            to_be_visited.remove(elem)

    while len(to_be_visited) > 0:
        e = next(iter(to_be_visited))
        #print('NEXT')
        visit(e)

    return result

mid_p = 0
mid_p2 = 0

for p in pages:
    if validate_pages(p, rules):
        v=p[len(p)//2]
        mid_p += v
        #print(v)
    else:
        z = fix_pages(p, rules)
        v=z[len(z)//2]
        mid_p2 += v

print(mid_p)
print(mid_p2)
