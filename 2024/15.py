input_file="inp15.txt"
sample_file="sample15.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)
#a = parse_lines("sample15b.txt")

def parse_map(l):
    wall = set()
    box = set()
    robot = 0
    for y, row in enumerate(a):
        for x, elem in enumerate(row):
            if elem == '#':
                wall.add(x+y*1j)
            elif elem == 'O':
                box.add(x+y*1j)
            elif elem == '@':
                robot = x+y*1j
    return (robot, box, wall)

def parse_dir(l):
    d = {'<': -1, '>': 1, 'v': 1j, '^': -1j}
    return [d[x] for x in ''.join(l)]

m = parse_map(a[:a.index('')])
d = parse_dir(a[a.index('')+1:])

def print_m(m):
    for row in range(a.index('')):
        l = ''
        for col in range(len(a[0])):
            p = (col + row*1j)
            if p == m[0]:
                l += '@'
            elif p in m[1]:
                l += 'O'
            elif p in m[2]:
                l += '#'
            else:
                l += '.'
        print(l)

def try_move(m, d):
    new_robot = m[0] + d
    new_box = m[1].copy()

    if new_robot in m[2]:
        return m
    if new_robot not in m[1]: # next spot is free
        return (new_robot, m[1], m[2])
    
    # we push some boxes
    fb = new_robot
    b=fb
    while b in m[1]:
        b += d
    # b is first pos after stack of boxes    
    if b in m[2]:
        return m
    box = m[1].copy()
    box.remove(fb)
    box.add(b)
    return (new_robot, box, m[2])
    
nm = (m[0], m[1].copy(), m[2].copy())
for e in d:
    nm = try_move(nm, e)
    #print("move {}".format(e))
    #print_m(nm)
    

print_m(nm)

def gps(x):
    return int(x.imag * 100 + x.real)

print(sum(map(gps, nm[1])))
##############################

def parse_map2(l):
    wall = set()
    box = set()
    robot = 0
    for y, row in enumerate(l):
        for x, elem in enumerate(row):
            #print('bbe {} {} {}'.format(y, x, elem))
            if elem == '#':
                wall.add((2*x)+y*1j)
                wall.add((2*x+1)+y*1j)
            elif elem == 'O':
                box.add((2*x)+y*1j)
            elif elem == '@':
                robot = (2*x)+y*1j
    return (robot, box, wall)

m2 = parse_map2(a[:a.index('')])

def print_m2(m):
    l = ''
    for row in range(a.index('')):
        for col in range(len(a[0])*2):
            p = (col + row*1j)
            if p == m[0]:
                l += '@'
            elif p in m[1]:
                l += '['
            elif (p-1) in m[1]:
                l += ']'
            elif p in m[2]:
                l += '#'
            else:
                l += '.'
        l += '\n'
    print(l)

def pos_is_box(m,p):
    return p in m[1] or p-1 in m[1]

def box_from_pos(m, p):
    res = []
    if p in m[1]:
        res.append(p)
    if p-1 in m[1]:
        res.append(p-1)
    return res

def try_move2(m, d, v=0):
    new_robot = m[0] + d
    new_box = m[1].copy()

    if new_robot in m[2]:
        return m

    if not pos_is_box(m, new_robot): # next spot is free
        return (new_robot, m[1], m[2])
    # we push some boxes
    next_push = set(box_from_pos(m, new_robot))

    pushing = set()
    while len(next_push) > 0:
        b = next_push.pop()
        if v:
            print(b)
        pushing.add(b)
        if b+d in m[2] or b+1+d in m[2]:
            return m # we would push on wall somewhere, abort

        new_boxes = box_from_pos(m, b+d) + box_from_pos(m, b+1+d)
        for x in new_boxes:
            if x != b:
            #if x not in pushing:
                next_push.add(x)

    box = m[1].copy()
    for e in pushing:
        box.remove(e)
    for e in pushing:
        box.add(e+d)
    return (new_robot, box, m[2])

        

nm2 = (m2[0], m2[1].copy(), m2[2].copy())
for i, e in enumerate(d):
    nm2 = try_move2(nm2, e)
    di = {-1: '<', 1:'>', 1j:'v', -1j: '^'}
    #print("move {} {}".format(i, di[e]))
    #print_m2(nm2)

print_m2(nm2)

print(sum(map(gps, nm2[1])))

