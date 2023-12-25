with(open('inp6.txt') as f) :
     raw=f.read()

raw2 = """Time:      7  15   30
Distance:  9  40  200
"""

a = raw[:-1].split('\n')


TIMES = [int(x) for x in a[0].split(' ')[1:] if x != ""]
DIST = [int(x) for x in a[1].split(' ')[1:] if x != ""]

def dist(hold, total):
    return hold * (total - hold)

def num(total, win):
    score = 0
    for i in range(total):
        if dist(i, total) > win:
            score += 1

    return score

def score():
    res = 1
    for i in range(len(TIMES)):
        res *= num(TIMES[i],DIST[i])
    return res

print(score())

TF = int(a[0].split(':')[1].replace(' ', ''))
DF = int(a[1].split(':')[1].replace(' ', ''))

print(num(TF, DF))
