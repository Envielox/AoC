from aoc import *
from collections import defaultdict

inp,sam = l(7)

def parse(l):
    S = l[0].index('S')
    res = []
    for idx,r in enumerate(l[1:]):
        res.append([i for i,v in enumerate(r) if v == '^'])
        
    return(S, res)

a = parse(inp)
b = parse(sam)

def solve(l):
    S, split = l
    beams = set()
    beams.add(S)
    qbeams = {S: 1}
    res = 0

    for s in split:
        new_beam = set()
        new_qbeam = defaultdict(int)
        for b in beams:
            if b in s:
                new_beam.add(b-1)
                new_beam.add(b+1)
                new_qbeam[b-1] += qbeams[b]
                new_qbeam[b+1] += qbeams[b]
                res += 1
            else:
                new_beam.add(b)
                new_qbeam[b] += qbeams[b]
        beams = new_beam
        qbeams = new_qbeam
        
    return res, sum(qbeams.values())

print(solve(b))
print(solve(a))

