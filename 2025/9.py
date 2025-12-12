from aoc import *

inp,sam = l(9)

def parse(l):
   return [tuple(map(int, r.split(','))) for r in l]

a = parse(inp)
b = parse(sam)

def solve(l):
   r = 0
   for e1 in l:
      for e2 in l:
         r = max(r, (1+abs(e1[0]-e2[0])) * (1+abs(e1[1]-e2[1])))
   return r

print(solve(b))
print(solve(a))

def add(a,b):
   return ( a[0] + b[0], a[1] + b[1] )

def is_in(elem, v_edges, h_edges):
   for h in h_edges:
      if elem[1] == h[0] and elem[0] >= h[1] and elem[0] <= h[2]:
         return True

   for v in v_edges:
      if elem[0] == v[0] and elem[1] >= v[1] and elem[1] <= v[2]:
         return True

   left_edges = [x for x in v_edges if x[0] < elem[1] and elem[0] > x[1] and elem[1] < x[2]]
   return (len(left_edges) % 2) == 1

def is_h_intersect(minx,maxx,miny,maxy, h_edges):
   for e in h_edges:
      if e[0] > miny and e[0] < maxy:
         if e[1] >= maxx or e[2] <= minx:
            continue
         return True
   return False

def is_v_intersect(minx,maxx,miny,maxy, v_edges):
   for e in v_edges:
      if e[0] > minx and e[0] < maxx:
         if e[1] >= maxy or e[2] <= miny:
            continue
         return True
   return False


def get_edges(l):
   h_edges = []
   v_edges = []

   for i in range(len(l)):
      v1 = l[i]
      v2 = l[(i+1) % len(l)]
      if v1[0] == v2[0]:
         v_edges.append( (v1[0], min(v1[1], v2[1]), max(v1[1], v2[1])) )
      else:
         h_edges.append( (v1[1], min(v1[0], v2[0]), max(v1[0], v2[0])) )

   h_edges.sort()
   v_edges.sort()
   return h_edges, v_edges

def solve2(l):
   h_edges, v_edges = get_edges(l)

   r = 0
   max_pt = 0
   max_pt2 = 0
   for i, e1 in enumerate(l):
      for e2 in l[i+1:]:
         if not is_in((e1[0], e2[1]), v_edges, h_edges):
            continue
         
         if not is_in((e2[0], e1[1]), v_edges, h_edges):
            continue

         minx = min(e1[0], e2[0])
         maxx = max(e1[0], e2[0])
         miny = min(e1[1], e2[1])
         maxy = max(e1[1], e2[1])
         
         if is_h_intersect(minx,maxx,miny,maxy, h_edges):
            continue

         if is_v_intersect(minx,maxx,miny,maxy, v_edges):
            continue
                  
         cand = (1+abs(e1[0]-e2[0])) * (1+abs(e1[1]-e2[1]))
         if cand > r:
            r = cand
            max_pt = e1
            max_pt2 = e2
   print(max_pt)
   print(max_pt2)
   return r        

print(solve2(b))
print(solve2(a))

# By visual check (desmos) those will be part of the solution
# 94582, 48596 -> check with all y < than it
# 94582, 50174 -> check with all y > than it

def solve3(l):
   tc1 = (94582, 48596)
   tc2 = (94582, 50174)

   # tricky bits for my data set
   bad_xs = [6957, 6125, 4778, 2160, 3106, 2869]
   
   r = 0
   max_pt = -1
   for e in l:
      if e[1] > tc1[1]:
         continue
      if e[1] < 33454:
         continue
      if e[0] in bad_xs:
         continue
      cand = (1+abs(e[0]-tc1[0])) * (1+abs(e[1]-tc1[1]))
      if cand > r:
         r = cand
         max_pt = e

   for e in l:
      if e[1] < tc2[1]:
         continue
      if e[1] > 69047:
         continue
      if e[0] in bad_xs:
         continue
      cand = (1+abs(e[0]-tc2[0])) * (1+abs(e[1]-tc2[1]))
      if cand > r:
         r = cand
         max_pt = e
   print(max_pt)
   return r


print(solve3(a))

   
   
