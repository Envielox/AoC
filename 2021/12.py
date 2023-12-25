with open('12.in') as f:
    a = [x[:-1] for x in f.readlines()]

from collections import defaultdict

dirs = defaultdict(list)

for x in a:
    s,t =  x.split('-')
    dirs[s].append(t)
    dirs[t].append(s)

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_all_paths():
    paths = [['start']]
    result = []
    while len(paths) > 0:
        p = paths.pop()
        if p[-1] == 'end':
            result.append(p)
            continue
        for d in dirs[p[-1]]:
            if d[0] in uppercase or d not in p:
                paths.append(p + [d])
    return result

print( len(find_all_paths()))

def can_go_there(p, nex):
    if nex == 'start':
        return False
    if nex == 'end':
        return True
    if nex[0] in uppercase:
        return True
    if nex not in p:
        return True
    lc = [x for x in p if x[0] not in uppercase]
    lcs = set(lc)
    return len(lc) == len(lcs)

def find_all_paths_2():
    paths = [['start']]
    result = []
    while len(paths) > 0:
        p = paths.pop()
        if p[-1] == 'end':
            result.append(p)
            continue
        for d in dirs[p[-1]]:
            if can_go_there(p, d):
                paths.append(p + [d])
    return result

print (len(find_all_paths_2()))
