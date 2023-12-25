with(open('inp2.txt') as f) :
     a=f.read().split('\n')[:-1]

b = [x.split(':')[1].split(';') for x in a]

def parse_run(s):
    r = 0
    b = 0
    g = 0
    el = s.split(',')
    for x in el:
        z = x.strip()
        [v, k] = z.split(' ')
        if k == 'red':
            r += int(v)
        elif k == 'green':
            g += int(v)
        elif k == 'blue':
            b += int(v)
        else:
            raise Exception("unknown color")
    return (r, g, b)

def parse_game(g):
    return [parse_run(x) for x in g]

c = [parse_game(x) for x in b]
            
MAX = (12, 13, 14)

def run_possible(v):
    return v[0] <= MAX[0] and v[1] <= MAX[1] and v[2] <= MAX[2]

def game_possible(g):
    return all([run_possible(r) for r in g])

res = 0


for k, v in enumerate(c):
    if game_possible(v):
        res += k + 1
print(res)


def min_game(ga):
    r = 0
    g = 0
    b = 0
    for run in ga:
        r = max(run[0], r)
        g = max(run[1], g)
        b = max(run[2], b)
    return (r,g,b)

def power(s):
    return s[0] * s[1] * s[2]

print(sum([power(min_game(g)) for g in c]))


    



