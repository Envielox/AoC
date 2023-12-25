with open('2.in') as f:
          a = f.read()

b = a.split('\n')

c = [(x[0], x[2]) for x in b[:-1]]

def m(a):
    d = {
        'A': 0,
        'B': 1,
        'C': 2,
        
        'X': 0,
        'Y': 1,
        'Z': 2,
        }
    return d[a]

def res(a, b):
    ax = m(a)
    bx = m(b)
    if ax == bx:
        return 3
    if (ax + 1) % 3 == bx: # 1 is "A", 2 is "Y", 1 lost
        return 6
    if (bx + 1) % 3 == ax:
        return 0
    raise Exception('Unnown score for plays: {} {}'.format(a,b))

def score(e):
   d = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        }
   return d[e[1]] + res(e[0], e[1])

def get_my(e):
   dist = ord(e[1]) - ord('Y')
   my = ord(e[0]) + dist
   return chr((my - ord('A')) % 3 + ord('A'))
   
def score2(e):
   my = get_my(e)
   d = {
        'A': 1,
        'B': 2,
        'C': 3,
        }
   return d[my] + res(e[0], my)
