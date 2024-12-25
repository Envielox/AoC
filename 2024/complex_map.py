input_file="inp2.txt"
sample_file="sample2.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
a = parse_lines(sample_file)


from collections import defaultdict

ant = defaultdict(set)

for y, row in enumerate(a):
    for x, elem in enumerate(row):
        if elem != '.':
            ant[elem].add(x+y*1j)
        
def in_map(a, pos):
    return pos.real >= 0 and pos.real < len(a) and pos.imag >= 0 and pos.imag < len(a[0])

def print(vals):
    for row in range(len(a)):
        l = ''
        for col in range(len(a[0])):
            p = (col + row*1j)
            if p in vals:
                l += '#'
            else:
                l += a[row][col]
        print(l)
