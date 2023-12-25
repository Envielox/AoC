with open('20.in') as f:
    a = [x[:-1] for x in f.readlines()]

key = ["1" if x == "#" else "0" for x in a[0]]
a = a[2:]

life = {}
outside = '0'

for y, row in enumerate(a):
    for x, e in enumerate(row):
        if e == '#':
            life[(x,y)] = "1"
        else:
            life[(x,y)] = "0"

state = (life, outside)

def get_nei(cx,cy):
    res = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            res.append((cx + x, cy + y))
    return res

def get_zone(state):
    to_consider = set()
    for l in state:
        for n in get_nei(*l):
            to_consider.add(n)
    return to_consider

def step(state):
    to_consider = get_zone(state[0])
    
    new_state = {}
    for candidate in to_consider:
        values = [state[0][i] if i in state[0] else state[1] for i in get_nei(*candidate)]
        b = ''.join(values)
        idx = int(b, 2)
        new_state[candidate] = key[idx]

            
        
    if state[1] == '1':
        new_outside = key[511]
    else:
        new_outside = key[0]
    return (new_state, new_outside)

def getc(v):
    if v == "1":
        return "#"
    else:
        return "."
    
def display(mx,ax,my,ay,state):
    for y in range(my, ay):
        for x in range(mx, ax):
            if (x,y) in state[0]:
                print(getc(state[0][(x,y)]), end='')
            else:
                print(getc(state[1]), end='')
        print()
