input_file="inp16.txt"
sample_file="sample16.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines("sample16b.txt")
#a = parse_lines(sample_file)


def g(a, p):
    return a[int(p.imag)][int(p.real)] != '#'

for y, row in enumerate(a):
    if 'S' in row:
        S = complex(row.index('S'), y)
    if 'E' in row:
        E = complex(row.index('E'), y)

from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

def BFS(a, S, E):
    s = S
    e = E
    d = 1
    pq = PriorityQueue()
    visited = set()
    pq.put(PrioritizedItem(0, (S, d)))

    while pq.qsize() > 0:
        t = pq.get()
        score = t.priority
        pos, di = t.item
        if t.item in visited:
            continue
        if pos == e:
            return score
        visited.add(t.item)
        if g(a, pos + di):
            pq.put(PrioritizedItem(score + 1, (pos+di, di)))
        pq.put(PrioritizedItem(score + 1000, (pos, di * 1j)))
        pq.put(PrioritizedItem(score + 1000, (pos, di * -1j)))

print(BFS(a, S, E))

        

def BFS2(a, S, E):
    s = S
    e = E
    d = 1
    pq = PriorityQueue()
    paths = {(-1,0): (0, set())}
    pq.put(PrioritizedItem(0, (S, d, (-1, 0))))
    best_score = 10e6

    end_di = 0

    while pq.qsize() > 0:
        t = pq.get()
        score = t.priority
        pos, di, prev = t.item
        if score > best_score:
            break
        if (pos,di) in paths:
            if score == paths[(pos, di)][0]:
                paths[(pos,di)][1].update(paths[prev][1])
            continue
        if pos == e:
            end_di = di
            best_score = score
        pp = paths[prev][1].copy()
        pp.add(pos)
        paths[(pos,di)] = (score, pp)

        if g(a, pos + di):
            pq.put(PrioritizedItem(score + 1, (pos+di, di, (pos,di))))
        pq.put(PrioritizedItem(score + 1000, (pos, di * 1j, prev)))
        pq.put(PrioritizedItem(score + 1000, (pos, di * -1j, prev)))

    return len(paths[(E,end_di)][1])
        
print(BFS2(a, S,E))
