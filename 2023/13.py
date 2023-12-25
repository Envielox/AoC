with(open('inp13.txt') as f) :
     raw=f.read()

raw2 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

a = raw[:-1].split('\n\n')
b = [x.split('\n') for x in a]


def get_number(l):
    s = 0
    e = 1
    for i in l:
        if i == '#':
            s += e
        e *= 2
    return s

def parse_layout(l):
    columns = [get_number([r[i] for r in l]) for i in range(len(l[0]))]
    rows = [get_number(r) for r in l]
    return (columns, rows)

c = [parse_layout(l) for l in b]

def is_mirror(l, pos):
    for a,b in zip(l[pos:], l[pos-1::-1]):
        if a != b:
            return False
    return True

def is_smudge(a, b):
    ab = format(a, '020b')
    bb = format(b, '020b')
    diff = sum([1 for x in zip(ab, bb) if x[0] != x[1]])
    return diff == 1


def is_mirror2(l, pos):
    smudge = 0
    for a,b in zip(l[pos:], l[pos-1::-1]):
        if a != b:
            if smudge == 0 and is_smudge(a,b):
                smudge = 1
            else:
                return False
    return True if smudge != 0 else False


def find_mirror(l):
    sum = 0
    for cx in range(1,len(l[0])):
        if is_mirror(l[0], cx):
            sum += cx

    for rx in range(1,len(l[1])):
        if is_mirror(l[1], rx):
            sum += rx * 100
    return sum
    


d = [find_mirror(x) for x in c]

print(sum(d))

def find_mirror2(l):
    sum = 0
    for cx in range(1,len(l[0])):
        if is_mirror2(l[0], cx):
            sum += cx

    for rx in range(1,len(l[1])):
        if is_mirror2(l[1], rx):
            sum += rx * 100
    return sum
    

e = [find_mirror2(x) for x in c]

print(sum(e))


