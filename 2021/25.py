with open('25.in') as f:
    a = [x[:-1] for x in f.readlines()]

def to_map(m):
    return [[x for x in r] for r in m]

b = to_map(a)

def p(m):
    for r in m:
        print(''.join(r))

def move_hor(m):
    update_cnt = 0
    for y, row in enumerate(m):
        first_elem = row[0]
        updated_prev = False
        for x, elem in enumerate(row):
            if elem != '>' or updated_prev == True:
                updated_prev = False
                continue
            if x + 1 < len(row) and row[x+1] == '.':
                row[x] = '.'
                row[x+1] = '>'
                updated_prev = True
                update_cnt += 1
            elif x+1 >= len(row) and first_elem == '.':
                row[x] = '.'
                row[0] = '>'
                updated_prev = True
                update_cnt += 1
    return update_cnt


def move_vert(m):
    update_cnt = 0
    first_row = m[0][:]
    updated_prev = [False] * len(first_row)
    for y, row in enumerate(m):
        for x, elem in enumerate(row):
            #print((x,y))
            if elem != 'v' or updated_prev[x] == True:
                updated_prev[x] = False
                #print("T1")
                continue
            if y + 1 < len(m) and m[y+1][x] == '.':
                #print("T2 {}".format(m))
                row[x] = '.'
                m[y+1][x] = 'v'
                updated_prev[x] = True
                update_cnt += 1
            elif y+1 >= len(m) and first_row[x] == '.':
                #print("T3")
                row[x] = '.'
                m[0][x] = 'v'
                updated_prev[x] = True
                update_cnt += 1
    return update_cnt

def move(m):
    res = 0
    res += move_hor(m)
    res += move_vert(m)
    return res

res = -1
cnt = 0
while res != 0:
    res = move(b)
    cnt += 1

print(cnt)
            
                
            
