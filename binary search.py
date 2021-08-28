n = int(input())
l = []
for i in range(n):
    l.append(int(input())

a = int(input())

start = 0
end = n-1
while(start<=end):
    mid = (start+end)//2
    if(a == l[mid]):
        print(mid)
        break
    elif(a > l[mid]):
        start = mid+1
    else:
        end = mid-1
