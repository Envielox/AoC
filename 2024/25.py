input_file="inp25.txt"
sample_file="sample25.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        fc = f.read()
    elems = fc.split('\n\n')
    return elems[:-1] + [elems[-1][:-1]]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

keys = set()
locks = set()

def parse(l):
    res = []
    for col in range(5):
        row = 0
        while l[row][col] == '#':
            row += 1
        res.append(row-1)
    return tuple(res)

for elem in a:
    s = elem.split('\n')
    if s[0] == '#####':
        locks.add(parse(s))
    elif s[-1] == '#####':
        keys.add(parse(s[::-1]))

def test(a, b):
    s = map(lambda z: z[0] + z[1], zip(a,b))
    return not any([x>5 for x in s])

res = 0
for key in keys:
    for lock in locks:
        if test(key, lock):
            res += 1
print(res)
