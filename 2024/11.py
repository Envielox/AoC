ar = [int(x) for x in "773 79858 0 71 213357 2937 1 3998391".split()] # real
ae = [125, 17]

def b(elem):
    if elem == 0:
        return [1]
    if len(str(elem)) % 2 == 0:
        s = str(elem)
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    return [elem * 2024]

def blink(l):
    return sum(map(b, l), [])

def blinkn(l, n):
    for i in range(n):
        # print(l)
        l = blink(l)
    return l

# print (len(blinkn(ar, 25)))

import functools

@functools.cache
def blink_sum(l, n):
    if n == 0:
        return len(l)
    
    res = 0
    for elem in l:
        res += blink_sum(tuple(b(elem)), n-1)
    return res
    
