with open('4.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = [ [[int(z, 10) for z in y.split('-')] for y in x.split(',')] for x in b] 


def contains(a, b):
    if a[0] >= b[0] and b[1] >= a[1]:
        return True
    if b[0] >= a[0] and a[1] >= b[1]:
        return True
    return False

res = [contains(x[0], x[1]) for x in c]
result = len([1 for x in res if x == True])
print(result)

def overlap(a, b):
    if a[1] < b[0]:
        return False
    if b[1] < a[0]:
        return False
    return True

res = [overlap(x[0], x[1]) for x in c]
result = len([1 for x in res if x == True])
print(result)
