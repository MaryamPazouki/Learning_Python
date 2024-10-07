n = 0
m = 3
row =  [0] * m
col = []
col2 = []
col3 = []

for i in range (m):
    for j in range (m):
        row[j] = n
        n += 1
    col.append(row[:])
    col2.append(row[:])

for i in range (m):
    for j in range (m):
            row[j] = col[i][j] * col2[i][j]
    col3.append(row[:])
  
for i in range (m):
    for j in range (m):
        print (col[i][j], end = " ")
    print()

for i in range (m):
    for j in range (m):
        print (col2[i][j], end = " ")
    print()

for i in range (m):
    for j in range (m):
        print (col3[i][j], end = " ")
    print()
