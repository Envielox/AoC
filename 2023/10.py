with(open('inp10.txt') as f) :
     raw=f.read()

raw2 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

raw3 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

raw4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

raw5 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

a = raw[:-1].split('\n')

def get(m, pos):
    if pos.real < 0 or pos.real >= len(a[0]) or pos.imag < 0 or pos.imag >= len(a):
        return '.'
    return a[int(pos.imag)][int(pos.real)]

for y in range(len(a)):
    for x in range(len(a[0])):
        if get(a, complex(x,y)) == 'S':
            S_POS = complex(x,y)
            break


connections = {
    '.': [],
    '|': [1j, -1j],
    '-': [ 1, -1],
    'L': [ 1, -1j],
    'J': [-1, -1j],
    '7': [-1,  1j],
    'F': [ 1,  1j],
}

def next_pipe(fr, now):
    dir1 = fr - now
    cur_el = get(a, now)
    dirs = connections[cur_el]
    if dir1 not in dirs:
        return None # Currnet not connected to `fr`
    other_dir = dirs[0] if dirs[1] == dir1 else dirs[1]
    return now + other_dir

def collect_pipe(start, di):
    pipe = [start]
    current = start + di
    while get(a, current) != 'S':
        nex = next_pipe(pipe[-1], current)
        if nex is None:
            return (pipe, False)
        pipe.append(current)
        current = nex
    return (pipe, True)
    
def count1():
    res = collect_pipe(S_POS, -1)
    if (res[1] == False):
        res = collect_pipe(S_POS, 1)
    if (res[1] == False):
        res = collect_pipe(S_POS, 1j)
    if (res[1] == False):
        return "Still false after 3 attempts"
    return len(res[0]) / 2
    
print(count1())

def border():
    res = collect_pipe(S_POS, -1)
    if (res[1] == False):
        res = collect_pipe(S_POS, 1)
    if (res[1] == False):
        res = collect_pipe(S_POS, 1j)
    if (res[1] == False):
        return "Still false after 3 attempts"
    return res[0]

LOOP_BORDER = border()

s_dirs = [LOOP_BORDER[1] - LOOP_BORDER[0], LOOP_BORDER[-1] - LOOP_BORDER[0]]
for k, v in connections.items():
    if set(s_dirs) == set(v):
        # update S to pipe
        row = a[int(S_POS.imag)]
        new_row = row[:int(S_POS.real)] + k + row[int(S_POS.real)+1:]
        a[int(S_POS.imag)] = new_row
        break


def get2(p):
    orig =  complex(p.real//3, p.imag//3)
    local = complex(p.real%3, p.imag%3)
    if orig not in LOOP_BORDER:
        return '.'
    if local == 1+1j:
        return 'x'
    if local - (1+1j) in connections[get(a,orig)]:
        return 'x'
    return '.'


def flood_fill(start):
    to_visit = set([start])
    visited = set()
    while len(to_visit) > 0:
        pos = to_visit.pop()
        if pos in visited:
            continue
        if get2(pos) == 'x':
            continue
        if pos.real < -1 or pos.real > len(a[0])*3 or pos.imag < -1 or pos.imag > len(a)*3:
            continue
        visited.add(pos)
        for p in [pos + 1, pos -1, pos +1j, pos -1j]:
            if p not in visited:
                to_visit.add(p)

    return visited

OUT = flood_fill(0)

def print_new():
    for y in range(len(a)*3):
        l = []
        for x in range(len(a[0]) * 3):
            if complex(x,y) in OUT:
                l.append('O')
            else:
                l.append(get2(complex(x, y)))
        print(''.join(l))
    
INSIDE = 0
for y in range(len(a)):
    for x in range(len(a[0])):
        pos = complex(x, y)
        if pos in LOOP_BORDER:
            continue
        big = pos*3
        outs = [1 for dy in range(3) for dx in range(3) if (big + dx + 1j*dy) in OUT]
        if len(outs) == 0:
            INSIDE += 1
print(INSIDE)
                


# print((len(a)+2)*(len(a[0])+2) - len(LOOP_BORDER) - len(OUT))

    
