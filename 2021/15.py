with open('15.in') as f:
    a = [x[:-1] for x in f.readlines()]

from queue import PriorityQueue

v = [[int(e) for e in row] for row in a]
len_y = len(v)
len_x = len(v[0])
end = (len_x - 1, len_y - 1)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_nei(pos):
    res = []
    for dx, dy in dirs:
        cx = pos[0] + dx
        cy = pos[1] + dy
        if cx >= 0 and cx < len_x and cy >= 0 and cy < len_y:
            res.append((cx, cy))
    return res

def cost(p):
    return p[0]

def heur(p):
    x,y = p[1]
    return (len_x - x) + (len_y - y)


def a_star(v):
    start = (0, (0,0))
    q = PriorityQueue()
    q.put((cost(start) + heur(start), start))
    visited = set()
    while q.qsize() > 0:
        elem = q.get()
        p = elem[1]
        if p[1] in visited:
            continue
        visited.add(p[1])
        if p[1] == end:
            return p[0]
        for x,y in get_nei(p[1]):
            new_p = (p[0] + v[y][x], (x,y))
            q.put((cost(new_p) + heur(start), new_p))
        

print(a_star(v))

def rep_row(row):
    res = []
    for i in range(5):
        new_row = [x + i if x + i < 10 else x + i - 9 for x in row]
        res.extend(new_row)
    return res

def rep_all_rows(m):
    return [rep_row(row) for row in m]

def rep_map(m):
    new_m = rep_all_rows(m)
    res = []
    for i in range(5):
        for row in new_m:
            res.append([x + i if x + i < 10 else x + i - 9 for x in row])
    return res
         
big_map = rep_map(v)
len_x = len_x * 5
len_y = len_y * 5
end = (len_x - 1, len_y - 1)

print(a_star(big_map))






    
