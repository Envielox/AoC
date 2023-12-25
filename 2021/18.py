with open('18.in') as f:
    a = [x[:-1] for x in f.readlines()]

import copy
import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")


x = [eval(i) for i in a]

x2=[[1,1],
[2,2],
[3,3],
[4,4],
[5,5],
[6,6]]

def add_to_leftmost(p, v):
    if type(p[0]) == int:
        p[0] += v
        return
    else:
        add_to_leftmost(p[0], v)

        
def add_to_rightmost(p, v):
    if type(p[1]) == int:
        p[1] += v
        return
    else:
        add_to_rightmost(p[1], v)
        

def explode_helper(p, lvl):
    if type(p[0]) is int and type(p[1]) is int:
        if lvl >= 4:
            return "EXPLODE_ME"
        return None
    if type(p[0]) is list:
        ret = explode_helper(p[0], lvl+1)
        if ret == "EXPLODE_ME":
            if type(p[1]) is int:
                p[1] += p[0][1]
            else:
                add_to_leftmost(p[1], p[0][1])
            go_left = p[0][0]
            p[0] = 0
            return ("L", go_left)
        if type(ret) == tuple:
            if ret[0] == "L":
                return ret
            elif ret[0] == "R":
                if type(p[1]) is int:
                    p[1] += ret[1]
                else:
                    add_to_leftmost(p[1], ret[1])
                return ("D", 0)
            elif ret[0] == "D":
                return ("D", 0)
    if type(p[1]) is list:
        ret = explode_helper(p[1], lvl+1)
        if ret == "EXPLODE_ME":
            if type(p[0]) is int:
                p[0] += p[1][0]
            else:
                add_to_rightmost(p[0], p[1][0])
            go_right = p[1][1]
            p[1] = 0
            return ("R", go_right)
        if type(ret) == tuple:
            if ret[0] == "R":
                return ret
            elif ret[0] == "L":
                if type(p[0]) is int:
                    p[0] += ret[1]
                else:
                    add_to_rightmost(p[0], ret[1])
                return ("D", 0)
            elif ret[0] == "D":
                return ("D", 0)
    return None

def explode(p):
    explode_helper(p, 0)
    return p

def split(p):
    split_helper(p)
    return p

def split_helper(p):
    if type(p[0]) is int and p[0] > 9:
        x = p[0]
        p[0] = [x // 2, (x+1) // 2]
        return True
    if type(p[0]) is list:
        r = split_helper(p[0])
        if r:
            return True
    if type(p[1]) is int and p[1] > 9:
        x = p[1]
        p[1] = [x // 2, (x+1) // 2]
        return True
    if type(p[1]) is list:
        r = split_helper(p[1])
        if r:
            return True
    return False

last_reduce = []

def reduce(p):
    global last_reduce
    last_reduce = []
    while True:
        # print("{}\t\t{}".format(p[0], p[1]))
        last_reduce.append(copy.deepcopy(p))
        ret = explode_helper(p, 0)
        if ret is not None:
            continue

        ret = split_helper(p)
        if ret:
            continue
        break
    last_reduce.append(copy.deepcopy(p))
    return p

def magnitude(p):
    if type(p) is int:
        return p
    return magnitude(p[0]) * 3 + magnitude(p[1]) * 2

p = x[0]
c = 0
for i in range(1, len(x)):
    print()
    print(p)
    print()
    c += 1
    if c > 4:
        pass
        #break
    p = [p, x[i]]
    reduce(p)

def print_with_diff(p0, p1):
    if p1 == p0:
        print(p1, end="")
    elif type(p0) != type(p1):
        color.write(str(p1), "ERROR")
    # types match but values do not
    elif type(p1) is int:
        color.write(str(p1), "ERROR")
    else:
        print("[", end="")
        print_with_diff(p0[0], p1[0])
        print(", ", end="")
        print_with_diff(p0[1], p1[1])
        print("]", end="")    

def print_last_reduce():
    print(last_reduce[0])
    for i in range(1, len(last_reduce)):
        print_with_diff(last_reduce[i-1], last_reduce[i])
        print()

    

x = [eval(i) for i in a]

res = []

for i1 in range(len(x)):
    for i2 in range(len(x)):
        e = [copy.deepcopy(x[i1]), copy.deepcopy(x[i2])]
        reduce(e)
        res.append(magnitude(e))

print(max(res))
