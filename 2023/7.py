with(open('inp7.txt') as f) :
     raw=f.read()

raw2 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

a = raw[:-1].split('\n')

def process(l):
    return [10 if x == 'T' else
            11 if x == 'J' else
            12 if x == 'Q' else
            13 if x == 'K' else
            14 if x == 'A' else
            int(x) for x in l]

def classify(l):
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    if len(d) == 1:
        return 50 # FIVE OF A KIND
    if len(d) == 2:
        any_elem = next(iter(d))
        if d[any_elem] in [4, 1]:
            return 40 # FOUR OF A KIND
        else:
            return 32 # FULL HOUSE
    if len(d) == 3:
        ite = iter(d)
        val = next(ite)
        if d[val] == 1:
            val = next(ite)
        if d[val] == 1:
            val = next(ite)
        if d[val] == 3:
            return 30 # THREE OF A KIND
        elif d[val] == 2:
            return 22 # TWO PAIR
        else:
            raise Exception("Unexpected count: " + str(d))
    if len(d) == 4:
        return 20 # ONE PAIR
    if len(d) == 5:
        return 10 # HIGH CARD
    raise Exception("Unexpected count: " + str(d))

b = []
for x in a:
    z, y = x.split(' ')
    l = process(z)
    b.append((classify(l), l, int(y)))

c = sorted(b)

score = 0

for k, v in enumerate(c):
    score += (k+1) * v[2]

print(score)


def process2(l):
    return [10 if x == 'T' else
             1 if x == 'J' else
            12 if x == 'Q' else
            13 if x == 'K' else
            14 if x == 'A' else
            int(x) for x in l]

def classify2(l):
    to_check = [[]]
    for pos in range(5):
        if l[pos] != 1:
            to_check = [x + [l[pos]] for x in to_check]
        else:
            new_check = []
            for test in range(2, 15):
                new_check.extend([x + [test] for x in to_check])
            to_check = new_check
    return max((classify(x) for x in to_check))


   
b2 = []
for x in a:
    z, y = x.split(' ')
    l = process2(z)
    b2.append((classify2(l), l, int(y)))

c2 = sorted(b2)

score = 0

for k, v in enumerate(c2):
    score += (k+1) * v[2]

print(score)
