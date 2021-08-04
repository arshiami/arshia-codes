import random
computer_number = random.randint(0, 20)
user_number = -1
talash = 0
while True:
    talash += 1
    user_number = int(input())
    if computer_number == user_number:
        print("barikala, you tried:",talash)
        break
    elif computer_number > user_number:
        print("boro bala")
    elif computer_number < user_number:
        print("boro paeen")
