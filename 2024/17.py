input_file="inp17.txt"
sample_file="sample17.txt"
assert(input_file[-1] == sample_file[-1])

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)


A = int(a[0][len('Register X: '):])
B = int(a[1][len('Register X: '):])
C = int(a[2][len('Register X: '):])

P = [int(x) for x in a[4][len('Program: '):].split(',')]

S = {
    'ip': 0,
    'A': A,
    'B': B,
    'C': C,
    'prog': P,
    }

def combo(op, S):
    res = [0,1,2,3,S['A'], S['B'], S['C']]
    return res[op]


def run_step(S, out):
    if S['ip'] >= len(S['prog']) - 1:
        return "HALT"
    ins = S['prog'][S['ip']]
    op = S['prog'][S['ip']+1]

    match ins:
        case 0:  #adv
            S['A'] = S['A'] // (2**combo(op, S))
        case 1:  #bxl
            S['B'] = S['B'] ^ op
        case 2:  #bst
            S['B'] = combo(op, S) % 8
        case 3:  #jnz
            if S['A'] != 0:
                S['ip'] = op - 2 # we will add 2 after this step
        case 4:  #bxc
            S['B'] ^= S['C']
        case 5:  #out
            out.append(combo(op, S) % 8)
        case 6:  #bdv
            S['B'] = S['A'] // (2**combo(op, S))
        case 7:  #bdv
            S['C'] = S['A'] // (2**combo(op, S))
    S['ip'] += 2

def run_prog(S):
    out = []
    while run_step(S, out) != "HALT":
        pass
        #print(S)
    #print(S)
    return out


out=run_prog(S)
print(','.join(map(str, out)))

def run_with_A(w):
        St = {'ip': 0, 'A': w, 'B': B, 'C': C, 'prog': P, }
        return run_prog(St)
        


# 2,4 BST B= A%8
# 1,5 BXL B=B^5
# 7,5 CDV C=A/2**B
# 1,6 BXL B=B^6
# 4,3 BXC B=B^C
# 5,5 out B,
# 0,3 ADV A=A/8
# 3,0 jnz 0

def other(A):
    B = 0
    C = 0
    res = []
    while A > 0:
        B = A%8
        B ^= 5
        C = A // (2**B)
        B ^= 6
        B ^= C
        res.append(B%8)
        A = A//8
    return res

def getV(v):
    return(sum(x * 8**i for i,x in enumerate(v)))

def break_A():
    vals = [[] for i in range(17)]
    vals[16] = [[0]*16]
    for pos in range(15,-1,-1):
        print ("POS: {} #{}".format(pos, len(vals[pos+1])))
        
        for val in vals[pos+1]:
            #print("POS: {}, val: {}".format(pos, val))
            for i in range(8):
                res = run_with_A(i*8**pos + getV(val))
                if len(res) == 16 and res[pos] == P[pos]:
                    nv = val[:]
                    nv[pos]=i
                    vals[pos].append(nv)
    return vals[0]

vals = break_A()

print(min(map(getV, vals)))





