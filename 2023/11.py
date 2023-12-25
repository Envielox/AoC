with(open('inp11.txt') as f) :
     raw=f.read()

raw2 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

a = raw[:-1].split('\n')

galaxy = []
row_cnt = [0] * len(a)
col_cnt = [0] * len(a[0])

for y in range(len(a)):
    for x in range(len(a[0])):
        if a[y][x] == '#':
            galaxy.append((x,y))
            row_cnt[y] += 1
            col_cnt[x] += 1

extra_rows = []
extra_cols = []
extra = 0

for y in range(len(a)):
    if row_cnt[y] == 0:
        extra += 1
    extra_rows.append(extra)

extra = 0
for x in range(len(a[0])):
    if col_cnt[x] == 0:
        extra += 1
    extra_cols.append(extra)

def expanded_pos(pos, SPACE_CONSTANT=1):
    return (pos[0] + extra_cols[pos[0]] * SPACE_CONSTANT, pos[1] + extra_rows[pos[1]] * SPACE_CONSTANT)


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def score(SPACE_CONSTANT=1):
    score = 0
    for g1 in range(len(galaxy)-1):
        for g2 in range(g1+1, len(galaxy)):
            score += dist(expanded_pos(galaxy[g1], SPACE_CONSTANT), expanded_pos(galaxy[g2], SPACE_CONSTANT))
    return score

print(score(1))
print(score(999999))





    
