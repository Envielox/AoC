from aoc import *

inp,sam = lb(12)

def parse_shape(l):
   res = set()
   for y, row in enumerate(l[1:]):
      for x, elem in enumerate(row):
         if elem == '#':
            res.add(x + 1j * y)
   return res

def parse_region(l):
   el = l.split(' ')
   s = el[0][:-1].split('x')
   return (int(s[0]) + 1j * int(s[1]), list(map(int, el[1:])))

def parse(l):
   return (list(map(parse_shape, l[:-1])), list(map(parse_region, l[-1][:-1])))

b = parse(sam)
a = parse(inp)

def solve_single(query, shapes):
   size = query[0]
   total = size.real * size.imag
   for i, s in enumerate(shapes):
      total -= query[1][i] * len(s)
   return total >= 0 

def solve(l):
   res = 0
   for elem in l[1]:
      if solve_single(elem, l[0]):
         res += 1
   return res

print(solve(b))
print(solve(a))

