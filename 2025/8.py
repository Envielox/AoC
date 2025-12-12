from aoc import *

inp,sam = l(8)

def parse(l):
   return [tuple(map(int, elem.split(','))) for elem in l]

a = parse(inp)
b = parse(sam)

def dist(a,b):
   return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def dfs(l, e, s, visited):
   if s in visited:
      return visited
   visited.add(s)
   for neigh in e[s]:
      a = dfs(l, e, neigh, visited)
      visited = visited.union(a)
   return visited   

def product(l):
   res = 1
   for i in l:
      res *= i
   return res

def get_dists(l):
   dists = []
   for i, a in enumerate(l):
      for j, b in enumerate(l):
         if j >= i:
            continue
         dists.append((dist(a,b), i, j))
   dists.sort()
   return dists

def solve(l, n):
   dists = get_dists(l)
   circuits = []
   visited = set()
   edges = [set() for i in range(len(l))]
   for d in dists[:n]:
      edges[d[1]].add(d[2])
      edges[d[2]].add(d[1])
   
   for i in range(len(l)):
      if i in visited:
         continue
      res = dfs(l, edges, i, set())
      circuits.append(res)
      visited = visited.union(res)
   lens = list(sorted(map(len,circuits)))
   
   return product(lens[-3:])
         
print(solve(b, 10))
print(solve(a, 1000))

def solve2(l):
   dists = get_dists(l)

   box_to_c = [i for i in range(len(l))]
   c_to_box = {i : set([i]) for i in range(len(l))}

   for e in dists:
      c1 = box_to_c[e[1]]
      c2 = box_to_c[e[2]]
      if c1 == c2:
         continue
      new_c = c_to_box[c1].union(c_to_box[c2])
      
      for elem in c_to_box[c2]:
         box_to_c[elem] = c1
      del c_to_box[c2]
      c_to_box[c1] = new_c

      if len(c_to_box) == 1:
         # solution
         return l[e[1]][0] * l[e[2]][0]
   return -1

print(solve2(b))
print(solve2(a))

def find(l, v):
   if l[v] == v:
      return v
   l[v] = find(l, l[v])
   return l[v]
         
def unio(l, x, y):
   l[find(l,y)] = l[find(l,x)]

def solve3(l):
   dists = get_dists(l)
   box_to_c = [i for i in range(len(l))]
   num_c = 0
   
   for e in dists:
      c1 = find(box_to_c, e[1])
      c2 = find(box_to_c, e[2])
      if c1 == c2:
         continue
      
      unio(box_to_c, e[1], e[2])
      num_c += 1
      
      if num_c == len(l) - 1:
         return l[e[1]][0] * l[e[2]][0]
   return -1

print(solve3(b))
print(solve3(a))

   



