with(open('inp4.txt') as f) :
     raw=f.read()

raw2 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

a = raw.split('\n')[:-1]

a = [x.split(": ")[1] for x in a]

def parse_list(l):
    return [int(x) for x in l.split(" ") if x != ""]

b = [(parse_list(z.split(' | ')[0]), parse_list(z.split(' | ')[1])) for z in a]

def score(c):
    s = 0
    for elem in c[1]:
        if elem in c[0]:
            if s == 0:
                s = 1
            else:
                s *= 2
    return s

def score2(c):
    return len(set(c[0]).intersection(set(c[1])))



print (sum(map(score, b)))

num_cards = [1] * len(b)

for idx in range(len(b)):
    s = score2(b[idx])
    for add in range(s):
        num_cards[idx + 1 + add] += num_cards[idx]

print(sum(num_cards))
