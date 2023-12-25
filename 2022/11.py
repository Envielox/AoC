with open('11.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

items = []
params = []
score = []

te_mul = 1
for i in range(0, len(b), 7):
    # i + 0 monkey number
    l = b[i+1][len('  Starting items: '):]
    li = l.split(', ')
    items.append([int(x) for x in li])
    op = b[i+2][len('  Operation: new = old '):].split(' ')
    te = int(b[i+3][len('  Test: divisible by '):])
    ift = int(b[i+4][len('    If true: throw to monkey '):])
    iff = int(b[i+5][len('    If false: throw to monkey '):])
    if op[1] == 'old' and op[0] == '*':
        op[0] = '**'
        op[1] = '2'
    params.append((op[0], int(op[1]), te, ift, iff))
    score.append(0)
    te_mul *= te

def exc(val1, op, val2):
    if op == '+':
        return val1+val2
    if op == '*':
        return val1*val2
    if op == '**':
        return val1**val2
    raise Exception('Unknown operation: {}'.format(op))
    
def round(idx):
    score[idx] += len(items[idx])
    for item in items[idx]:
        #print(item)
        item = exc(item, params[idx][0], params[idx][1])
        item = item % te_mul
        #print(item)
        ## Star 2 ## item = item // 3
        t= item % params[idx][2] == 0
        new_mon = params[idx][3] if t else params[idx][4]
        #print("Item with worry lvl {} is thrown to {}".format(item, new_mon))
        items[new_mon].append(item)
    items[idx] = []

def turn():
    for i in range(len(params)):
        round(i)
    # print(items)

def n_turns(n):
    for i in range(n):
        turn()
        if i % 100 == 0:
            print(i)

n_turns(10_000)
res = sorted(score)[-2:]
print(res[0] * res[1])
