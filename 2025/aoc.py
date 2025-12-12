def parse_lines(fi):
    with(open(fi) as f):
        return f.read().split('\n')[:-1]

def parse_blocks(fi):
    with(open(fi) as f):
        return f.read().split('\n\n')

def lb(day):
    input_file = "inp" + str(day) + ".txt"
    sample_file = "sample" + str(day) + ".txt"
    a, b = parse_blocks(input_file), parse_blocks(sample_file)
    return list(map(lambda x: x.split('\n'), a)), list(map(lambda x: x.split('\n'), b))
    #return (parse_lines(input_file), parse_lines(sample_file))


def l(day):
    input_file = "inp" + str(day) + ".txt"
    sample_file = "sample" + str(day) + ".txt"
    return (parse_lines(input_file), parse_lines(sample_file))

C_NEIGH = [1, -1, 1+1j, 1j, -1+1j, 1-1j, -1j, -1-1j]

def parse_complex(l, cond):
    res = set()
    for y, row in enumerate(l):
        for x, elem in enumerate(row):
            if cond(elem):
                res.add(x + 1j * y)
    return res
