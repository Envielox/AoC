with open('13.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = [(b[i], b[i+1]) for i in range(0, len(b), 3)]

d = []
for a,b in c:
    exec('ax = {}'.format(a))
    exec('bx = {}'.format(b))
    d.append((ax,bx))


def cmp(a,b):
    #print("Cmping {} vs {}".format(a,b))
    if isinstance(a,int) and isinstance(b, int):
        return a - b
    if isinstance(a,list) and isinstance(b, list):
        for i in range(max(len(a), len(b))):
            if i >= len(a) and i >= len(b):
                return 0
            if i >= len(a):
                return -1
            if i >= len(b):
                return 1
            z = cmp(a[i] ,b[i])
            if z == 0:
                continue
            return z
        return 0
    if isinstance(a,int) and isinstance(b, list):
        return cmp([a], b)
    if isinstance(a,list) and isinstance(b, int):
        return cmp(a, [b])
    raise Exception("unknown setup {} vs {}".format(a,b))

res = 0
for i,v in enumerate(d):
    x,y = v
    if cmp(x,y) < 0:
        res += i + 1
        #print("Found that {} is matching".format(i))
print(res)


e = []
for x in d:
    e.append(x[0])
    e.append(x[1])

e.append([[2]])
e.append([[6]])

from functools import cmp_to_key

f = sorted(e, key=cmp_to_key(cmp))
print((f.index([[2]]) + 1) * (f.index([[6]]) + 1))
