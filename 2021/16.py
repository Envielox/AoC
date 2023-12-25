with open('16.in') as f:
    a = [x[:-1] for x in f.readlines()]

v = a[0]

def get_bits(x):
    return ('0000' + bin(int(x, 16))[2:])[-4:]

def hex_to_bits(h):
    return ''.join([get_bits(x) for x in h])

bits = hex_to_bits(v)

def parse_data(d):
    result = ''
    rest = d[:]
    while True:
        group = rest[:5]
        rest = rest[5:]
        result += group[1:]
        if group[0] == '0':
            break
    return int(result, 2), rest

def parse_packet(p):
    res = {}
    res['v'] = int(p[0:3], 2)
    res['t'] = int(p[3:6], 2)
    if res['t'] == 4:
        res['val'], rest = parse_data(p[6:])
        return res, rest
    # sub packets
    res['sub'] = []
    if p[6] == '0': # 15 bit total len
        max_len = int(p[7: 7+15], 2)
        sub_data = p[7+15: 7+15+max_len]
        total_rest = p[7+15+max_len:]
        rest = sub_data[:]
        while True:
            s, rest = parse_packet(rest)
            res['sub'].append(s)
            if rest == '':
                break
        return res, total_rest
    else: # 11 bit packet num
        packet_num = int(p[7: 7+11], 2)
        rest = p[7+11:]
        for i in range(packet_num):
            s, rest = parse_packet(rest)
            res['sub'].append(s)
        return res, rest

def get_all_v(s):
    if 'val' in s:
        return s['v']
    return s['v'] + sum([get_all_v(elem) for elem in s['sub']])
        
def do_all(h):
    b = hex_to_bits(h)
    d, r = parse_packet(b)
    print(r)
    return get_all_v(d)

def eva(s):
    if s['t'] == 0:
        return sum([eva(x) for x in s['sub']])
    if s['t'] == 1:
        prod = 1
        for x in s['sub']:
            prod *= eva(x)
        return prod
    if s['t'] == 2:
        return min([eva(x) for x in s['sub']])
    if s['t'] == 3:
        return max([eva(x) for x in s['sub']])
    if s['t'] == 4:
        return s['val']
    if s['t'] == 5:
        return 1 if eva(s['sub'][0]) > eva(s['sub'][1]) else 0
    if s['t'] == 6:
        return 1 if eva(s['sub'][0]) < eva(s['sub'][1]) else 0
    if s['t'] == 7:
        return 1 if eva(s['sub'][0]) == eva(s['sub'][1]) else 0
        
def do_all2(h):
    b = hex_to_bits(h)
    d, r = parse_packet(b)
    print(r)
    return eva(d)
