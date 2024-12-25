input_file="inp19.txt"
sample_file="sample19.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)


towels = a[0].split(', ')
patterns = a[2:]

import functools

@functools.cache
def if_pattern(p):
    if p == "":
        return True

    return any(if_pattern(p[len(x):]) for x in towels if p.startswith(x))

res = 0
for p in patterns:
    if if_pattern(p):
        res += 1

print(res)



@functools.cache
def if_pattern2(p):
    if p == "":
        return 1

    return sum([if_pattern2(p[len(x):]) for x in towels if p.startswith(x)])

res = 0
for p in patterns:
    res += if_pattern2(p)

print(res)
