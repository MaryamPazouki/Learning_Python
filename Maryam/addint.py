# first install stdio -> pip install stdio
import sys
import stdio

n = int(sys.argv[1])

total = 0
for i in range(n):
    total += stdio.readint()

print('sum is %s', total)