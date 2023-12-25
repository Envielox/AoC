with open('15.in') as f:
          a = f.read()
LIMIT = 20
LIMIT = int(4e6)

b = a.split('\n')[:-1]

import re

pat = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

c = [pat.match(x).groups() for x in b]

d = [(int(x[0]) + 1j * int(x[1]), int(x[2]) + 1j * int(x[3])) for x in c]

beacons = set([x[1] for x in d])

def query(row):
    ranges = []
    for elem in d:
        z = elem[0] - elem[1]
        dist = abs(z.real) + abs(z.imag)
        radius = dist - abs(row - elem[0].imag)
        if radius <= 0:
            continue
        s = elem[0].real - radius
        ranges.append((s, radius * 2 + 1))
        #print("Elem {}, adding {}".format(elem, ranges[-1]))
    ranges.sort()
    eoc = -1e9 # first not covered
    res = 0
    for s,di in ranges:
        if s > eoc:
            res += di
        else:
            res += max(s + di - eoc,0)
        for b in beacons:
            if b.imag == row:
                if b.real >= s and b.real >= eoc and b.real < s+di:
                    res -= 1
        eoc = max(eoc, s+di)
        #print((res, eoc))
    return res

## 10 ..111112222222222223333######..
#           _
# 5 + 12 + 4 + 7?


def query2(row):
    ranges = []
    for elem in d:
        z = elem[0] - elem[1]
        dist = abs(z.real) + abs(z.imag)
        radius = dist - abs(row - elem[0].imag)
        if radius <= 0:
            continue
        s = elem[0].real - radius
        ranges.append((s, radius * 2 + 1))
        #print("Elem {}, adding {}".format(elem, ranges[-1]))
    ranges.sort()
    eoc = 0 # first not covered
    res = 0
    for s,di in ranges:
        eoc_factor = min(s - eoc,0)
        if s > eoc:
            print('hole found at: {} {}'.format(s - 1, row))
            print('VAL: {}'.format(int(s-1)*4000000 + row))
        if s + di < LIMIT:
            limit_factor = 0
        else:
            limit_factor = s + di -LIMIT
        res += di + eoc_factor - limit_factor

        eoc = max(eoc, s+di)
        if eoc >= LIMIT:
            break
        #rint((res, eoc))
    return res
