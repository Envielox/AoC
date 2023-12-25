with open('7.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = [ x.split(' ') for x in b]

cwd = []
contents = {}


def parse_all(lines):
    i = 0
    while i < len(lines):
        if lines[i][0] != '$':
            raise Exception ("Wrong command line ({}): {}".format(i, lines[i]))
        inp = lines[i][1:]
        i+=1
        output = []
        while i < len(lines) and lines[i][0] != '$':
            output.append(lines[i])
            i+=1
        parse_command(inp, output)
        

def parse_command(inp, output):
    global cwd
    global contents
    if inp[0] == 'cd':
        if inp[1] == '/':
            cwd = []
        elif inp[1] == '..':
            cwd.pop()
        else:
            cwd.append(inp[1])
    elif inp[0] == 'ls':
        loc = '/' + '/'.join(cwd)
        if loc in contents:
            raise Exception("Directory {} already processed".format(loc))
        cont = []
        for l in output:
            if l[0] == 'dir':
                cont.append((l[1], 'dir'))
            else:
                cont.append((l[1], int(l[0])))
        contents[loc] = cont
    else:
        raise Exception("Unknown command: {}".format(inp))
        
parse_all(c)

contents[''] = contents['/']

cumulative = {}
def find_cumulative(loc):
    global cumulative
    if loc in cumulative:
        return cumulative[loc]
    total = 0
    for v in contents[loc]:
        if v[1] == 'dir':
            total += find_cumulative(loc + '/' + v[0])
        else:
            total += v[1]
    cumulative[loc] = total
    return total

find_cumulative('')

res = 0
for k,v in cumulative.items():
    if v <= 100000:
        res += v
print(res) # star 1

disk = 70000000
needed = 30000000
used = cumulative['']
free = disk - used
to_del = needed - free

dirs = []
for k,v in cumulative.items():
    if v >= to_del:
        dirs.append((v, k))
dirs.sort()
print(dirs[0][0]) # star 2
