from aoc import *
from queue import Queue
from z3 import *

inp,sam = l(10)

def parse_single(l):
   elems = l.split()
   indi = set([i for i,v in enumerate(elems[0][1:-1]) if v == '#'])
   jott = [int(i) for i in elems[-1][1:-1].split(',')]
   wire = [ set([ int(i) for i in el[1:-1].split(',')]) for el in elems[1:-1]]
   return (indi, wire, jott)

def parse(l):
   return [parse_single(x) for x in l]

a = parse(inp)
b = parse(sam)

def xor(a, b):
   r = a.copy()
   for elem in b:
      if elem in a:
         r.remove(elem)
      else:
         r.add(elem)
   return r

def bfs(edge, start, end, func):
   q = Queue()
   q.put((0, start))
   visited = set(tuple(start))

   while not q.empty():
      e = q.get()
      if tuple(e[1]) in visited:
         continue
      visited.add(tuple(e[1]))
      if e[1] == end:
         return e[0]
      for elem in edge:
         new_elem = func(e[1], elem)
         if tuple(new_elem) not in visited:
            q.put( (e[0]+1, new_elem) )
   return -1      

def solve_single(l):
   return bfs(l[1], set(), l[0], xor)

def solve(l):
    return sum(map(solve_single,l))

print(solve(b))
print(solve(a))

def is_solvable(l, result):
   var = [Int('x{}'.format(i)) for i in range(len(l[1]))]
   s = Solver()
   for i in range(len(l[1])):
      s.add(eval("var[{}] >= 0".format(i)))
   for i, elem in enumerate(l[2]):
      st = str(elem) + " == 0"
      for v, wire in enumerate(l[1]):
         if i in wire:
            st += " + var[{}]".format(v)
      s.add(eval(st))
   res = Int('sum')
   s.add(eval('res == ' + '+'.join(map(lambda x : 'var[{}]'.format(x), range(len(var))))))
   s.add(res <= result)
   return s.check() == sat

def bin_find(mi,ma,func):
   if mi == ma:
      return mi
   ele = (mi + ma - 1)//2
   if func(ele):
      return bin_find(mi, ele, func)
   else:
      return bin_find(ele+1, ma, func)

def solve_single2(l):
   cand = bin_find(0, sum(l[2]), lambda x: is_solvable(l, x))
   if is_solvable(l, cand):
      return cand
   return 100000000000000000000000

def solve2(l):
    return sum(map(solve_single2,l))

print(solve2(b))
print(solve2(a))

