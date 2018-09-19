#import necessary packages
import random
import time  

#declare variables
randomNum = 0
userNum = 0
numberOfAttempts = 0
numberOfGuesses = 0

#assign random number to variable
randomNum = random.randint(1,20)
print(randomNum)

#welcome user and explain the rules of the game
print("Welcome to the Guessing Game. You have five attempts to guess a randomly generated number between 1 and 20. Good luck.")

#logic to control the game. If/else statements nested inside a while loop.
while numberOfAttempts < 5: 
    userNum = int(input("Please guess a number: "))
    if userNum == randomNum:
        print ("Congratulations! You win!")
        break
    elif userNum != randomNum:
        numberOfAttempts += 1
        print ("Sorry, that is incorrect.")

if(numberOfAttempts >= 5 and userNum != randomNum):
    print ("You lose. But don't worry, your mom still loves you. Probably...")