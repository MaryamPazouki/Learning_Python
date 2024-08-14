import stdio

total = 0.0
count = 0

while not stdio.isEmpty():
    value = stdio.readFloat()
    total += value
    count +=1
print('verage value is %.2f' %(total / count))