input_file="inp3.txt"
sample_file="sample3.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read()

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)
#a="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

import re

patterns = re.findall(r'mul\((\d*),(\d*)\)', a)

vals = [ int(x[0],10) * int(x[1],10) for x in patterns]
print(sum(vals))

patterns = re.findall(r"(mul\((\d*),(\d*)\)|do\(\)|don't\(\))", a)

enabled = True
vals = []
for elem in patterns:
    if elem[0] == "do()":
        enabled = True
    elif elem[0] == "don't()":
        enabled = False
    elif enabled:
        vals.append(int(elem[1],10) * int(elem[2],10))

print(sum(vals))
