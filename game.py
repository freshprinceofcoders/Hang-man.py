import random
from words import Test_list
gameovercondition = False
chances = 0
right = []
wrong = []
word = random.choice(Test_list)
print(word)
while gameovercondition == False:
    guess = input("Enter a letter: ")

    # letterCountInTheWord = word.count(guess)
    # print(letterCountInTheWord)
 
    # letterCountInTheRightArray = right.count(guess)
    # print(letterCountInTheRightArray)


    if word.count(guess) > right.count(guess):
        if guess in word:
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
        print(word)
        gameovercondition = True


