n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

a = int (input())
for i in range(n):
    if(l[i] == a):
        print(i)
