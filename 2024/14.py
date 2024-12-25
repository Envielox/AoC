input_file="inp14.txt"
sample_file="sample14.txt"

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
size = 101+103j
# Comment out to run actual solution
#a = parse_lines(sample_file)
#size = 11+7j


import re

b = []

for x in a:
    r = re.fullmatch(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', x)
    b.append((int(r[1])+1j*int(r[2]), int(r[3]) + 1j*int(r[4])))

def mod(a,b):
    return (a.real % b.real) + 1j * (a.imag % b.imag)

def steps(m, s):
    return [mod(x[0] + x[1] * s, size) for x in m]

c = steps(b, 100)

q1 = [x for x in c if x.real < size.real//2 and x.imag < size.imag//2]
q2 = [x for x in c if x.real > size.real//2 and x.imag < size.imag//2]
q3 = [x for x in c if x.real < size.real//2 and x.imag > size.imag//2]
q4 = [x for x in c if x.real > size.real//2 and x.imag > size.imag//2]

import numpy as np

print(np.prod([len(q1),len(q2),len(q3),len(q4)]))

from collections import Counter

def p(m):
    c = Counter(m)
    s = ''
    for y in range(int(size.imag)):
        for x in range(int(size.real)):
            pos=x+1j*y
            if pos in c:
                s += str(c[pos])
            else:
                s += '.'
        s += '\n'
    print(s)
  
#for s in range(6780, 10000):
#    print(s)
#    p(steps(b, s))

#for s in range(6881, 10000, 101):
#    print(s)
#    p(steps(b, s))

# 6780 - tall
# 6774 - wide
# 6881 - tall
