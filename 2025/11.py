from aoc import *
from collections import defaultdict
from functools import cache

inp,sam = l(11)


def parse_single(l):
   w = l.split()
   return (w[0][:-1], w[1:])

def parse(l):
   e = list(map(parse_single, l))
   return {k: v for k,v in e}

a = parse(inp)
b = parse(sam)

global g
@cache
def dfs(s, e, forbidden=None, verbose=False):
   if s == e:
      return 1
   global g
   if s not in g:
      return 0
   if s == forbidden:
      return 0
   if verbose:
      print("Visiting: {} {}".format(s,e))
   return sum(map(lambda x: dfs(x, e, forbidden,verbose), g[s]))

def solve(l):
   dfs.cache_clear()
   global g
   g = l
   return dfs('you', 'out')

print(solve(b))
print(solve(a))

def solve2(l):
   dfs.cache_clear()
   global g
   g = l

   a1 = dfs('svr', 'fft', forbidden='dac')
   a2 = dfs('fft', 'dac')
   a3 = dfs('dac', 'out', forbidden='fft')

   b1 = dfs('svr', 'dac', forbidden='fft')
   b2 = dfs('dac', 'fft')
   b3 = dfs('fft', 'out', forbidden='dac')
   return (a1 * a2 * a3) + (b1*b2*b3)

c = parse(parse_lines('sample11b.txt'))

print(solve2(c))
print(solve2(a))
