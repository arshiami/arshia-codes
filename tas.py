import random
answer = input("write (start) to begin the game:")
if answer == "start":
    number = random.randint(1, 6)
    print(number)
    if number == 6:
        answer1 = input("You are a lucky person! Type (continue) to roll the prize round:")
        if answer1 == "continue":
            number = random.randint(1, 6)
            print(number)  
else:
    exit
