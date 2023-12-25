with open('19.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

import re

pat = re.compile("Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")

c = [tuple(map(int, pat.match(x).groups())) for x in b] 

d = [( (x[0], 0, 0, 0), (x[1], 0, 0, 0), (x[2], x[3], 0, 0), (x[4], 0, x[5], 0)) for x in c]

import math

def pro(bot, res, n):
    return tuple(map(lambda x: x[1] + x[0] * n, zip(bot, res)))

def sub(a, b):
    return tuple(map(lambda x: x[0] - x[1], zip(a, b)))

def new_bot(b, idx):
    return tuple([x + (i == idx) for i,x in enumerate(b)])

def add_bot(s, blue, idx):
    needed = map(lambda x: max(x[0] - x[1], 0), zip(blue[idx], s[2]))
    turns = map(lambda x: 0 if x[1] == 0 else math.ceil(x[0] / x[1]), zip(needed, s[1]))
    turn = max(turns) + 1 
    new_res = pro(s[1], s[2], turn)
    return (s[0] + turn, new_bot(s[1], idx), sub(new_res, blue[idx]))

def max_cost(cost, idx):
    return max([x[idx] for x in cost])

from queue import PriorityQueue

time_limit = 24
time_limit = 32

def add_to(s, bots, res):
    for i in range(res[0]):
        for j in range(res[1]):
            for k in range(res[2]):
                for l in range(res[3]):
                    s.add((bots, (i,j,k,l)))

from collections import defaultdict

def strictly_more(a,b):
    return all(map(lambda x: x[0]>x[1], zip(a,b)))

def reduce(s):
    elems = sorted(s, key=lambda w: sum(map(lambda z: z*z, w)))
    res = set()
    for v in elems:
        add = True
        for r in res:
            if strictly_more(r, v):
                add = False
                break
        if add:
            res.add(v)
    return res

def flat(a):
    return tuple([*a[0], *a[1]])

def unflat(a):
    return ( (a[0], a[1], a[2], a[3]), (a[4], a[5], a[6], a[7]) )

def potential(n, m, b, c):
    total = c
    bots = b
    for i in range(n, m):
        total += bots
        bots += 1
    return total
        
    

def play(blue, time_limit=time_limit, start = (0, (1,0,0,0), (0,0,0,0))):
    state = defaultdict(set)
    state[start[0]].add((start[1], start[2]))
    res = 0
    visited = set()
    for i in range(time_limit):
        print("Size of {} is {}".format(i, len(state[i])))
        ## cleanup state here
        #ss = map(flat, state[i])
        #sss = timeit(reduce, ss)
        #new_state = set(map(unflat, sss))
        #print("Size is {}".format(len(new_state)))

        new_state = state[i]
        
        for v in new_state:
            s = (i, v[0], v[1])
        
            if v in visited:
                continue
            visited.add(v)
            #print(s)
            #print(state)
            if s[0] >= time_limit:
                continue

            if potential(s[0], time_limit, s[1][3], s[2][3]) < res:
                continue # We are worse than the current record holder

            if s[1][3] > 0:
                fin = pro(s[1], s[2], time_limit - s[0])
                if fin[3] > res:
                    print("New high score [{}] from state: {}".format(fin[3], s))
                    res = fin[3]

            if s[0] == time_limit - 1:  # We won't manage to build any new bots anyway
                continue

            # add Geode bot
            if s[1][2] > 0:
                c = add_bot(s, blue, 3)
                if c[0] < s[0] + 6:
                    #print(c)
                    if c[0] <= i:
                        raise Exception ("{} {} !!!!".format(i, c))
                    state[c[0]].add((c[1], c[2]))

            if s[0] == time_limit - 2:  # We won't manage to build any new bots anyway
                continue
            
            # add Obsidian bot
            if s[1][1] > 0 and s[1][2] < max_cost(blue, 2):
                c = add_bot(s, blue, 2)
                if c[0] < s[0] + 6:
                    #print(c)
                    if c[0] <= i:
                        raise Exception ("{} {} {} !!!!".format(i, c,s))
                    state[c[0]].add((c[1], c[2]))

            if s[0] == time_limit - 3:  # We won't manage to build any new bots anyway
                continue
            
            # add Clay bot
            if s[1][1] < max_cost(blue, 1):
                c = add_bot(s, blue, 1)
                #print(c)
                if c[0] <= i:
                    raise Exception ("{} {} !!!!".format(i, c))
                state[c[0]].add((c[1], c[2]))

            if s[0] == time_limit - 4:  # We won't manage to build any new bots anyway
                continue
            
            # add Ore bot
            if s[1][0] < max_cost(blue, 0):
                c = add_bot(s, blue, 0)
                #print(c)
                if c[0] <= i:
                    raise Exception ("{} {} !!!!".format(i, c))
                state[c[0]].add((c[1], c[2]))
            
    return res       

##idx = 1
##result = 0 
##for x in d:
##    res = play(x)
##    print(res)
##    result += res * idx
##    idx += 1
##print(result)

def solve2():
    x = []
    x.append(play(d[0]))
    x.append(play(d[1]))
    x.append(play(d[2]))
    print(x[0] * x[1] * x[2])
#print(29 * 23 * 16)
print(timeit(solve2))


