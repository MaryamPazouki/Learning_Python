import random
import sys

n = int(sys.argv[1])

count = 0
collectedCount = 0
isCollected = [False] * n

while collectedCount < n:
    print(isCollected)
    count += 1
    coupon = random.randrange(0, n)
    if not isCollected[coupon]:
        isCollected[coupon] = True
        collectedCount += 1
print(count)