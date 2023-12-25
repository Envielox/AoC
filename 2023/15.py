with(open('inp15.txt') as f) :
     raw=f.read()

raw2 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

a = raw[:-1].split('\n')
b=a[0].split(',')

def hash(s):
    val = 0
    for elem in s:
        val += ord(elem)
        val *= 17
        val = val % 256
    return val

s = 0
for elem in b:
    s += hash(elem)
print(s)

boxes = [[] for x in range(256)]

def operate(s):
    if s[-1] == '-':
        label = s[:-1]
        box = hash(label)
        for k, v in enumerate(boxes[box]):
            if v[0] == label:
                del(boxes[box][k])
                break
    elif s[-2] == '=':
        label = s[:-2]
        box = hash(label)
        focus = int(s[-1])
        done = 0
        
        for k, v in enumerate(boxes[box]):
            if v[0] == label:
                boxes[box][k] = (label, focus)
                done = 1
                break
        if done == 0:
            boxes[box].append((label, focus))
        
        
def pp():
    for k, v in enumerate(boxes):
        if v != []:
            print(k, v)
    print()
            
for op in b:
    operate(op)
    #pp()

def score():
    total = 0
    for b in range(256):
        for k,v in enumerate(boxes[b]):
            total += (b+1) * (k+1) * v[1]
    return total

print(score())
