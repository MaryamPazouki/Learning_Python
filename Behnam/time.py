import time
import random

n = 10000000
a = []
t0 = time.time()
for i in range(n):
    a += [random.random()]
t1 = time.time()
print(t1 - t0)

t0 = time.time()
a = [random.random for i in range(n)]
t1 = time.time()
print(t1-t0)