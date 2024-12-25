input_file="inp10.txt"
sample_file="sample10.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

from collections import defaultdict

h = defaultdict(set)

for y, row in enumerate(a):
    for x, elem in enumerate(row):
        h[int(elem)].add(x+y*1j)
        
def in_map(a, pos):
    return pos.real >= 0 and pos.real < len(a) and pos.imag >= 0 and pos.imag < len(a[0])

def print_q(vals):
    for row in range(len(a)):
        l = ''
        for col in range(len(a[0])):
            p = (col + row*1j)
            if p in vals:
                l += '#'
            else:
                l += a[row][col]
        print(l)
scores = {}

for elem in h[9]:
    scores[elem] = set([elem])

for height in range(8, -1, -1):
    for elem in h[height]:
        s = set()
        for d in [1, -1, 1j, -1j]:
            if (d + elem) in h[height+1]:
                s.update(scores[d+elem])
        scores[elem] = s

print(sum([len(scores.get(x, set())) for x in h[0]]))
    
scores = {}

for elem in h[9]:
    scores[elem] = 1

for height in range(8, -1, -1):
    for elem in h[height]:
        s = 0
        for d in [1, -1, 1j, -1j]:
            if (d + elem) in h[height+1]:
                s += scores[d+elem]
        scores[elem] = s

print(sum([scores.get(x, 0) for x in h[0]]))
    



    
