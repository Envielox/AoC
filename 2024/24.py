input_file="inp24.txt"
sample_file="sample24.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

vals = {}
for l in a[:a.index('')]:
    z = l.split(': ')
    vals[z[0]] = int(z[1])

gates = {}
var = set()

for l in a[a.index('')+1:]:
    z = l.split(' ')
    var.add(z[0])
    var.add(z[2])
    var.add(z[4])

    gates[z[4]] = (z[1], z[0], z[2], z[4])

def solve(val):
    if val in vals:
        return vals[val]
    g = gates[val]
    v1 = solve(g[1])
    v2 = solve(g[2])
    if g[0] == "AND":
        res = v1 and v2
    elif g[0] == "OR":
        res = v1 or v2
    elif g[0] == "XOR":
        res = v1 ^ v2
    vals[val] = res
    return res

res = [0] * len([1 for x in var if x[0] == 'z'])

for v in var:
    w = solve(v)
    if v[0] == "z":
        idx = int(v[1:], 10)
        res[idx] = w

b = ''.join(map(str, res[::-1]))
print(int(b, 2))

class OP:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return str(self.data) < str(other.data)
    
    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return self.data.__hash__()

    def __repr__(self):
        return self.data.__repr__()

op = {}
for k in var:
    if k[0] in 'xy':
        op[k] = OP(k)
        

carry = { OP(("AND", "x00", "y00")) : "c00", }
for i in range(45):
    x ="x{0:02d}".format(i)
    y ="y{0:02d}".format(i)
    c ="c{0:02d}".format(i-1)
    
    carry[OP(('OR', ('AND', x, y), ('AND', ('XOR', x, y), c)))] = "c{0:02d}".format(i)

swaps = [('vdc', 'z12'), ('nhn', 'z21'), ('tvb', 'khg'), ('gst', 'z33')]

res = ['vdc', 'z12', 'nhn', 'z21', 'tvb', 'khg', 'gst', 'z33']
print(','.join(sorted(res)))

for s in swaps:
    gt = gates[s[0]]
    gates[s[0]] = gates[s[1]]
    gates[s[1]] = gt


def op_solve(val):
    if val in op:
        return op[val]
    g = gates[val]
    v1 = op_solve(g[1])
    v2 = op_solve(g[2])
    if v1 < v2:
        res = (g[0], v1.data, v2.data)
    else:
        res = (g[0], v2.data, v1.data)
    if OP(res) in carry:
        res = carry[OP(res)]
    op[val] = OP(res)
    return OP(res)

for v in var:
    w = op_solve(v)

for i in range(45):
    print(op['z{0:02d}'.format(i)])
    
