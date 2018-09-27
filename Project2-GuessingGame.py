#import necessary packages
import random
import time
import signal  

#declare variables
randomNum = 0
userNum = 0
numberOfAttempts = 0
numberOfGuesses = 0

#defne alarm function to interrupt loop if time expires
def timeout_handler(signal, frame):
    raise Exception("Time is up!")
signal.signal(signal.SIGALRM, timeout_handler)

#assign random number to variable
randomNum = random.randint(1,20)

#welcome user and explain the rules of the game
print("Welcome to the Guessing Game!\nYou have five attempts and 25 seconds to guess a randomly generated number between 1 and 20. Good luck.")

#initialize timer
start = time.time()

signal.alarm(25)
#logic to control the game. If/else statements nested inside a while loop.
try:
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
                print ("Time's up! You really needed more than 25 seconds for this? Shame.")
                break

except:
    print("Time's up! You really needed more than 25 seconds for this? Shame.")