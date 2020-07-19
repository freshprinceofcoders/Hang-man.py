import random
from words import Test_list
gameovercondition = False
chances = 0
right = [''] * 6
wrong = [] 
word = random.choice(Test_list)
print(word) 
separator = ''

while gameovercondition == False:
    if separator.join(right) == word:
        print("Congrats you win!!!!!!!!!!!!")
    guess = input("Enter a letter: ")
    if len(guess) < 2:
        if word.count(guess) > right.count(guess):#with word count when you guess a letter from the random it will count the number of letters you have inputed that are in the word and with the right it will count the number in the array
            letPos = [i for i, ltr in enumerate(word) if ltr == guess]
            #print(letPos)

            for let in letPos:
               # print(let)
                if(right[let]==''):
                #    print("i am here")
                    right[let]=guess
                    break
                   # if(let.find()>1):
                    #    print(let)

                        
                        
            # letPos = word.find(guess)#finds the position of the letter in the word
            # right[letPos] = guess # assigning thenright array position to the guess so the letters go in the right place

            print("Right")
            print(separator.join(right))
            chances += 1
            print(f"Chance:{chances}")

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
    else:
        print("You can only input on letter")

for n in range(len(word)):
    if word[n] == letPos:
        letPos.append(n)




