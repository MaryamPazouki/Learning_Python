import sys
import matplotlib.pyplot as plt
import random

n = int(sys.argv[1])

cx = [0 , 0, 0.500]
cy = [0, 1, 0.866]

x, y = 0,0
x_points = []
y_points = []

for i in range(n):
    r = random.randrange(0,3)
    x = (x + cx[r]) /2.0
    y = (y +  cy[r]) / 2.0
    x_points.append(x)
    y_points.append(y)

plt.scatter(x_points, y_points, s=0.1, c='red')
plt.show()