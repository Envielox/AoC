import time
def timeit(f, *args):
    start = time.time()
    res = f(*args)
    end = time.time()
    print("it took {:.2f} sec".format(end-start))
    return res

with open('20.in') as f:
          a = f.read()

b = a.split('\n')[:-1]

