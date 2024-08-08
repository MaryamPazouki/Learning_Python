import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

s = a + b
diff = a - b
p = a * b
q = a // b
h = a ** b
r = a % b

print(str(a) + (' + ') + str(b) + (' = ') + str(s))
print(str(a) + (' - ') + str(b) + (' = ') + str(diff))
print(str(a) + (' * ') + str(b) + (' = ') + str(p))
print(str(a) + (' / ') + str(b) + (' = ') + str(q))
print(str(a) + (' % ') + str(b) + (' = ') + str(r))
print(str(a) + (' ** ') + str(b) + (' = ') + str(h))
