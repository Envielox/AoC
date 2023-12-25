inp = "target area: x=179..201, y=-109..-63"

sample = ((20, 30), (-10, -5))
target = ((179, 201), (-109, -63))

def gen_x_vel(x):
    return [i for i in range(x, 0, -1)] + [0] * 300

def gen_x_pos(x):
    pos = 0
    res = []
    for i in gen_x_vel(x):
        pos += i
        res.append(pos)
    return res

def find_all_matching_x_vel(min_x, max_x):
    res = {}
    for v in range(max_x + 1):
        positions = gen_x_pos(v)
        matching = [i for i, p in enumerate(positions) if min_x <= p and p <= max_x]
        if len(matching) > 0:
            res[v] = matching
    return res

def gen_y_vel(y):
    res = []
    vel = y
    STEPS=500
    for i in range(STEPS):
        res.append(vel)
        vel -= 1
    return res

def gen_y_pos(y):
    pos = 0
    res = []
    for i in gen_y_vel(y):
        pos += i
        res.append(pos)
    return res
    
def find_all_matching_y_vel(min_y, max_y):
    res = {}
    for v in range(500, -500, -1):
        positions = gen_y_pos(v)
        matching = [i for i, p in enumerate(positions) if min_y <= p and p <= max_y]
        if len(matching) > 0:
            res[v] = matching
    return res


Y_MIN = -10# -109
Y_MAX = -5#-63
X_MIN = 20#179
X_MAX = 30#201


from collections import defaultdict
turn_to_x_vel = defaultdict(list)
x_vel = find_all_matching_x_vel(X_MIN, X_MAX)
for k,l in x_vel.items():
    for i in l:
        turn_to_x_vel[i].append(k)

all_pairs = []

for y_vel, y_turn in find_all_matching_y_vel(Y_MIN, Y_MAX).items():
    found = False
    for t in y_turn:
        if t in turn_to_x_vel:
            print("Found for {} at turn {}".format(y_vel, t))
            print("Max pos: {}".format(max(gen_y_pos(y_vel))))
            for vx in turn_to_x_vel[t]:
                all_pairs.append((vx, y_vel))
            found = True
            #break
    if found:
        pass
        #break

