Hours = int(input("Enter the hours:"))
Minutes = int(input("Enter thr minutes:"))
Seconds = int(input("Enter the seconds:"))
if Hours > 23 or Hours < 0 or Minutes > 59 or Minutes < 0 or Seconds > 59 or Seconds < 0:
    print("Error: pay attention to clock's rules")
else:
    whole_seconds = (Hours*3600) + (Minutes*60) + (Seconds)
    print("You passed {} seconds of your day!".format(whole_seconds))
