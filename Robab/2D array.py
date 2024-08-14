m=10
n=3
a=[]
for i in range(m):
    row=[0]*n
    a+=[row]
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
