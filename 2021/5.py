with open('5.in') as f:
    a = [x[:-1] for x in f.readlines()]

from collections import defaultdict

z = [[elem.split(',') for elem in l.split(' -> ')]  for l in a]
def flatten(l):
    return [item for sublist in l for item in sublist]
z = [[int(c) for c in flatten(x)] for x in z]

res = defaultdict(int)

for v in z:
    if v[0] == v[2]:
        d = 1 if v[3] >= v[1] else -1
        for i in range(v[1], v[3] + d, d):
            res[(v[0], i)] += 1
    elif v[1] == v[3]:
        d = 1 if v[2] >= v[0] else -1
        for i in range(v[0], v[2] + d, d):
            res[(i, v[1])] += 1
    else:
        continue # comment out for Part 2
        d = (1 if v[2] >= v[0] else -1, 1 if v[3] >= v[1] else -1)
        pos = (v[0], v[1])
        while True:
            res[pos] += 1
            if pos == (v[2], v[3]):
                break
            pos = (pos[0] + d[0], pos[1] + d[1])

print(len([1 for x in res.values() if x > 1]))
