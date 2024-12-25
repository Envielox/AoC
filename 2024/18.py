input_file="inp18.txt"
sample_file="sample18.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
size=70+70j
felems=1024
# Comment out to run actual solution
#a = parse_lines(sample_file)
#size=6+6j
#felems=12

b = [complex(*map(int, x.split(','))) for x in a]

from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

def in_map(a, pos):
    return not(pos.real < 0 or pos.imag < 0 or pos.real > size.real or pos.imag > size.imag)

def g(a, pos):
    return in_map(a,pos) and pos not in a

def BFS(a, S, E):
    s = S
    e = E
    pq = PriorityQueue()
    visited = set()
    pq.put(PrioritizedItem(0, S))

    while pq.qsize() > 0:
        t = pq.get()
        score = t.priority
        pos = t.item
        if pos in visited:
            continue
        if pos == e:
            return score
        visited.add(t.item)
        for di in [1, -1, 1j, -1j]:
            if g(a, pos + di):
                pq.put(PrioritizedItem(score + 1, pos+di))
        

print(BFS(b[:felems], 0, size))


r = (0, len(b))
while r[0] +1 != r[1]:
    print(r)
    c = (r[0] + r[1]+1) // 2
    if BFS(b[:c+1], 0, size) is None:
        r = (r[0], c)
    else:
        r = (c, r[1])
print("{},{}".format(int(b[r[1]].real), int(b[r[1]].imag)))

