#Title: iter2
#Creater: Caleb Young
#Current iteration: 2
#StartDate: 5/1/23
#FinishDate: 
#Description: This is a file that is apart of a set of files that will in the end hopefullly contain a lovley polished game that works well.

#importing stuff
import random

#Variables
randintstart = 0
randintend = 21
attempt = 4

#game engine/attempts
def gameEngineAndLives():
  global attempt
  a = random.randint(randintstart,randintend)
  print("Welcome to the random number guessing game. This is a game where you guess a number betwen the value of 0 and 20.")
  for i in range(attempt + 1):
      user_input = int(input("Enter Number: "))
  
      if user_input == (a):
          print('You won!')
          break
      else:
          print(f'Try again! {attempt} attempts left.')
          attempt -= 1
          continue
  
  
gameEngineAndLives()