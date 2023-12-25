with open('10.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

vals = []
nex = 1

for x in b:
    if x == 'noop':
        vals.append(nex)
        # next doesn't change
    else:
        c,d = x.split(' ')
        vals.append(nex)
        vals.append(nex)
        nex += int(d)

w = list( zip(vals[20::40], range(20, len(vals), 40)))
print(sum(map(lambda x: x[0]*x[1], w)))

for i, v in enumerate(vals):
    if abs(v - i%40) <= 1:
        print('#', end='')
    else:
        print(' ', end='')
    if i % 40 == 39:
        print()
