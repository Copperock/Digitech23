"""This file is a number guessing game that is slowly being made."""
# Title: iter4
# Creater: Caleb Young
# Current iteration: 4
# StartDate: 30/5/23
# FinishDate:
# Description: This is a file that is apart of a
# Description p2: set of files that will in the end
# Descriptin p3: hopefullly contain a lovley polished game that works well.

# random stuff that I just need to do
import random
# Variables
randintend = 101
attempt = 4
game_play = True


def gameengineandlives():
    """Return lives left and run game engine."""
    user_input = ""
    global attempt
    a = random.randint(0, randintend)
    for i in range(attempt + 1):
        try:
            user_input = int(input("Enter Number: "))
        except ValueError:
            print("Invaild input. Please input a number")

        if user_input == (a):
            print('You won')
            break

        elif user_input >= (a):
            print("Lower")
            continue
            
        elif user_input <= (a):
            print("Higher")
            continue
            
        else:
            print(f'Try again! {attempt} attempts left.')
            attempt -= 1
            continue

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
        replayloop = True
        replaysys()
    

while game_play == True:
    gameengineandlives()
    if replayloop == True:
        game_play == True

    else:
        game_play == False
        print("Thanks for particapating in this show :)")