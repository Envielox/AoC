input_file="inp22.txt"
sample_file="sample22.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

b = list(map(int, a))

def gen(seed):
    x = seed
    while True:
        x = (x^(x*64)) % 16777216

        x = (x^(x//32)) % 16777216

        x = (x^(x*2048)) % 16777216
        yield x


def get_n(seed, n):
    g = gen(seed)
    for i in range(n-1):
        next(g)
    return next(g)

#print(sum(map(lambda x: get_n(x, 2000), b)))

def get_2(seed):
    g = gen(seed)
    return [seed%10] + [next(g) % 10 for i in range(2000)]

from collections import defaultdict

def get_diffs(vals):
    res = {}
    for i in range(4, len(vals)):
        k = (vals[i-3]-vals[i-4], vals[i-2]-vals[i-3], vals[i-1]-vals[i-2], vals[i] - vals[i-1])
        if k not in res:
            res[k] = vals[i]
    return res

total_diffs = {(-2, 1, -1, 3): 0}
for elem in b:
    x = get_2(elem)
    d = get_diffs(x)
    for k,v in d.items():
        if k in total_diffs:
            total_diffs[k] += v
        else:
            total_diffs[k] = v
            
print(max(total_diffs.values()))
