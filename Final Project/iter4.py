"""This file is a number guessing game that is slowly being made."""
# Title: iter4
# Creater: Caleb Young
# Current iteration: 4
# StartDate: 30/5/23
# FinishDate:
# Description: This is a file that is apart of a
# Description p2: set of files that will in the end
# Descriptin p3: hopefullly contain a lovley polished game that works well.

# stuff to be imported
import random
# Variables
randintend = 20
randintstart = 0
attempt = 4
user_guesses = []

# welcome


print("""Welcome to the random number guessing game.
This is a game where you guess a number""",
f"between the value of 0 and {randintend}.")

# game engine and attempts


def gameengineandlives():
    """Return lives left and run game engine."""
    user_input = ""
    global attempt
    a = random.randint(randintstart, randintend + 1)
    for i in range(attempt + 1):
        while user_input != int():
            try:
                user_input = int(input("Enter Number: "))
                break
            except ValueError:
                print("Invaild input. Please input a number")

        if user_input == (a):
            user_guesses.append(user_input)
            print('You won')
            attempt = 0
            break

        elif user_input >= (randintend):
            print(f"please guess within range {randintstart,randintend}")

        elif user_input <= (randintstart):
            print(f"Please guess within range {randintstart,randintend}")

        elif user_input >= (a):
            print(f"Lower than {user_input}")
            print(f'Try again! {attempt} attempts left.')
            user_guesses.append(user_input)
            attempt -= 1

        elif user_input <= (a):
            print(f"Higher than {user_input}.")
            print(f'Try again! {attempt} attempts left.')
            user_guesses.append(user_input)
            attempt -= 1

        else:
            print('Invalid input, please try again.')

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
        del user_guesses[:]
        replayloop = True
        gameengineandlives()
    elif replay_input == "n":
        print("Goodbye")
        replayloop = False
    else:
        print("Please input Y or N")
        replayloop = True
        replaysys()

# Please run well


def plsrun():
    """Do a run command to run the game."""
    global attempt
    attempt = 4

    gameengineandlives()

    print(f'You guessed {user_guesses}')

    replaysys()


plsrun()


# replayloop
while replayloop:
    plsrun()
