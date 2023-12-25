with(open('inp5.txt') as f) :
     raw=f.read()

raw2 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

a = raw[:-1].split('\n\n')

seeds = list(map(int, a[0].split(' ')[1:]))

def parse_range(r):
    result = []
    for el in r.split('\n')[1:]:
        b, a, c = el.split(' ')
        result.append((int(a), int(b), int(c)))
    result.sort()
    return result

ss = parse_range(a[1])
sf = parse_range(a[2])
fw = parse_range(a[3])
wl = parse_range(a[4])
lt = parse_range(a[5])
th = parse_range(a[6])
hl = parse_range(a[7])

def get(m, s):
    prev = -1
    for e in m:
        if e[0] > s:
            break
        prev = e
    if prev == -1:
        return s
    if s <= prev[0] + prev[2] - 1:
        return prev[1] + (s - prev[0])
    return s

def solve(s):
    return get(hl, get(th, get(lt, get(wl, get(fw, get(sf, get(ss, s)))))))

print(min([ solve(s)  for s in seeds]))
    
seeds2 = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

def virtual_ranges(m):
    nex = 0
    res = []
    for e in m:
        if e[0] != nex:
            res.append((nex,nex,e[0]-nex))
        res.append(e)
        nex = e[0] + e[2]
    res.append((nex,nex,10e9))
    return res

    
def get_r(m, r):
    result = [] 
    range_start = r[0]
    range_size = r[1]
    for d in virtual_ranges(m):
        if range_start > d[0] + d[2]:
            continue
        if range_size <= 0:
            break
        x = min(range_size, d[2] - (range_start - d[0]))
        result.append((d[1] + (range_start - d[0]), x))
        range_start = range_start + x
        range_size -= x
    return result

def get_rs(m, rs):
    res = []
    for e in rs:
        res.extend(get_r(m, e))
    return res

def solve2(s):
    return get_rs(hl, get_rs(th, get_rs(lt, get_rs(wl, get_rs(fw, get_rs(sf, get_rs(ss, s)))))))

s2 = solve2(seeds2)
print(min(map(lambda x: x[0], s2)))


