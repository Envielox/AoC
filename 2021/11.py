with open('11.in') as f:
    a = [x[:-1] for x in f.readlines()]

v = [ [int(x) for x in row] for row in a]

dirs = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def get_neighbors(cx, cy):
    new_dir = [(x + cx,y + cy) for x,y in dirs]
    return [(x,y) for x,y in new_dir if x >= 0 and x < 10 and y >= 0 and y < 10]

def step(b):
    flashing = set()
    flashed = set()
    for y in range(len(b)):
        for x in range(len(b[y])):
            b[y][x] += 1
            if b[y][x] > 9:
                flashing.add((x,y))

    while len(flashing) > 0:
        f = flashing.pop()
        if f in flashed:
            continue
        flashed.add(f)
        for x,y in get_neighbors(*f):
            b[y][x] += 1
            if b[y][x] > 9 and (x,y) not in flashed:
                flashing.add((x,y))

    for x,y in flashed:
        b[y][x] = 0
    return len(flashed)
        
def print_board(b):
    for r in b:
        print(''.join([str(x) for x in r]))

scores = [step(v) for i in range(100)]
print(sum(scores))

num = 100
while True:
    num += 1
    if step(v) == 100:
        print(num)
        break
    if num % 100 == 0:
        print('Still running, step: {}'.format(num))
