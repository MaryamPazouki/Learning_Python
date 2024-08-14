import sys
import random

n = int(sys.argv[1])

for i in range(n):
    print(random.random())

# generat data .txt and the output of this file will be saved in data.txt
# python randomseq.py 100 > data.txt


# the output of this file will be piped with next function sort
# python randomseq.py 100 | sort

#the output of this file will be piped with next function more abd show page to page
#python randomseq.py 100 | more

# next page Tab
# stop ctrl + z
