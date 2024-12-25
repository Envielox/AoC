input_file="inp7.txt"
sample_file="sample7.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

b = [list(map(int, l.replace(':', '').split(' '))) for l in a]


def can_be_true(res, val, l):
    if len(l) == 0:
        return res == val
    return can_be_true(res, val + l[0], l[1:]) + can_be_true(res, val * l[0], l[1:])

print(sum(map(lambda l: l[0] if can_be_true(l[0], l[1], l[2:]) else 0, b)))

def conc(a, b):
    return int(str(a) + str(b))

def can_be_true2(res, val, l):
    if len(l) == 0:
        return res == val
    return can_be_true2(res, val + l[0], l[1:]) + \
           can_be_true2(res, val * l[0], l[1:]) + \
           can_be_true2(res, conc(val, l[0]), l[1:])

print(sum(map(lambda l: l[0] if can_be_true2(l[0], l[1], l[2:]) else 0, b)))
