with(open('inp12.txt') as f) :
     raw=f.read()

raw2 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

a = raw[:-1].split('\n')

b = [(x.split(' ')[0], list(map(int, x.split(' ')[1].split(',')))) for x in a]

def matches(pattern, elems):
    for elem in zip(pattern, elems):
        if elem == ('.', '#') or elem == ('#', '.'):
            return False
    return True

def generate(pattern, desc, prev_pattern = ''):
    if desc == []:
        remain = '.' * len(pattern)
        s = 1 if matches(pattern, remain) else 0
        #print((prev_pattern + remain, s, pattern))
        
        return s
    e = desc[0]
    remain = sum(desc) - 1 + len(desc) - 1
    score = 0
    for i in range(len(pattern) - remain):
        elem = '.' * i + '#' * e + ('.' if len(desc) != 1 else '')
        if matches(pattern, elem):
            score += generate(pattern[len(elem):], desc[1:], prev_pattern=prev_pattern+elem)
        #print((prev_pattern+elem, score))
    return score


def generate2(pattern, desc):
    # IDEA: dynamic programming, answer "in how many ways we could be in this position
    # @ each index in pattern we have mapping "position in desc" -> "numbe rof popssible layouts"

    mapping = [ [0 for __ in range(len(desc) + 1)] for _ in range(len(pattern)+1)]
    mapping[0][0] = 1
    
    for p in range(len(pattern)):
        #print(p, mapping[p])
        if pattern[p] in '.?':
            # Nothing changes we are in the same position
            for k, v in enumerate(mapping[p]):
                mapping[p+1][k] += v
                
        if pattern[p] in '#?':
            # We need to advance desc
            for k, v in enumerate(mapping[p]):
                if k == len(desc):
                    continue
                elem = '#'*desc[k] + ('.' if k != len(desc)-1 else '') 
                if p + len(elem) <= len(pattern):
                    mapping[p + len(elem)][k+1] += v if matches(pattern[p:],elem) else 0

    #print(mapping)
    return mapping[len(pattern)][len(desc)]



c = [((x[0] + '?') * 4 + x[0], x[1] * 5) for x in b]

def results():
    total = 0
    for elem in b:
        dt = generate2(elem[0], elem[1])
        #print(elem, dt)
        total += dt
        
    print(total)

    total = 0
    for i, elem in enumerate(c):
        dt = generate2(elem[0], elem[1])
        print((i, elem, dt))
        total += dt
        
    print(total)

#results()
