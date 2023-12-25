with(open('inp3.txt') as f) :
     a=f.read().split('\n')[:-1]

za="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')


def get(p):
    if p[1] < 0 or p[1] >= len(a) or p[0] < 0 or p[0] >= len(a[0]):
        return '.'
    return a[p[1]][p[0]]

def neigh(p):
    return [(p[0]+x, p[1]+y)
        for y in [-1, 0, 1]
        for x in [-1, 0, 1]
        if not (x == 0 and y==0)]
            
def number_neigh(p):
    if get(p) not in '0123456789':
        return set()
    return set(neigh(p)) | number_neigh((p[0]+1, p[1]))

def has_part(s):
    elems = set((get(p) for p in s)) - set('.0123456789')
    return len(elems) > 0

def parse_number(p, v=0, d=0):
    if get(p) not in '0123456789':
        return (v, d)
    dv = int(get(p))
    return parse_number((p[0]+1, p[1]), v=10*v+dv, d=d+1)


res = 0

part_to_number = {}
for y in range(len(a)):
    for x in range(len(a[0])):
        if get((x,y)) == '*':
            part_to_number[(x,y)] = []

for y in range(len(a)):
    try:
        x_iter = iter(range(len(a[0])))
        for x in x_iter:
            nn = number_neigh((x,y))
            if has_part(nn):
                v,d = parse_number((x,y))
                for n in nn:
                    if n in part_to_number:
                        part_to_number[n].append((x,y))
                res += v
                for z in range(d):
                    next(x_iter)
    except StopIteration:
        pass

print(res)


res2=0
for k,v in part_to_number.items():
    if len(v) == 2:
        res2 += parse_number(v[0])[0] * parse_number(v[1])[0]

print(res2)

