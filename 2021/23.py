sample = {
    "A1" : (1,2),
    "A2" : (7,2),
    "B1" : (1,1),
    "B2" : (5,1),
    "C1" : (3,1),
    "C2" : (5,2),
    "D1" : (3,2),
    "D2" : (7,1),
}

real = {
    "A1" : (5,2),
    "A2" : (7,1),
    "B1" : (1,2),
    "B2" : (3,1),
    "C1" : (1,1),
    "C2" : (7,2),
    "D1" : (3,2),
    "D2" : (5,1),
}

star_2 = {
    "D3": (1,2),
    "D4": (1,3),
    "C3": (3,2),
    "C4": (7,3),
    "B3": (3,3),
    "B4": (5,2),
    "A3": (5,3),
    "A4": (7,2),
    }

def update_to_star2(state):
    state=state.copy()
    for name in state:
        if state[name][1] == 2:
            state[name] = (state[name][0], 4)
    state = {**state, **star_2}
    return state

sample_s2 = update_to_star2(sample)
real_s2 = update_to_star2(real)

resting_spaces = [
    (0,0), (0,1),
    (2,0),
    (4,0),
    (6,0),
    (8,0), (8,1)
]

HOME_SIZE = 4

def steps(fro, to):
    return fro[1] + abs(fro[0] - to[0]) + to[1]

def can_move(state, fro, to):
    must_be_empty = set([to])
    if fro[1] >= 2:
        for i in range(1, fro[1]):
            must_be_empty.add((fro[0], i))
    if to[1] == 2:
        for i in range(1, to[1]):
            must_be_empty.add((to[0], i))
    if fro == (0,1) or to == (0,1):
        must_be_empty.add((0,0))
    if fro == (8,1) or to == (8,1):
        must_be_empty.add((8,0))
    for i in range(
            min(fro[0], to[0]),
            max(fro[0], to[0])+1
            ):
        must_be_empty.add((i, 0))
    if fro in must_be_empty:
        must_be_empty.remove(fro)
    occupied = set(state.values())
    #print("Trying to move from: {} to: {}".format(fro, to))
    #print(occupied)
    #print(must_be_empty)
    return len(occupied.intersection(must_be_empty)) == 0
    
def get_home(name):
    homes = {
        "A": 1,
        "B": 3,
        "C": 5,
        "D": 7,
        }
    return homes[name[0]]

def cost(name):
    costs = {
        "A": 1,
        "B": 10,
        "C": 100,
        "D": 1000,
        }
    return costs[name[0]]

def partner_pos(state,name):
    if name[1] == '1':
        x = '2'
    else:
        x = '1'
    return state[name[0] + x]

def state_after_move(state, name, pos):
    cos = cost(name) * steps(state[name], pos)
    new_state = state.copy()
    new_state[name] = pos
    return (cos, new_state)

def how_many_at_home(state, name):  
    res = 0
    for n in state:
        if state[n][0] == get_home(name):
            if n[0] != name[0]:
                return -1
            res += 1
    return res

def is_at_home(state, name):
    for n in state:
        if state[n][0] == get_home(name):
            if n[0] != name[0]:
                return False # Someone else at our home
    return state[name][0] == get_home(name)

def gen_steps(state):
    # if someone can go home, they go
    for name in state:
        #print(name)
        if is_at_home(state, name):
            continue
        home = get_home(name)
        st = how_many_at_home(state, name)
        if st == -1:
            continue
        if can_move(state, state[name], (home, HOME_SIZE-st)):
            return [state_after_move(state, name, (home, HOME_SIZE-st))]
    # otherwise generate all possible steps of getting out of homes to the free spaces
    res = []
    for name in state:
        if is_at_home(state, name):
            continue
        if state[name][1] == 0 or state[name][0] in [0,8]:
            continue # outside of home already, they can only go home in the above if
        for to in resting_spaces:
            if can_move(state, state[name], to):
                res.append(state_after_move(state, name, to))
    return res

def is_end(state):
    for name in state:
        if state[name][0] != get_home(name):
            return False
    return True

from queue import PriorityQueue

states = PriorityQueue()

from itertools import count


def tuplify_state(state):
    keys = list(state.keys())
    keys.sort()
    res = []
    for k in keys:
        res.append(state[k])
    return tuple(res)

def solve(state):
    unique = count()
    states.put((0, next(unique), state))

    visited_states = set()

    c=0
    while states.qsize() > 0:
        cur = states.get()
        if tuplify_state(cur[2]) in visited_states:
            continue
        visited_states.add(tuplify_state(cur[2]))

        if is_end(cur[2]):
            return (cur[0])

        #print("{} {}".format(cur[0], cur[2]))
        c += 1
        if c % 1000 == 0:
            print("Step {}, len: {}, min_val: {}".format(c, states.qsize(), cur[0] ))
        new_steps = gen_steps(cur[2])
        for elem in new_steps:
            states.put((cur[0] + elem[0], next(unique), elem[1]))
    return "ERROR not found"

test_state = {
    "A1" : (7,2),
    "A2" : (1,2),
    "B1" : (3,1),
    "B2" : (3,2),
    "C1" : (5,1),
    "C2" : (5,2),
    "D1" : (4,0),
    "D2" : (7,1),
}

