n = int(input())
l = []
ans = []
for i in range (n):
    tmp = int(input())
    l.append(tmp)
for i in range(n):
    mini = l[0]
    index = 0
    for j in range(len(l)):
        if (mini > l[j]):
            mini = l[j]
            index = j
    ans.append(mini)
    del l[index]
    print("l:" ,l)
    print("ans:", ans)
