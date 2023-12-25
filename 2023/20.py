with(open('inp20.txt') as f) :
     raw=f.read()

raw2 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

raw3 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

a = raw[:-1].split('\n')

rules = {}
for elem in a:
    name, outs = elem.split(' -> ')
    t = 'b'
    if name != "broadcaster":
        t = name[0]
        name = name[1:]
    o = outs.split(', ')
    rules[name] =  (t, o)

con_modules = set([name for name, v in rules.items() if v[0] == '&'])
flp_modules = set([name for name, v in rules.items() if v[0] == '%'])
state = {}
for e in flp_modules:
    state[e] = False
for e in con_modules:
    state[e] = {}
for k, v in rules.items():
    for out in v[1]:
        if out in con_modules:
            state[out][k] = False

DONE = False
def send_pulse():
    to_do = [(False, 'broadcaster', 'button')]
    cnt_h = 0
    cnt_l = 0
    while len(to_do) > 0:
        (signal, name, fro) = to_do.pop(0)
        if signal:
            cnt_h += 1
        else:
            cnt_l += 1
        #print("{} -{}-> {}  ({})".format(fro, 'high' if signal else 'low', name, (cnt_h, cnt_l)))
        if name == 'xt' and signal == False:
            global DONE
            DONE = True
        if name not in rules:
            continue
        r = rules[name]
        if r[0] == 'b':
            for o in r[1]:
                to_do.append((signal, o, name))
        elif r[0] == '%':
            if signal == False:
                state[name] = not state[name]
                for o in r[1]:
                    to_do.append((state[name], o, name))
        elif r[0] == '&':
            state[name][fro] = signal
            if all(state[name].values()):
                s = False
            else:
                s = True
            for o in r[1]:
                to_do.append((s, o, name))

    return (cnt_h, cnt_l)

def solve():
    res = (0,0)
    for i in range(1000):
        h, l = send_pulse()
        res = (res[0] + h, res[1]+l)
    return res[0] * res[1]

#print(solve())
s = 0
while s < 10000:
    s+= 1
    send_pulse()
    if DONE:
        print(s)
        DONE = False
    #if s > 2220:
    #    res = []
    #    for e in ['nt', 'cx', 'qh', 'ln', 'mq', 'hs', 'sl', 'zl', 'nj', 'pt', 'gt', 'hg']:
    #        res.append('1' if state[e] else '0')
    #    print(s, ''.join(res), state['xq'])
print(s)

sp = 3929
lk = 3823
zv = 4051
xt = 3767
# above are number of steps for each sub-tree
# answer is their LCM

