#x = [3,2,1,1,2,3] #6 counts
# i = 0

# for i in range(len(x)):
#     print(x[i])
# print i iteration (index)
# print x[i] priting mo yung index nung x na un

# for i in enumerate(x):
#     print(i)
# this will print each index with value

# for i, element in enumerate(x):
#     print(i, element)
# same for this but no ()


# while i < 10:
#     print("runn")
#     i += 1
# run print while i < 10

# while True:
#     print("runn")
#     i += 1
#     if i == 10:
#         break

# This is a simple number guessing game.
# The computer will randomly select a number between 1 and 10.
# Your task is to guess the correct number.
# The program will give you hints if your guess is too high or too low.
# It will continue to prompt you until you guess the correct number.
# Let's get started!

import random
userInput = int(input("Guess the number from 1 to 10: "))
choices = [1,2,3,4,5,6,7,8,9,10]
choicesLen = random.randint(0, len(choices)-1) # 0 to 10-1, 0 to 9 (total index)
bot = choices[choicesLen]
print(bot)


while True:
    
    if userInput == bot:
        print("Correct\n")
        playAgain = input("Would you like to play again? Y/N: ")

        if playAgain == "Y" or "y":
            userInput = int(input("Guess the number from 1 to 10: "))
            choicesLen = random.randint(0, len(choices)-1) # add this so we can have a new index
            bot = choices[choicesLen]
        
        else:
            break
            

    elif userInput > bot:
        print("Lower")
        userInput = int(input("Try again: "))


    elif userInput < bot:
        print("Higher")
        userInput = int(input("Try again: "))

    else:
        break