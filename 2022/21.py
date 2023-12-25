import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

with open('21.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

monkey = {}
for x in b:
    mon,y = x.split(': ')
    vals = y.split(' ')
    if len(vals) == 1:
        monkey[mon] = int(vals[0])
    else:
        monkey[mon] = (vals[1], vals[0], vals[2])

values = {}
def valuate(name):
    if name not in values:
        if name == 'humn':
            raise Exception('Failed to valuate human')
        if isinstance(monkey[name], int):
            values[name] = monkey[name]
        else:
            ops = {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a // b,
            }
            mon = monkey[name]
            values[name] = ops[mon[0]](valuate(mon[1]), valuate(mon[2]))
    return values[name]

human_poisoned = set(['humn'])
def check_human(name):
    if name in human_poisoned:
        return True
    if isinstance(monkey[name], int):
        return False
    if check_human(monkey[name][1]) or check_human(monkey[name][2]):
        human_poisoned.add(name)
        return True
    return False
check_human('root')    

def expect(name, value):
    if name == 'humn':
        return value
    if monkey[name][1] in human_poisoned:
        if monkey[name][0] == '+':
            return expect(monkey[name][1], value - valuate(monkey[name][2]))
        if monkey[name][0] == '-':
            return expect(monkey[name][1], value + valuate(monkey[name][2]))
        if monkey[name][0] == '*':
            return expect(monkey[name][1], value // valuate(monkey[name][2]))
        if monkey[name][0] == '/':
            return expect(monkey[name][1], value * valuate(monkey[name][2]))
    else:
        if monkey[name][0] == '+':
            return expect(monkey[name][2], value - valuate(monkey[name][1]))
        if monkey[name][0] == '-':
            return expect(monkey[name][2], valuate(monkey[name][1]) - value)
        if monkey[name][0] == '*':
            return expect(monkey[name][2], value // valuate(monkey[name][1]))
        if monkey[name][0] == '/':
            return expect(monkey[name][2], valuate(monkey[name][1]) // value)
    
#values['humn'] = 5842743947753


            
#x = valuate(monkey['root'][1])
y = valuate(monkey['root'][2])
#print((x,y))
print(expect(monkey['root'][1], y))
    
