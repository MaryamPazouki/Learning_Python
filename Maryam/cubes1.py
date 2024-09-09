import sys
# the variable i is not mutable, that is why we can't change it in the main function 
# the output of the function is None, because we are not returning anything

def cube(i):
    i = i**3
    
    # return i
    # return i**3  # this is the better way to do return, because it take less memory


n = int(sys.argv[1])

for i in range(1, n+1):
    print("%s %s" %(i, cube(i)))