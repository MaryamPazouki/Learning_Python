import sys
import stdio, stdin

total = 0
count = 0
while not stdio.isEmpty():
    value = stdio.readfloat()
    total += value
    count += 1

print('average = ' + (total // count))