import random
from words import words_list
gameovercondition = False
chances = 0
right = []
wrong = []
letter = random.choice(words_list)

while gameovercondition == False:
    guess = input("Enter a letter")
    if guess in letter:
        right.append(guess)
        print("Right")
        print(right)
        chances += 1
        print(chances)
    else:
        wrong.append(guess)
        print("Wrong")
        print(wrong)
        chances += 1
        print(chances)
        

    if chances > 12:
        print("Out of chances")
        print(letter)
        gameovercondition = True


