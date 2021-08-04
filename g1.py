import random
list1 = []
o = 0
n = int(input("Enter the lenght of list:"))
max = int(input("Enter the maximum of your list:"))
if n > max:
    print("Can't make a list, try again")
    n = int(input("Enter the lenght of list:"))
    max = int(input("Enter the maximum of your list:")) 
while len(list1) != n:
    numbers = random.randint(0, max)
    if numbers in list1:
        continue
    list1.append(numbers)
print(list1)
