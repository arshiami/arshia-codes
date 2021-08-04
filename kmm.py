a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
kmm = 0
max = max(a, b)
min = min(a, b)
for i in range(max, a*b+1):
    if i % max == 0 and i % min == 0:
        kmm = i
        break
print("The K.M.M is:", kmm)
