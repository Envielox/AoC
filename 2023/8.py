with(open('inp8.txt') as f) :
     raw=f.read()

raw2 = """
"""

a = raw[:-1].split('\n')

ins = a[0]

d = {x[0:3] : (x[7:10], x[12:15]) for x in a[2:]}

def nex(elem, di):
    if di == 'L':
        return d[elem][0]
    else:
        return d[elem][1]

def walk():
    step = 0
    cur = 'AAA'
    while cur != 'ZZZ':
        s = ins[step%len(ins)]
        cur = nex(cur, s)
        step += 1
    return step

start_nodes = [x[0:3] for x in a[2:] if x[2] == 'A']

def walk2(start_nodes=start_nodes):
    step = 0
    cur = start_nodes
    while not all([x[2] == 'Z' for x in cur]) :
        s = ins[step%len(ins)]
        cur = [nex(elem, s)  for elem in cur]
        step += 1
    print(cur)
    return step


def find_cycle(start, step=0):
    cur = start
    visited_at_zero = set()
    visited_time = {}
    while True:
        if step % len(ins) == 0:
            if cur in visited_at_zero:
                break
            visited_at_zero.add(cur)
            visited_time[cur] = step
        cur = nex(cur, ins[step%len(ins)])
        step += 1
    return cur, step, visited_time[cur], (step - visited_time[cur])/len(ins)


def find_ends(start, steps_max):
    step = 0
    win = []
    cur = start
    while step < steps_max:
        if cur[2] == 'Z':
            win.append(step)
        cur = nex(cur, ins[step%len(ins)])
        step += 1
    return win

equation = [(x, find_ends(x, 100000)[0], len(ins)*find_cycle(x)[3]) for x in start_nodes]

# calculate LCM  of all cycles

    
