input_file="inp21.txt"
sample_file="sample21.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)


num_kb = { 'A': 0, '0': -1,
           '3': 1j, '2': -1+1j, '1': -2+1j,
           '6': 2j, '5': -1+2j, '4': -2+2j,
           '9': 3j, '8': -1+3j, '7': -2+3j,
           }

dir_kb = { 'A': 0, 1j: -1,
           1: -1j, -1j: -1j-1, -1: -1j-2
           }

from dataclasses import dataclass, field
from typing import Any

from queue import PriorityQueue

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


import functools

@functools.cache
def find_simple_path(v, Spos, E):
    if v:
        a = dir_kb
    else:
        a = num_kb
    pq = PriorityQueue()
    pq.put(PrioritizedItem(0, (Spos, [])))

    max_res= 10e6
    res_paths = []
    
    while pq.qsize() > 0:
        e = pq.get()
        prio = e.priority
        it = e.item
        if prio > max_res:
            break
        if it[0] == a[E]:
            res_paths.append(e.item[1] + ['A'])
            max_res = prio
        else:
            for d in [1, -1, 1j, -1j]:
                p = it[0] + d
                if p in a.values():
                    pq.put(PrioritizedItem(prio+1, (p, it[1] + [d])))
    return res_paths

@functools.cache
def find_simple_path2(v, Spos, E):
    if v:
        a = dir_kb
    else:
        a = num_kb

    T = a[E]

    d = T - Spos
    dr = 1 if d.real >= 0 else -1
    di = 1j if d.imag >= 0 else -1j

    tr = [dr] * abs(int(d.real))
    ti = [di] * abs(int(d.imag))
    
    if d.real == 0:
        return ti + ['A']
    if d.imag == 0:
        return tr + ['A']

    low_corner = T.real + 1j * Spos.imag
    high_corner = Spos.real + 1j * T.imag

    if d.real < 0:
        if low_corner in a.values():
            return tr + ti + ['A']
        return ti + tr + ['A']
    else:
        if high_corner in a.values():
            return ti + tr + ['A']
        return tr + ti + ['A']

import itertools
import collections

def find_path(v, path):
    if v:
        a = dir_kb
    else:
        a = num_kb
    c_pos = 0
    res = []
    
    for elem in path:
        new_paths = find_simple_path2(v, c_pos, elem)
        res.extend(new_paths)
        c_pos = a[elem]
    
    return res

def flatten(xss):
    return [x for xs in xss for x in xs]

def resolve(c, x):
    w = find_path(False, c)
    for i in range(x-1):
        w = find_path(True, w)
    return len(w)

res = 0
for c in a:
    num = int(c[:-1], 10)
    val = resolve(c, 3)
    print((num, val))
    res += num * val
print(res)
print()

def find_path2(v, path):
    if v:
        a = dir_kb
    else:
        a = num_kb
    c_pos = 0
    res = []
    
    for elem in path:
        new_paths = find_simple_path2(v, c_pos, elem)
        res.append(tuple(new_paths))
        c_pos = a[elem]
    
    return collections.Counter(res)

def resolve2(c, x):
    w = find_path2(False, c)

    for i in range(x):
        new_w = collections.Counter()
        for sub, cnt in w.items():
            new_c = find_path2(True, sub)
            for k in new_c:
                new_c[k] *= cnt
            new_w.update(new_c)
        w = new_w
    return sum(map(lambda k: len(k[0]) * k[1], w.items()))

        

res = 0
for c in a:
    num = int(c[:-1], 10)
    val = resolve2(c, 25)
    print((num, val))
    res += num * val
print(res)
print()






    



            
