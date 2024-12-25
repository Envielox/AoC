input_file="inp4.txt"
sample_file="sample4.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

from collections import defaultdict
v = defaultdict(lambda : '')
for y, row in enumerate(a):
    for x, e in enumerate(row):
        v[x+y*1j] = e

res = 0

for y, row in enumerate(a):
    for x, e in enumerate(row):
        p = x + y * 1j
        for d in [1, -1, 1+1j, 1j,-1+1j, 1-1j,-1j,-1-1j]:
            if v[p] == 'X' and v[p+d] == 'M' and v[p+2*d] == 'A' and v[p+3*d] == 'S':
                res += 1

print(res)

res2 = 0        
for y, row in enumerate(a):
    for x, e in enumerate(row):
        p = x + y * 1j
        if v[p] == 'A' and set([v[p+1+1j], v[p-1-1j]]) == set(['S', 'M']) \
           and set([v[p+1-1j], v[p-1+1j]]) == set(['S', 'M']):
            res2 += 1

print(res2)
