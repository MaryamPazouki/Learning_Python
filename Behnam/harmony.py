import sys

total = 0
n = int(sys.argv[1])
for i in range(1, n + 1):
	total += 1 / i
print ("total = " + str(total))