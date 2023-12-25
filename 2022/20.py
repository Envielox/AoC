import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

with open('20.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = list(map(int, b))

sample = [1, 2,-3, 3, -2, 0, 4]

def brut2(l):
    key = 811589153
    op = [(x * key, i) for i, x in enumerate(l)]
    for r in range(10):
        print([x[0] for x in op])
        for i in range(len(l)):
            #print(i)
            #print(l)
            scroll = 0
            while op[scroll][1] != i:
                scroll += 1
            op = op[scroll:] + op[:scroll]
            x = op[0][0]
            new_pos = x % (len(l) - 1)
            op = op[1:new_pos+1] + [op[0]] + op[new_pos+1:]
    return [x[0] for x in op]
 
def brut(l):
    op = [(x, False) for x in l]
    moved = 0
    while moved < len(l):
        #print([x[0] for x in op])
        if op[0][1] == True:
            op = op[1:] + [op[0]]
        else:
            x = op[0][0]
            new_pos = x % (len(l) - 1)
            op = op[1:new_pos+1] + [(x, True)] + op[new_pos+1:]
            moved += 1
    return [x[0] for x in op]

def score(l):
    z = l.index(0)
    z1 = (z + 1000)%len(l)
    z2 = (z + 2000)%len(l)
    z3 = (z + 3000)%len(l)
    print("{}: {}, {}: {}, {}: {}".format(z1, l[z1], z2, l[z2], z3, l[z3]))
    return l[z1] + l[z2] + l[z3]
