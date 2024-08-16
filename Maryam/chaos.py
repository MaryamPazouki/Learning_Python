import sys
import dudraw
import random

n = int(sys.argv[1])

cx = [0 , 0, 0.500]
cy = [0, 1, 0.866]

x, y = 0,0

for i in range(n):
    r = random.randrange(0,3)
    x = (x + cx[r]) /2.0
    y = (y +  cy[r]) / 2.0
    dudraw.set_pen_color_rgb(255, 0, 0)
    dudraw.point(x,y)
    dudraw.show(0)

dudraw.show()


