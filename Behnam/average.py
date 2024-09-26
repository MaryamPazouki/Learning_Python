total = 0.0
a = list(range(1, 9))

for i in range(len(a)):
    total += a[i]
print("average = " + str(total // len(a)))



total = 0.0
for v in a:
    total += v
print("average = " + str(total // len(a)))


print ('average = ' + str(float(sum(a) // len(a))))