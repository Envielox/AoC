import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

with open('22.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

ins = b[-1].replace('L', ' L ').replace('R', ' R ').split(' ')
ins = [x if i % 2 == 1 else int(x) for i,x in enumerate(ins)]

m = set()
wall = set()

height = len(b) - 1
width = max(map(len, b[:-1]))

for r in range(height):
    for c in range(len(b[r])):
        if b[r][c] == ' ':
            continue
        if b[r][c] == '#':
            wall.add(c + 1j * r)
        m.add(c + 1j * r)

def p():
    for r in range(height):
        for c in range(width):
            p = c + 1j * r
            if p in wall:
                print('#', end='')
            elif p in m:
                print('.', end='')
            else:
                print(' ', end='')
        print()


start = b[0].index('.')

pos = start
face = 1 # facing, versor in the right direction




##    # 0 1
##    # 2 #
##    4 3 #
##    5 # #

##    # 1 2
##    # 3 #
##    5 6 #
##    4 # #

neigh = { # each side neighbors in order up, right, down, left
    1: [4, 2, 3, 5],
    2: [4, 6, 3, 1],
    3: [1, 2, 6, 5],
    4: [5, 6, 2, 1],
    5: [3, 6, 4, 1],
    6: [3, 2, 4, 5],
}

cube_size = 50
cube_pos = {
    1: 1,
    2: 2,
    3: 1+1j,
    4: 3j,
    5: 2j,
    6: 1+2j,
}
pos_to_cube = {v: k for k,v in cube_pos.items()}

face_order = [-1j, 1, 1j, -1] # up, right, down, left

clockwise = [1, 1j, -1, -1j]
to_dist = [
    lambda x: cube_size-1 - x.real,
    lambda x: cube_size-1 - x.imag,
    lambda x: x.real,
    lambda x: x.imag,

    ]

face_base_pos = [0, cube_size-1, (cube_size-1) + 1j*(cube_size-1), 1j * (cube_size-1)]

def cube_wrap(fro, face):
    c_pos = fro.real // cube_size + 1j * (fro.imag // cube_size)
    in_cube_pos = fro.real % cube_size + 1j * (fro.imag % cube_size)
    cube = pos_to_cube[c_pos]
    new_cube = neigh[cube][face_order.index(face)]

    t_dist = to_dist[face_order.index(face)]

    edge_dist = t_dist(in_cube_pos)

    new_cube_edge = neigh[new_cube].index(cube)
    new_edge_pos = clockwise[new_cube_edge] * edge_dist
        
    new_in_cube_pos = face_base_pos[new_cube_edge] + new_edge_pos
    
    new_global_pos = cube_pos[new_cube] * cube_size + new_in_cube_pos
    new_facing = -1 * face_order[new_cube_edge]
    return (new_global_pos, new_facing)


def get_next():
    if pos + face in m:
        return (pos + face, face)
    # We need to wrap it
    return cube_wrap(pos, face)
    r_face = -1 * face
    ret = pos
    while ret + r_face in m:
        ret = ret + r_face
    return ret

def move(x):
    global pos
    global face
    if x == 'R':
        face *= 1j
        return
    if x == 'L':
        face *= -1j
        return
    for i in range(x):
        n, nf = get_next()
        if n not in wall:
            pos = n
            face = nf
        else:
            break


def score():
    z = {1: 0, 1j: 1, -1: 2, -1j: 3}
    return int((pos.imag + 1) * 1000 + (pos.real + 1) * 4 + z[face])

for e in ins:
    move(e)

print(score())
