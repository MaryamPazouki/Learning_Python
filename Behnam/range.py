a = list(range(1, 11))
print(a)
n = len(a)
for i in range(n // 2):
    temp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = temp
print(a)
