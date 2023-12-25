with open('16.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

import re

rx = re.compile('Valve (.+) has flow rate=(\d+); tunnels? leads? to valves? (.+)')

c = {}
for x in b:
    #print(x)
    m = rx.match(x)
    c[m.group(1)] = (int(m.group(2)), m.group(3).split(', '))

valuable = [k for k,v in c.items() if v[0] != 0]

def hashit(m):
    return ( m[1], m[2])

from queue import PriorityQueue

def DFS(LIMIT=30,valuable=valuable):
    moves = PriorityQueue()
    moves.put((0, 'AA', '', 0))
    max_score = 0
    max_steps = len(c) * 2**len(valuable)
    step = 0
    visited = set()
    while not moves.empty():
        move = moves.get()
        if hashit(move) in visited:
            continue
        visited.add(hashit(move))
        step += 1
        if step % 100000 == 0:
            print("Step {} of {}, (len of visited: {})".format(step, max_steps, len(visited)))
        if move[2] == valuable:
            max_score = min(max_score, move[3])
            continue # We opened all the valves that do anything, nothing left to do
        if move[0] == LIMIT:
            max_score = min(max_score, move[3])
            continue # out of time
            
        if move[1] in valuable and move[1] not in move[2].split(','):
            # We can open valve
            moves.put((move[0] + 1, move[1], ','.join(sorted(move[2].split(',') + [move[1]])), move[3] - (30 - (move[0] + 1)) * c[move[1]][0]))
        

        for neigh in c[move[1]][1]:
            moves.put((move[0] + 1, neigh, move[2], move[3]))
    #print(visited)
    return max_score

import time

def DFS2():
    LIMIT = 26
    moves = PriorityQueue()
    moves.put((0, 'AA,AA', '', 0))
    max_score = 0
    max_steps = len(c)*(len(c)+1)/2 * 2**len(valuable)
    step = 0
    visited = set()
    start_time = time.time()
    while not moves.empty():
        move = moves.get()
        if hashit(move) in visited:
            continue
        visited.add(hashit(move))
        max_score = min(max_score, move[3])

        step += 1
        if step % 100000 == 0:
            print("[{:.2f}] Step {} of {}, max_score: {}, len moves: {}, current_move: {}".format(
                time.time() - start_time,
                step,
                max_steps,
                max_score,
                moves.qsize(),
                move))
        if move[2] == valuable:
            continue # We opened all the valves that do anything, nothing left to do
        if move[0] == LIMIT:
            continue # out of time

        remaining_v = set(valuable) - set(move[2])
        remaining_p = sum(c[x][0] for x in remaining_v) * (LIMIT - (move[0] + 1))
        if move[3] - remaining_p > max_score:
            continue # Even if we were to open all remaining valves right now, we wouldn't beat high score, skip it

        p0,p1 = move[1].split(',')
        def get_moves(pos, valves):
            res=[(neigh, [], 0) for neigh in c[pos][1]]

            if pos in valuable and pos not in valves:
                res.append((pos, [pos], c[pos][0]))
            return res
        p0_moves = get_moves(p0, move[2].split(','))
        p1_moves = get_moves(p1, move[2].split(','))


        for m0 in p0_moves:
            for m1 in p1_moves:
                if m0[0] == m1[0] and m0[2] != 0 and m1[2] != 0:
                    # Both try to open valve in the same place, illegal move
                    continue
                moves.put((move[0] + 1,
                           ','.join(sorted([m0[0],m1[0]])),
                           ','.join(sorted(move[2].split(',') + m0[1] + m1[1])),
                           move[3] - (LIMIT - (move[0] + 1)) * (m0[2] + m1[2])))

    #print(visited)
    return max_score
