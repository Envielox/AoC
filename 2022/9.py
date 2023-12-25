with open('9.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = [(a, int(b)) for a,b in [x.split(' ') for x in b]]

sample = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
bs = sample.split('\n')[:-1]

cs = [(a, int(b)) for a,b in [x.split(' ') for x in bs]]



def d_to_v(x):
    if x == 'U':
        return (0, 1)
    if x == 'D':
        return (0, -1)
    if x == 'L':
        return (-1, 0)
    if x == 'R':
        return (1, 0)
    raise Exception("Unnown value in d_to_v: {}".format(x))


H = (0,0)
T = (0,0)
visited = set([(0,0)])

def step(d):
    global H
    global T
    H = (H[0] + d[0], H[1] + d[1])
    if abs(H[0] - T[0]) >= 2 or abs(H[1] - T[1]) >= 2:
        # fixing T
        dx = 0
        dy = 0
        if H[0] != T[0]:
            dx = (H[0] - T[0]) // abs(H[0] - T[0])
        if H[1] != T[1]:
            dy = (H[1] - T[1]) // abs(H[1] - T[1])
        #print((dx, dy))
        T = (T[0] + dx, T[1] + dy)
        visited.add(T)

def n_steps(d, n):
    for i in range(n):
        step(d_to_v(d))


def do_all(inp):
    for a,b in inp:
        n_steps(a, b)
    return len(visited)


R = [(0,0)] * 10

def long_mini_step(d, i):
    global R
    R[i] = (R[i][0] + d[0], R[i][1] + d[1])
    if i + 1 >= len(R):
        # We just moved end of the rope
        visited.add(R[i])
        return # end of rope
    if abs(R[i][0] - R[i+1][0]) >= 2 or abs(R[i][1] - R[i+1][1]) >= 2:
        # fixing R[i+1]
        dx = 0
        dy = 0
        H = R[i]
        T = R[i+1]
        if H[0] != T[0]:
            dx = (H[0] - T[0]) // abs(H[0] - T[0])
        if H[1] != T[1]:
            dy = (H[1] - T[1]) // abs(H[1] - T[1])
        long_mini_step((dx, dy), i+1)
        
def long_n_steps(d, n):
    for i in range(n):
        long_mini_step(d_to_v(d), 0)

def do_all_long(inp):
    for a,b in inp:
        long_n_steps(a, b)
    return len(visited)
