%%python - 5 
import sys
if __name__ == '__main__':
    n = int (sys.argv[1])
power=1
for i in range(n+1):
    print(str(i) + ' ' + str(power))
    power *=2
