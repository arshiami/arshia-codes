
seconds = int(input("Enter the seconds you passed from your day:"))
if seconds > 86400:
    print("Error!can't make a true time")
hours = seconds // 3600
b1 = seconds % 3600
minutes = b1 // 60
b2 = b1 % 60
seconds02 = b2
print("Time:{}:{}:{}".format(hours, minutes, seconds02))
