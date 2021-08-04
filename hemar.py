print("Welcome to the (triangle maker)")
a = float(input("Enter the first flank:"))
b = float(input("Enter the second flank:"))
c = float(input("Enter the third flank:"))
max = max(a, b, c)
min = min(a, b, c)
middle = 0
if a > b > c or c > b > a:
    middle = b
if a > c > b or b > c > a:
    middle = c
if b > a > c or c > a > b:
    middle = a
if middle + min > max:
    print("You entered a true triangle")
else:
    print("Your triangle was false,pay attention to Hemar's rule.")
