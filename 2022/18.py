with open('18.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = set([tuple(map(int, x.split(','))) for x in b])

#c = [(1,1,1), (1,1,2)]

def get_sides(x):
    neigh = [
        (1,0,0), (-1, 0, 0),
        (0,1,0), (0, -1, 0),      
        (0,0, 1), (0, 0, -1),
        ]
    res = 6
    for n in neigh:
        t = tuple(map(lambda x: x[0] + x[1], zip(x, n)))
        if t in c:
            #print("{} found substracting".format(t))
            res -= 1
    #print(res)
    return res

print(sum(map(get_sides, c)))

def get_neigh(x):
    neigh = [
        (1,0,0), (-1, 0, 0),
        (0,1,0), (0, -1, 0),      
       (0,0, 1), (0, 0, -1),
    ]
    res = set()
    for n in neigh:
        t = tuple(map(lambda x: x[0] + x[1], zip(x, n)))
        if all(map(lambda x: x >= -1 and x <= 21, t)):
            res.add(t)
    return res

def dfs(p):
    q = [p]
    visited = set()
    while len(q) > 0:
        x = q.pop()
        if x in visited:
            continue
        visited.add(x)
        for n in get_neigh(x):
            if n not in c:
                q.append(n)
    return visited

exterior = dfs((-1, -1, -1))

def get_sides2(x):
    neigh = [
        (1,0,0), (-1, 0, 0),
        (0,1,0), (0, -1, 0),      
        (0,0, 1), (0, 0, -1),
        ]
    res = 0
    for n in neigh:
        t = tuple(map(lambda x: x[0] + x[1], zip(x, n)))
        if t in exterior:
            #print("{} found substracting".format(t))
            res += 1
    #print(res)
    return res

print(sum(map(get_sides2, c)))
