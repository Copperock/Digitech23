# Title: iter4
# Creater: Caleb Young
# Current iteration: 4
# StartDate: 110523
# FinishDate:
# Description: This is a file that is apart of a set of files that will in the end hopefully contain a game that works well.

# random stuff that I just need to do
import random
# Variables
randintend = 21
attempt = 0+4
replayLoop = False

# welcome
def welcome():
    print(
        "Welcome to the random number guessing game. This is a game where you guess a number between the value of 0 and 20."
    )


# game engine/attempts
def gameEngineAndLives():
    global attempt
    a = random.randint(0, randintend)
    for i in range(attempt + 1):
        user_input = int(input("Enter Number: "))

        if user_input == (a):
            print('You won!')
            
        else:
            print(f'Try again! {attempt} attempts left.')
            attempt -= 1


# replay loop
def replaySYS():
    global replayLoop
    print("Now that we have finished that, would you like to play again?")
    replay_input = input("Y,N    ").lower()

    if replay_input == "y":
        print("Let's play again")
        replayLoop = False
        gameEngineAndLives()
    
    elif replay_input == "n":
        print("Goodbye")
        replayLoop = True

    else:
        print("Please input Y or N")
        replayLoop = False

    while replayLoop = True
    gameEngineAndLives()

# Please run well
def plsrun():
    welcome()
    gameEngineAndLives()
    replaySYS()

plsrun()
