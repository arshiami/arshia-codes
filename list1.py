import random
list01 = []
for i in range(20):
    number_s = int(input("Enter your numbers:"))
    list01.insert(i, number_s)
for i in range(20):
    list01[i] = list01[i] ** 2
    max1 = max(list01)
    min1 = min(list01)
print("Your list:{}, Maximum of your list:{}, Minimun of your list:{}".format(list01, max1, min1))
