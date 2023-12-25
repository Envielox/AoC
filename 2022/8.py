with open('8.in') as f:
    a = f.read()

b = a.split('\n')[:-1]

c = [[int(y) for y in x] for x in b]

def get_c(x):
    return c[x[1]][x[0]]

size=99

res = set()
for d in [(0,1), (1, 0), (-1, 0), (0, -1)]:
    for k1 in range(size):
        last_visible =0
        for k2 in range(size):
            # replace 0 with k1, 1/-1 with k2/99-k2
            pos = (k1 if d[0] == 0 else k2 if d[0] == 1 else size-1-k2,
                   k1 if d[1] == 0 else k2 if d[1] == 1 else size-1-k2)
            if pos[0] == 0 or pos[1] == 0 or pos[0] == size-1 or pos[1] == size-1:
                res.add(pos)
                last_visible = get_c(pos)
                continue
            #print("[{}] {} {}".format(d, pos, last_visible))
            if get_c(pos) > last_visible:
                res.add(pos)
                last_visible = get_c(pos)
            if last_visible == 9:
                break
print(len(res))

def get_neighbors(x):
    res = [(x[0]+d[0],x[1]+d[1]) for  d in [(0,1), (1, 0), (-1, 0), (0, -1)]]
    return [x for x in res if x[0] != -1 and x[1] != -1 and x[0] != size and x[1] != size]

def is_zero(x):
    if x[0] == 0 or x[1] == 0 or x[0] == size-1 or x[1] == size-1:
        return True
    return any([ get_c(n) > get_c(x) for n in get_neighbors(x)])

candidates = set([(x,y) for x in range(size) for y in range(size)])
 
def get_scenic_score(spos):
    score = 1
    for d in [(0,1), (1, 0), (-1, 0), (0, -1)]:
        for dist in range(1, size):
            pos = (spos[0] + dist * d[0], spos[1] + dist * d[1])
            #print ("Checking pos {}".format(pos))
            if pos[0] < 0 or pos[1] < 0 or pos[0] > size-1 or pos[1] > size-1:
                score *= dist - 1
                #print("Border, muling {}, score is {}".format(dist - 1, score))
                break
            if get_c(pos) >= get_c(spos):
                score *= dist
                #print("Found higher tree at dist [{}], muling {}, score is {}".format(d, dist, score))
                break
    return score

res = 0        
for x in candidates:
    t = get_scenic_score(x)
    if t > res:
        res = t
print(res)
