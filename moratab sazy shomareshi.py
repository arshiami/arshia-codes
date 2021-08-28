n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

b = []
for i in range(12):
    b.append(0)

for i in range(n):
    b[l[i]+5] = b[l[i]+5]+1

l = []
for i in range(11, -1, -1):
    for j in range(b[i]):
        l.append(i-5)
print(l)
