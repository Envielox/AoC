input_file="inp20.txt"
sample_file="sample20.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

track = set()

for y, row in enumerate(a):
    for x, elem in enumerate(row):
        if elem == '#':
            continue
        p = x+y*1j
        track.add(p)
        
        if elem == 'S':
            S = p
        if elem == 'E':
            E = p

def BFS():       
    c = -1
    t = 0
    times = {}
    n = set([S])

    while len(n) > 0:
        e = n.pop()
        if e in times:
            continue
        times[e] = t
        t += 1
        for d in [1, -1, 1j, -1j]:
            if (e + d) in track:
                n.add(e+d)
    return times

times = BFS()

cheats = [2, -2, 2j, -2j, 1+1j, 1-1j, -1+1j, -1-1j]

from collections import defaultdict
res = {}
res_2 = defaultdict(int)

for s_pos in times:
    for cheat in cheats:
        e_pos = s_pos + cheat
        if e_pos in times and times[s_pos] < times[e_pos] - 2:
            res[(s_pos, e_pos)] = times[e_pos] - times[s_pos] - 2
            res_2[times[e_pos] - times[s_pos] - 2] += 1

print(sum(v for k,v in res_2.items() if k >= 100))

res = {}
res_2 = defaultdict(int)

##for s_pos in times:
##    for e_pos in times:
##        d = e_pos - s_pos
##        dist = abs(int(d.real)) + abs(int(d.imag))
##        if dist > 20:
##            continue
##
##        if e_pos in times and times[s_pos] < times[e_pos] - dist:
##            res[(s_pos, e_pos)] = times[e_pos] - times[s_pos] - dist
##            res_2[times[e_pos] - times[s_pos] - dist] += 1

cheats = [x+1j*y for x in range(-20, 21) for y in range(-20,21) if abs(x) + abs(y) <= 20]

for s_pos in times:
    for cheat in cheats:
        e_pos = s_pos + cheat
        dist = abs(int(cheat.real)) + abs(int(cheat.imag))

        if e_pos in times and times[s_pos] < times[e_pos] - dist:
            #res[(s_pos, e_pos)] = times[e_pos] - times[s_pos] - dist
            res_2[times[e_pos] - times[s_pos] - dist] += 1


print(sum(v for k,v in res_2.items() if k >= 100))

