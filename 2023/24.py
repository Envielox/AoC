with(open('inp24.txt') as f) :
     raw=f.read()

raw2 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

a = raw[:-1].split('\n')

b = []
for x in a:
    p,v = x.split(' @ ')
    b.append((tuple(map(int,p.split(', '))), tuple(map(int, v.split(', ')))))

def parallel2(a, b):
    return a[0] * b[1] == a[1] * b[0]

def mul3(a,b):
    s0 = a[1] * b[2] - a[2] * b[1]
    s1 = a[2] * b[0] - a[0] * b[2]
    s2 = a[0] * b[1] - a[1] * b[0]
    return (s0, s1, s2)

def dot3(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def solve_alpha(a, da, b, db):
    # a + da * s = b + db * t, find s
    # t = (ax+dax*s - bx) / dbx
    # ay + day * s = by + dby * (ax+dax*s - bx) / dbx
    # ay * dbx + day * dbx * s = by * dbx + dby * (ax +dax*s - bx)
    # ay * dbx + day * dbx * s = by * dbx + dby * ax + dby * dax * s - dby * bx
    # day * dbx * s - dby * dax * s = -ay * dbx + by * dbx + dby * ax - dby * bx
    # s (day * dbx - dby * dax) = -ay * dbx + by * dbx + dby * ax - dby * bx
    # s = (-ay * dbx + by * dbx + dby * ax - dby * bx) / (day * dbx - dby * dax)
    return (b[1]*db[0] - b[0]*db[1] + a[0]*db[1] - a[1]*db[0]) / (da[1]*db[0] - da[0]*db[1])    


TEST_AREA = (200000000000000, 400000000000000)
#TEST_AREA = (7, 27) # for test data

score = 0
for idx in range(len(b)-1):
    for idx2 in range(idx+1, len(b)):
        if parallel2(b[idx][1], b[idx2][1]):
            #print(idx, idx2, "parallel")
            pass
        else:
            x, dx = b[idx]
            y, dy = b[idx2]
            s = solve_alpha(x, dx, y, dy)
            t = solve_alpha(y, dy, x, dx)
            if s < 0 or t < 0:
                continue
            p = (x[0] + dx[0] * s, x[1] + dx[1] * s)
            if p[0] < TEST_AREA[0] or p[0] > TEST_AREA[1] or p[1] < TEST_AREA[0] or p[1] > TEST_AREA[1]:
                continue
            score += 1
print(score)
            
# from numpy.linalg import solve

# r_i + d_i * @t_i@ = @c_i@
# @r_S@ + @d_S@ * @t_i@ = @c_i@

# r_i + d_i * t_i = r + d * t_i
# r = r_i + d_i * t_i - d * t_i
# r = r_i + t_i (d_i - d)

def add3(a,b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def sub3(a,b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

def mul1(a,x):
    return (a[0] * x, a[1] * x, a[2] * x)

p0 = b[0][0]
v0 = b[0][1]

p1 = sub3(b[1][0],p0)
v1 = sub3(b[1][1],v0)

A = p1
B = (p1[0] + v1[0], p1[1] + v1[1], p1[2] + v1[2])
N = mul3(A, B)



def plane_intersect(N, P0, vec):
    t = dot3(sub3(P0, vec[0]), N) / dot3(vec[1], N)  
    return add3(vec[0], mul1(vec[1], t)), t

I2,T2 = plane_intersect(N, (0,0,0), (sub3(b[2][0], p0), sub3(b[2][1], v0)))

I3,T3 = plane_intersect(N, (0,0,0), (sub3(b[3][0], p0), sub3(b[3][1], v0)))

Rv = tuple(map(lambda x: x/(T3-T2), sub3(I3, I2))) # Direction in the frame of hail_1
Rp = sub3(I2, mul1(Rv, T2)) # Start pos in the frame of hail_1

rock_pos = add3(Rp, p0)
rock_v = add3(Rv, v0)

#print(rock_pos, rock_v)
print(sum(rock_pos))





