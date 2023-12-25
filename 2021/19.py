with open('19.in') as f:
    a = [x[:-1] for x in f.readlines()]

r=[]
t=[]
for e in a:
    if e == '':
        r.append(t)
        t=[]
    else:
        if not e.startswith('---'):
            x,y,z = e.split(',')
            t.append((int(x),int(y),int(z)))
r.append(t)
t=[]

dirs = []


def add3(a,b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def sub3(a,b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def dist_sq(x):
    return x[0] ** 2 + x[1] ** 2 + x[2] ** 2

from collections import defaultdict

def get_pairwise_dists(l):
    res = defaultdict(list)
    for i in l:
        for j in l:
            if i == j:
                continue
            dist = dist_sq(sub3(i, j))
            res[dist].append((i, j))
    return res

if True:
    dists = []
    for scan in r:
        dists.append(get_pairwise_dists(scan))

for xpos in [0,1,2]:
    for xsign in ["x", "-x"]:
        for k,v in {"y": "z", "-z": "y", "-y": "-z", "z": "-y"}.items():
            res = ["", "", ""]
            res[xpos] = xsign
            res[(xpos + 1) % 3] = k if xsign == "x" else v
            res[(xpos + 2) % 3] = v if xsign == "x" else k
            dirs.append( (res[0], res[1], res[2]) )

def get_elem(elem, dest):
    if dest.startswith("-"):
        mul = -1
    else:
        mul = 1
    if dest[-1] == "x":
        return mul * elem[0]
    if dest[-1] == "y":
        return mul * elem[1]
    if dest[-1] == "z":
        return mul * elem[2]
    return None

def transform(elem, di):
    return tuple([get_elem(elem, d) for d in di])

def same_with_rot(a,b):
    for d in dirs:
        if a == transform(b, d):
            return d
    return None

def match_with_two_anchors(s1,a1,a12,s2,a2,a22):
    vec1 = sub3(a12, a1)
    vec2 = sub3(a22, a2)
    rot = same_with_rot(vec1, vec2)
    if rot is None:
        return None
    rot_a2 = transform(a2, rot)
    translate = sub3(a1, rot_a2)

    new_s2 = [add3(translate, transform(x, rot)) for x in s2]

    matching = [x for x in new_s2 if x in s1]
    return (matching, rot, translate)


def match_with_anchor(s1, a1, s2, a2):
    for a12 in s1:
        if a12 == a1:
            continue
        dist = sub3(a12, a1)
        if 0 in dist:
            continue
        for a22 in s2:
            if a22 == a2:
                continue
            dist2 = sub3(a22, a2)
            if sum(dist) != sum(dist):
                continue
            if same_with_rot(dist, dist2) is None:
                continue
            r = match_with_two_anchors(s1,a1,a12,s2,a2,a22)
            if r is not None:
                return r

def match(s1, s2):
    for s1_anchor in s1:
        for s2_anchor in s2:
            r = match_with_anchor(s1, s1_anchor, s2, s2_anchor)
            if r is not None:
                return r

def match2(s1, s2): # works with indices not point lists
    pass
    dists_s1 = set(dists[s1].keys())
    dists_s2 = set(dists[s2].keys())
    common_dists = dists_s1.intersection(dists_s2)
    for d in common_dists:
        for (a1, a12) in dists[s1][d]:
            for (a2, a22) in dists[s2][d]:
                res = match_with_two_anchors(r[s1], a1,a12, r[s2], a2, a22)
                if res is not None:
                    return res

unmatched = set(range(len(r)))
matched = set()
paths = {} # New Elem -> (Old elem, rot, translate)

unmatched.remove(0)
matched.add(0)
tried_pair = set()


if True:
    while len(unmatched) != 0:
        trying = unmatched.pop()
        unmatched.add(trying)
        #print("Trying to match scanner #{}".format(trying))
        #print("Matched {} scanners".format(len(matched)))
        for parent in matched:
            if (trying, parent) in tried_pair:
                continue
            tried_pair.add((trying, parent))
            #attempt = match(r[parent], r[trying])
            attempt = match2(parent, trying)
            if attempt is None:
                continue
            if len(attempt[0]) < 12:
                continue
            matched.add(trying)
            unmatched.remove(trying)
            paths[trying] = (parent, attempt[1], attempt[2])
            break

def get_absolute_pos(scanner_id, pos):
    if scanner_id == 0:
        return pos
    (parent, rot, trans) = paths[scanner_id]
    return get_absolute_pos(parent, add3(trans, transform(pos, rot)))

if True:
    all_beacons = set()
    for scan in range(len(r)):
        for x in r[scan]:
            all_beacons.add(get_absolute_pos(scan, x))
    print(len(all_beacons))            

if True:
    def manhattan(x):
        return abs(x[0]) + abs(x[1]) + abs(x[2])
    all_scanners = set()
    for scan in range(len(r)):
        all_scanners.add(get_absolute_pos(scan, (0,0,0)))
    res = []
    for i in all_scanners:
        for j in all_scanners:
            res.append(manhattan(sub3(i, j)))
    print(max(res))


    
    



