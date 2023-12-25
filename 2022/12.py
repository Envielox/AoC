with open('12.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

m = {}

for rn, row in enumerate(b):
    for cn, elem in enumerate(row):
        pos = complex(cn, rn)
        if elem == 'S':
            start = pos
            m[pos] = 0
        elif elem == 'E':
            end = pos
            m[pos] = 25
        else:
            m[pos] = ord(elem) - 97

def g(pos):
    return m.get(pos, 100)

def BFS(start, stop):
    q = [(start, 0)]
    visited = set()
    while len(q) > 0:
        elem, steps = q.pop(0)
        if elem == stop:
            return steps
        if elem in visited:
            continue
        visited.add(elem)
        for n in [+1, -1, +1j, -1j]:
            if g(elem + n) <= g(elem) + 1:
                q.append((elem + n, steps+1))
    return 1e9
        
print(BFS(start, end))

hike = [BFS(x, end) for x in m.keys() if g(x) == 0]

print(min(hike))
