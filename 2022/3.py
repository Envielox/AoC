with open('3.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

def divide(a):
    return a[:len(a)//2], a[len(a)//2:]

def find_match(a,b):
    ax = set(a)
    bx = set(b)
    return ax.intersection(bx).pop()

def find_match2(a,b,c):
    ax = set(a)
    bx = set(b)
    cx = set(c)
    return ax.intersection(bx).intersection(cx).pop()


def score(l):
    x = ord(l)
    if x >= 97:
        return x - 97 + 1
    return x - 65 + 27

def solve():
    s = [ score(find_match(*divide(x))) for x in b]
    return sum(s)

def solve2():
    res = 0
    for idx in range(0,len(b), 3):
        elem = find_match2(b[idx], b[idx+1], b[idx+2])
        res += score(elem)
    return res
