"""This file is a number guessing game that is slowly being made."""
# Title: iter3
# Creater: Caleb Young
# Current iteration: 3
# StartDate: 2/5/23
# FinishDate:30/5/23
# Description: This is a file that is apart of a
# Description p2: set of files that will in the end
# Descriptin p3: hopefullly contain a lovley polished game that works well.

# random stuff that I just need to do
import random
# Variables
randintend = 21
attempt = 4


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
            break
        else:
            print(f'Try again! {attempt} attempts left.')
            attempt -= 1
            continue


# replay loop
replayloop = True


def replaysys():
    """Replay loop return yes or no info."""
    global replayloop
    print("Would you like to play again?")
    replay_input = input("Y,N    ").lower()

    if replay_input == "y":
        print("Let's play again")
        replayloop = True
        gameengineandlives()
    elif replay_input == "n":
        print("Goodbye")
        replayloop = False
    else:
        print("Please input Y or N")
        replayloop = False
        replaysys()

# Please run well


def plsrun():
    """Do a run command to run the game."""
    global attempt
    attempt = 4
    gameengineandlives()
    replaysys()


plsrun()

# replayloop
while replayloop:
    plsrun()
