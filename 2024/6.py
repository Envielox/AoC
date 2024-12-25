input_file="inp6.txt"
sample_file="sample6.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

obs = set()

for y, row in enumerate(a):
    for x, elem in enumerate(row):
        if elem == '#':
            obs.add(x+y*1j)
        elif elem == '^':
            guard_start = x+y*1j

def in_map(a, pos):
    return pos.real >= 0 and pos.real < len(a) and pos.imag >= 0 and pos.imag < len(a[0])


def step(obs, pos, d):
    if pos + d in obs:
        return (pos, d*1j)
    else:
        return (pos + d, d)

def walk():
    pos = guard_start
    d = -1j
    visited = set()
    while in_map(a, pos):
        visited.add(pos)
        pos, d = step(obs, pos, d)
    return len(visited)


print(walk())

cnt = 0

def is_loop(obs, new_obs, start, s_d):
    pos = start
    d = s_d
    visited = set()
    eff_obs = obs.union(new_obs)
    assert(len(eff_obs) == len(obs) + 1)
    while in_map(a, pos):
        if (pos,d) in visited:
            global cnt
            cnt += 1
            if cnt > 1600:
                print (cnt)
            if cnt > 2000:
                for row in range(len(a)):
                    l = ''
                    for col in range(len(a[0])):
                        p = (col + row*1j)
                        if p in obs:
                            l += '#'
                        elif p in new_obs :
                            l += 'O'
                        elif ((p, 1) in visited or (p, -1) in visited) and ((p, 1j) in visited or (p, -1j) in visited):
                            l += '+'
                        elif (p, 1) in visited or (p, -1)in visited:
                            l += '-'
                        elif ((p, 1j) in visited or (p, -1j) in visited):
                            l += '|'
                        else:
                            l += '.'
                    print(l)
                print()           
            return True
        visited.add((pos, d))
        pos, d = step(eff_obs,pos, d)
    return False

def walk2():
    pos = guard_start
    d = -1j
    visited = set()
    new_obs = set()
    while in_map(a, pos): 
        if in_map(a, pos+d) and pos+d not in obs and pos+d not in new_obs and pos+d not in visited and is_loop(obs, set([pos+d]), pos, d*1j):
            new_obs.add(pos + d)
    
        visited.add(pos)
        pos, d = step(obs, pos, d)
    return new_obs


new_obs = walk2()

print(len(new_obs))

for row in range(len(a)):
    l = ''
    for col in range(len(a[0])):
        p = (col + row*1j)
        if p in obs:
            l += '#'
        elif p in new_obs :
            l += 'O'
        else:
            l += '.'
    print(l)



