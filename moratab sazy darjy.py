l = [-2, 2, 10, 100, 200, 320]
a = int(input())
n = len(l)
l.append(a)
for i in range(n):
    if(l[n-i] < l[n-i-1]):
        l[n-i], l[n-i-1] = l[n-i-1], l[n-i]
    else:
        break
print(l)
