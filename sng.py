import random
items = ['stone','paper','scissor']
cc = random.choice(items)
counter_cc = 0
counter_uc = 0
print("1-stone")
print("2-paper")
print("3-scissor")
while counter_cc != 5 and counter_uc != 5:
    uci = int(input())-1
    uc = items[uci]
    print("user choice:",uc)
    print("computer choice:",cc)
    if cc == "stone" and uc == "scissor" or cc == "scissor" and uc == "paper" or cc == "paper" and uc == "stone":
        counter_cc += 1
        print(counter_cc)
        print("comupter won this round")      
    elif uc == "stone" and cc == "scissor" or uc == "scissor" and cc == "paper" or uc == "paper" and cc == "stone":
        counter_uc += 1
        print("user won this round")
    else:
        print("this round didn't have winner")
if counter_cc == 5:
    print("computer won the game")
if counter_uc == 5:
    print("user won the game")
