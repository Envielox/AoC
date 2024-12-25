input_file="inp9.txt"
sample_file="sample9.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

b = [int(x) for x in a[0]]

c = [-1] * sum(b)

idx = 0
for i in range(len(b)):
    if i % 2 == 0:
       fn = i // 2
       for num in range(b[i]):
           c[idx] = fn
           idx += 1
    else:
        idx += b[i]

end_idx = len(c) - 1
start_idx = 0

while start_idx < end_idx:
    while start_idx < end_idx and c[start_idx] != -1:
        start_idx += 1
    while start_idx < end_idx and c[end_idx] == -1:
        end_idx -= 1
    if start_idx >= end_idx:
        break
    c[start_idx], c[end_idx] = c[end_idx], c[start_idx]
    
#checksum
print(sum(map(lambda a: a[0] * a[1], enumerate(c[:end_idx]))))

d = {}
f_to_d = {}

idx = 0
max_fn = 0
prev_idx = -1
for i in range(len(b)):
    if i % 2 == 0:
       fn = i // 2
       max_fn = fn
       d[idx] = (fn, b[i], prev_idx)
       if b[i] != 0:
           prev_idx = idx
       f_to_d[fn] = idx
       idx += b[i]
    else:
        d[idx] = (-1, b[i], prev_idx)
        if b[i] != 0:
            prev_idx = idx
        idx += b[i]


fd = max_fn + 1
while fd > 0:
    fd -= 1
    #print(fd)
    #print(d)
    # find file with id
    i = f_to_d[fd]
    size = d[i][1]
    
    # go from beginnig until big enough empty
    j = 0
    while j < i:
        if d[j][0] == -1 and d[j][1] >= size:
            break
        j += d[j][1]
    if j == i:
        continue
    #print("found {}".format(j))
    # change empty to file, add new empty (smaller)
    old_elem = d[j]
    d[j] = (fd, size, d[j][2])
    f_to_d[fd] = j
    if size < old_elem[1]:
        d[j+size] = (-1, old_elem[1] - size, j)
        nex = j + old_elem[1]
        d[nex] = (d[nex][0], d[nex][1], j+size)
        
    
    # merge with following empty
    d[i] = (-1, size, d[i][2])
    if i + size < len(c) and d[i + size][0] == -1:
        t = d[i + size]
        del d[i + size]
        d[i] = (-1, size + t[1], d[i][2])

    # merge with prev empty
    prev_idx = d[i][2]
    if d[prev_idx][0] == -1:
        d[prev_idx] = (-1, d[prev_idx][1] + d[i][1], d[prev_idx][2])
        next_idx = prev_idx + d[prev_idx][1]
        if next_idx < len(c):
            d[next_idx] = (d[next_idx][0], d[next_idx][1], prev_idx)
        del d[i]


#checksum
ck2 = 0
idx = 0

while idx < len(c):
    elem = d[idx]
    if elem[0] != -1:
        for k in range(elem[1]):
            ck2 += (idx+k) * elem[0]
    idx += elem[1]
    #print (idx)
print(ck2)




