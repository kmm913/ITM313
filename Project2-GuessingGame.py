#import necessary packages
import random
import time  

#declare variables
randomNum = 0
userNum = 0
numberOfAttempts = 0
numberOfGuesses = 0
timeLimit = 10

#create timer function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time is up!')

#assign random number to variable
randomNum = random.randint(1,20)

#welcome user and explain the rules of the game
print("Welcome to the Guessing Game!\nYou have five attempts to guess a randomly generated number between 1 and 20. Good luck.")

#initialize timer
start = time.time()

#logic to control the game. If/else statements nested inside a while loop.
while time.time() - start < 25:  
    if numberOfAttempts < 5:
        userNum = int(input("Please guess a number: "))
        if userNum == randomNum:
            print ("Congratulations! You win!")
            break
        elif userNum != randomNum:
            numberOfAttempts += 1
            print ("Sorry, that is incorrect.")
        if (numberOfAttempts == 5 and userNum != randomNum):
            print ("You lose. But don't worry, your mom still loves you. Probably...")
            break
        elif time.time() - start >= 25:
            print ("Time is up! You really needed more than 25 seconds for this? Shame.")
            break

