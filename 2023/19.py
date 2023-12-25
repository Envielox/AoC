with(open('inp19.txt') as f) :
     raw=f.read()

raw2 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

a = raw[:-1].split('\n\n')

parts = []
for elem in a[1].split('\n'):
    v = elem[1:-1].split(',')
    parts.append(tuple([int(x[2:]) for x in v]))

rules = {}
t = {'x':0,'m':1,'a':2,'s':3}
for elem in a[0].split('\n'):
    name, rest = elem[:-1].split('{')
    conds = rest.split(',')
    #print(conds)
    rules[name] = [ (t[e[0]], e[1], int(e[2:e.index(':')]), e[e.index(':')+1:]) for e in conds[:-1]]
    rules[name].append(conds[-1])    

def is_match(r, e):
    if type(r) != tuple:
        return True
    if r[1] == '<':
        return e[r[0]] < r[2]
    elif r[1] == '>':
        return e[r[0]] > r[2]
    else:
        raise Exception("unknown operator")

def find_match(rs, elem):
    for r in rs:
        if is_match(r, elem):
            return r[-1] if type(r) == tuple else r
    raise Exception("No match found " + str(rs) + ' ' + str(elem))

def decide(r, elem, name):
    if name == 'A':
        return True
    elif name == 'R':
        return False
    else:
        #print(name)
        return decide(r, elem, find_match(r[name], elem))

res = 0
for p in parts:
    if decide(rules, p, 'in'):
        res += sum(p)
print(res)


def divide(r, e):
    if r[1] == '<':
        new_dest = list(e)
        new_dest[r[0]] = (e[r[0]][0], r[2])
        rest = list(e)
        rest[r[0]] = (r[2], e[r[0]][1])
        return tuple(new_dest), tuple(rest)
    elif r[1] == '>':
        new_dest = list(e)
        new_dest[r[0]] = (r[2]+1, e[r[0]][1])
        rest = list(e)
        rest[r[0]] = (e[r[0]][0], r[2]+1)
        return tuple(new_dest), tuple(rest)
    else:
        raise Exception("unknown operator")

def divide_cond(rs, e):
    res = {}
    
    for r in rs[:-1]:
        v, e = divide(r, e)
        res[v] = r[3]
    res[e] = rs[-1]
    return res

START = tuple( [(1,4001)] * 4 )


def solve():
    to_consider = {START: 'in'}
    res = []
    while len(to_consider) > 0:
        k = next(iter(to_consider.keys()))
        v=to_consider.pop(k)
        if v == 'A':
            res.append(k)
            #print(v, k, 'A')
            continue
        if v == 'R':
            continue
        
        rr = divide_cond(rules[v], k)
        #print(v, k)
        for k, v in rr.items():
            to_consider[k] = v

    return res
    
def score1(x):
    r = 1
    for z in x:
        if z[1] - z[0] <= 0:
            r = 0
        else:
            r *= (z[1]-z[0])
    return r

def score(x):
    return sum(map(score1,x))

z = solve()

print(score(z))

def find_overlap(a, b):
    z = [ (max(a[i][0],b[i][0]), min(a[i][1],b[i][1])) for i in range(4)] 
    for i in range(4):
        if z[i][0] >= z[i][1]:
            return None
    return z

for e1 in range(len(z)):
    for e2 in range(e1+1, len(z)):
        o = find_overlap(z[e1], z[e2])
        if o:
            print(e1, e2, o)

#for elem in z:
#    print(decide(rules, tuple(map(lambda x: x[0], elem)), 'in'))
#    print(decide(rules, tuple(map(lambda x: x[1]-1,elem)), 'in'))
