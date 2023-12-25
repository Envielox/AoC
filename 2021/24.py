def step(instr, state, inp):
    si = instr.split()
    if si[0] == 'inp':
        state[si[1]] = int(inp[0])
        up_inp = inp[1:]
        return state, up_inp
    if si[2] in 'xyzw':
        p2 = state[si[2]]
    else:
        p2 = int(si[2])
    if si[0] == 'add':
        state[si[1]] += p2
        return state, inp
    if si[0] == 'mul':
        state[si[1]] *= p2
        return state, inp
    if si[0] == 'div':
        state[si[1]] = int(state[si[1]] / p2)
        return state, inp
    if si[0] == 'mod':
        state[si[1]] = int(state[si[1]] % p2)
        return state, inp
    if si[0] == 'eql':
        state[si[1]] = 1 if state[si[1]] == p2 else 0
        return state, inp

def run_prog(prog, state, inp):
    instr = prog.split('\n')
    for i in instr:
        state, inp = step(i, state, inp)
    return state

def empty():
    return {
        'x': 0,
        'y': 0,
        'z': 0,
        'w': 0,
    }

params = [
(1, 15, 15),
(1, 15, 10),
(1, 12, 2),
(1, 13, 16),
(26, -12, 12),
(1, 10, 11),
(26, -9, 5),
(1, 14, 16),
(1, 13, 6),
(26, -14, 15),
(26, -11, 3),
(26, -2, 12),
(26, -16, 10),
(26, -14, 13),
]

prog = \
"""inp w
mul x 0
add x z
mod x 26
div z {}
add x {}
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y {}
mul y x
add z y"""


