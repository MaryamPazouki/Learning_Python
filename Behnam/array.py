suits = ['clubs', 'diamonds', 'spades', 'heart']

x = [ 0.03, 0.5, 0.9]
y = [ 0.8, 0.3, 0.07]

n = len(x)

total = 0

for i in range (n):
    total += x[i] * y[i]
print(('total = ') + str(total))
