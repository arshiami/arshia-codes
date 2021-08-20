import random
true_chars = []
words = ["tree", "beach","clock","apple","book","android","python"]
word = random.choice(words)
score = len(word)
for i in range(len(word)):
    print("-",end = " ")

while score != 0:
    char = input("\nPlease enter the character:")
    if char in word:
        true_chars.append(char)
        print("Score:",score)
    else:
        score = score - 1
        print("Score:",score)

    if len(word) == len(true_chars):
        print("You won!, you quesssed all the letters of {} truely.".format(word))
        break
    if score == 0:
        print("game over.The word was {}".format(word))
        break

