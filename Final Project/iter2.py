#Title: iter2
#Creater: Caleb Young
#Current iteration: 2
#StartDate: 5/1/23
#FinishDate: 
#Description: Hopefully a file of which will contain the first version of a number guessing game that I will create.


#game engine/lives
import random
a = random.randint(0,20)
print("Welcome to the random number guessing game. This is a game where you guess a number betwen the value of 0 and 20.")
attempt = 4
for i in range(5):
    user_input = int(input("Enter Number: "))

    if user_input == (a):
        print('You won!')
        break
    else:
        print(f'Try again! {attempt} attempts left.')
        attempt -= 1
        continue