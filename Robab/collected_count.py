import sys
import random
if __name__=='__main__':
    n=int(sys.argv[1])
count=0
collected_count=0
is_collected=[False]*n

while collected_count <n:
    count+=1
    value=random.randrange(0,n)
    if not is_collected[value]:
        collected_count+=1
        is_collected[value]=True
print(count)
