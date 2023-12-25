with(open('inp9.txt') as f) :
     raw=f.read()

raw2 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

a = raw[:-1].split('\n')

b = [[int(z) for z in x.split(' ')] for x in a]


def predict(l):
    if all([x == 0 for x in l]):
        return 0
    list_of_diffs = [l[i+1] - l[i] for i in range(len(l) - 1)]
    next_diff = predict(list_of_diffs)
    return l[-1] + next_diff

print(sum([predict(x) for x in b]))

def predict_b(l):
    if all([x == 0 for x in l]):
        return 0
    list_of_diffs = [l[i+1] - l[i] for i in range(len(l) - 1)]
    prev_diff = predict_b(list_of_diffs)
    return l[0] - prev_diff

print(sum([predict_b(x) for x in b]))
