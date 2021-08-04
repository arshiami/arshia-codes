a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
bmm = 0
max = max(a, b)
min = min(a, b)
for i in range(1, min + 1):
    if max % i == 0 and min % i == 0:
        bmm = i
print("The B.M.M is:", bmm)
