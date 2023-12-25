with open('13.in') as f:
    a = [x[:-1] for x in f.readlines()]

pos = set()
i = 0
while a[i] != '':
    x,y = a[i].split(',')
    pos.add((int(x), int(y)))
    i += 1

i += 1

def fold_y(pos, dy):
    new_pos = set()
    for x, y in pos:
        if y > dy:
            new_x = x
            new_y = dy - (y - dy)
            new_pos.add((new_x, new_y))
        else:
            new_pos.add((x,y))
    return new_pos

def fold_x(pos, dx):
    new_pos = set()
    for x, y in pos:
        if x > dx:
            new_y = y
            new_x = dx - (x - dx)
            new_pos.add((new_x, new_y))
        else:
            new_pos.add((x,y))
    return new_pos

for idx in range(i, len(a)):
    d, p = a[idx].split('=')
    if d == 'fold along x':
        pos = fold_x(pos, int(p))
    elif d == 'fold along y':
        pos = fold_y(pos, int(p))
    else:
        print("ERROR")



result = [[' ' for x in range(40)] for y in range(6)]
for x,y in pos:
    result[y][x] = '#'

for r in result:
    print(''.join(r))
