import sys
import random

count = int(sys.argv[1])
n = int(sys.argv[2])
deadend = 0

for j in range(count):
    a = [[False] * n for i in range(n)]
    x = n // 2
    y = n // 2
    while 0 < x < n -1 and 0 < y < n - 1:
        if a[x][y+1] and a[x][y-1] and a[x-1][y] and a[x+1][y]:
            deadend += 1
            break
        a[x][y] = True
        r = random.random()
        if r < 0.25:
            if not a[x - 1][y] : x -= 1
        elif r < 0.5:
            if not a[x + 1][y] : x += 1
        elif r < 0.75:
            if not a[x][y - 1] : y -= 1
        else:
            if not a[x][y + 1] : y += 1
print(100 * deadend // count)