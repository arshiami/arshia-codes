n = int(input())
l = []
for i in range (n):
    tmp = int (input())
    l.append(tmp)

for i in range(n-1):
    maxi = l[0]
    index = 0
    for j in range(n-i):
        if maxi < l[j]:
            maxi = l[j]
            index = j
    l[index] = l[n-1-i]
    l[n-1-i] = maxi
    print("l:",l)
    print()
