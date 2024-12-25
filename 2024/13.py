input_file="inp13.txt"
sample_file="sample13.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

import re

def get_num(l):
    res = re.match('[^0123456789]*(\d+)[^0123456789]*(\d+)', l)
    return [int(res[1]), int(res[2])]

b = [(get_num(a[i]), get_num(a[i+1]), get_num(a[i+2])) for i in range(0, len(a), 4)]

import numpy

s = 0
s2 = 0

for e in b:
    a1 = [[e[0][0], e[1][0]], [e[0][1], e[1][1]]]
    b2 = e[2]
    res = numpy.linalg.solve(a1,b2)
    #print(res)
    if abs(res[0] - numpy.rint(res[0])) < 0.00001 and res[0] > 0 and res[1] > 0:
        s += int(res[0]* 3 + res[1])
##    for b1 in range(100):
##        for b2 in range(100):
##            if b1 * e[0][0] + b2 * e[1][0] == e[2][0] and b1 * e[0][1] + b2*e[1][1] == e[2][1]:
##                s2 += b1 * 3 + b2
##    print ("{} {}".format(s, s2))
    
print(s)

s = 0

for e in b:
    a1 = [[e[0][0], e[1][0]], [e[0][1], e[1][1]]]
    b2 = [e[2][0] + 10000000000000, e[2][1] + 10000000000000]
    res = numpy.linalg.solve(a1,b2)
    #print(res)
    b1 = numpy.rint(res[0])
    b2 = numpy.rint(res[1])
    if b1 * e[0][0] + b2 * e[1][0] == e[2][0]+10000000000000 and b1 * e[0][1] + b2*e[1][1] == e[2][1]+10000000000000:
        s += int(b1 * 3 + b2)

print(s)


