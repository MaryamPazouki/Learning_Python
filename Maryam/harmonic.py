import sys
import stdio

def harmonic(n,r = 2):
    total =0
    for i in range(1, n+1):
        total += 1/i**r
    return total

for i in range(1, len(sys.argv)):
    arg = int(sys.argv[i])
    value1 = harmonic(arg, r= 2)
    value2 = harmonic(arg, 2)
    value3 = harmonic(arg)

    stdio.write(value1)
    stdio.write(value2)
    stdio.write(value3)