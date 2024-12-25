input_file="inp1.txt"
sample_file="sample1.txt"

def parse_lines(fi):
    with(open(fi) as f) :
        return f.read().split('\n')[:-1]

a = parse_lines(input_file)
# Comment out to run actual solution
#a = parse_lines(sample_file)

b=[x.split() for x in a]
c=sorted([(int(x[0], 10)) for x in b])
d=sorted([(int(x[1], 10)) for x in b])

e = list(map(lambda a: abs(a[0]-a[1]), zip(c,d)))
print(sum(e))

from collections import Counter
cnt = Counter(d)

f=list(map(lambda x: cnt[x]*x, c))
print(sum(f))

