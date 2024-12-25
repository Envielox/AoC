input_file="inp2.txt"
sample_file="sample2.txt"

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

b= [ [int(elem,10) for elem in x.split()] for x in a]

def isSafe(l):
    if l != sorted(l) and l[::-1] != sorted(l):
        return False
    diffs = [abs(l[i] - l[i+1]) for i in range(len(l)-1)]
    if max(diffs) > 3:
        return False
    if min(diffs) < 1:
        return False
    return True

def pd(l):
    if isSafe(l):
        return True
    for i in range(len(l)):
        if isSafe(l[:i] + l[i+1:]):
            return True
    return False

c = [1 if isSafe(x) else 0 for x in b]
d = [1 if pd(x) else 0 for x in b]

print(sum(c))
print(sum(d))
