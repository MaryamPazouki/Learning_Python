%%python - 10 20 10000

import sys
import random
if __name__=='__main__':
    stake=int (sys.argv[1])
    goal=int(sys.argv[2])
    trial=int(sys.argv[3])
wins=0
bets=0
for t in range(trial):
    cash=stake
    while 0<cash <goal:
        bets+=1
        if random.randrange(0,2) ==0:
            cash+=1
        else:
            cash-=1
    if cash== goal:
        wins+=1
print(str(100*wins//trial))
print(str(bets//trial))
