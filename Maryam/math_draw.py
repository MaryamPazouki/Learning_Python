# pip install dudraw
# change setXscale -> set_scale

import math
import dudraw
import sys

n = int(sys.argv[1])

x, y = [], []

for i in range(n + 1):
    x += [math.pi * i /n]
    y += [math.sin(4*x[i]) + math.sin(20 * x[i])]
dudraw.set_scale(0, math.pi)
dudraw.set_scale(-2.0, 2.0)

for i in range(n):
    dudraw.line(x[i], y[i], x[i+1], y[i+1])

dudraw.show()