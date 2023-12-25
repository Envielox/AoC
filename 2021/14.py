with open('14.in') as f:
    a = [x[:-1] for x in f.readlines()]

from collections import defaultdict

start = a[0]
trans = {}
for x in a[2:]:
    s,t = x.split(' -> ')
    trans[s] = t

def step(s):
    res = ""
    for i in range(len(s) - 1):
        x = s[i] + s[i+1]
        t = trans[x]
        res += s[i] + t
    res += s[-1]
    return res

z = start
for i in range(10):
    z = step(z)

freq = defaultdict(int)
for l in z:
    freq[l] += 1


print(max(freq.values()) - min(freq.values()))

start_2 = defaultdict(int)
for i in range(len(start)-1):
    start_2[start[i] + start[i+1]] += 1

def smart_step(ss):
    res = defaultdict(int)
    for k, v in ss.items():
        t=trans[k]
        res[k[0] + t] += v
        res[t + k[1]] += v
    return res

def smart_freq(ss):
    freq = defaultdict(int)
    for k,v in ss.items():
        freq[k[0]] += v
    freq[start[-1]] += 1
    return freq


z = start_2.copy()
for i in range(10):
    z = smart_step(z)

freq = smart_freq(z)

print(max(freq.values()) - min(freq.values()))

for i in range(30):
    z = smart_step(z)

freq = smart_freq(z)

print(max(freq.values()) - min(freq.values()))
