with open('6.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

c = b[0]

def find_n(c, n):
    for i in range(len(c) - n):
        x = set(c[i:i+n])
        if len(x) == n:
            return i + n

print(find_n(c, 4))
print(find_n(c, 14))
