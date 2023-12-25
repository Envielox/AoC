with open('14.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = [x.split(' -> ') for x in b]

wall = set()

def add_wall(a, b):
    global wall
    xdir = (a.real < b.real) - (b.real < a.real)
    ydir = (a.imag < b.imag) - (b.imag < a.imag)

    if xdir == 0:
        for y in range(int(a.imag), int(b.imag + ydir), int(ydir)):
            wall.add(a.real + y * 1j)

    if ydir == 0:
        for x in range(int(a.real), int(b.real + xdir), int(xdir)):
            wall.add(x + a.imag * 1j)

            
for r in c:
    for i in range(len(r) - 1):
        xa, ya = r[i].split(',')
        xb, yb = r[i+1].split(',')
        add_wall(int(xa) + int(ya) * 1j, int(xb) + int(yb) * 1j)

VOID = max(map(lambda x: x.imag, wall)) + 2


sand = wall.copy()


def p():
    for y in range(10):
        for x in range(494, 504):
            print('#' if x+y*1j in wall else 'O' if x+y*1j in sand else '.', end='')
        print()

def sandfall():
    stream = [500]

    while stream[-1].imag < VOID:
        if stream[-1] + 1j not in sand:
            stream.append(stream[-1] + 1j)
        elif stream[-1] + 1j - 1 not in sand:
            stream.append(stream[-1] + 1j - 1)
        elif stream[-1] + 1j + 1 not in sand:
            stream.append(stream[-1] + 1j + 1)
        else:
            # coming to rest
            sand.add(stream.pop())
    return len(sand) - len(wall)


def sandfall2():
    stream = [500]

    while 500 not in sand:
        if (stream[-1] + 1j).imag >= VOID:
            sand.add(stream.pop())
            continue
        
        if stream[-1] + 1j not in sand:
            stream.append(stream[-1] + 1j)
        elif stream[-1] + 1j - 1 not in sand:
            stream.append(stream[-1] + 1j - 1)
        elif stream[-1] + 1j + 1 not in sand:
            stream.append(stream[-1] + 1j + 1)
        else:
            # coming to rest
            sand.add(stream.pop())
    return len(sand) - len(wall)
