"""This file contains a partially complete guessing game."""
# Title: iter4
# Creater: Caleb Young
# Current iteration: 4
# StartDate: 180523
# FinishDate:
# Description: A partially completed number guessing game

# random stuff that I just need to do
import random
# Variables
randintend = 21
attempt = 4
replayloop = True

# welcome


print("Welcome to the random number guessing game.")
print("This is a game where you guess a number between the value of 0 and 20.")


# game engine and attempts


def gameengineandlives():
    """Return lives left and run game engine."""
    global attempt
    a = random.randint(0, randintend)
    for i in range(attempt + 1):
        user_input = int(input("Enter Number: "))

        if user_input == (a):
            print('You won')
        else:
            print(f'Try again! {attempt} attempts left.')
            attempt -= 1


# replay loop


def replaysys():
    """Replay loop return yes or no info."""
    global replayloop
    global attempt
    print("Now that we have finished that, would you like to play again?")
    replay_input = input("Y,N    ").lower()

    if replay_input:
        print("Please input Y or N")
        replayloop = True
    elif replay_input == "y":
        print("Let's play again")
        replayloop = True
        gameengineandlives()
    else replay_input == "n":
        print("Goodbye")
        replayloop = False
# Please run well


def plsrun():
    """Do a run command to run the game."""
    gameengineandlives()
    replaysys()


plsrun()

# replayloop
while replayloop:
    plsrun()
