with open('8.in') as f:
    a = [x[:-1] for x in f.readlines()]

#a = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
d = [[z.split() for z in x.split(' | ')] for x in a]

di = [x[1] for x in d]

lens = [len([1 for x in z if len(x) in [2,3,4,7]]) for z in di]
print(sum(lens))

mapping = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg,'
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

def translate(t, digits):
    new_dig = [t[d] for d in digits]
    new_dig.sort()
    return ''.join(new_dig)

def get_num(x):
    for k,v in mapping.items():
        if x == v:
            return k
    return -1

def solve_entry_2(digits, numbers):
    _1 = [x for x in digits if len(x) == 2][0]
    _4 = [x for x in digits if len(x) == 4][0]
    _7 = [x for x in digits if len(x) == 3][0]
    _a = [x for x in _7 if x not in _1][0]
    
    digit_count = {d: sum((1 for x in digits if d in x)) for d in 'abcdefg'}
    _f = [k for k,v in digit_count.items() if v == 9][0]
    _c = [l for l in _1 if l != _f][0]
    _b = [k for k,v in digit_count.items() if v == 6][0]
    _d = [x for x in _4 if x not in _1 and x != _b][0]
    _e = [k for k,v in digit_count.items() if v == 4][0]
    _g = [k for k in 'abcdefg' if k not in [_a, _b, _c, _d, _e, _f]][0]
    tr = {'a': _a, 'b': _b, 'c': _c, 'd': _d, 'e': _e, 'f': _f, 'g': _g}
    rt = {v: k for k,v in tr.items()}
    numbers = [get_num(translate(rt, x)) for x in numbers]
    
    num = int(''.join(map(str, numbers)))
    return num


results = [solve_entry_2(dx[0], dx[1]) for dx in d]
print(results)
print(sum(results))
