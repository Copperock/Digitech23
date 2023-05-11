#Title: iter3
#Creater: Caleb Young
#Current iteration: 3
#StartDate: 5/2/23
#FinishDate: 
#Description: This is a file that is apart of a set of files that will in the end hopefullly contain a lovley polished game that works well.

#random stuff that I just need to do
replayLoop = False
import random

#Variables
randintend = 21
attempt = 4

#welcome
def welcome():
  print("Welcome to the random number guessing game. This is a game where you guess a number betwen the value of 0 and 20.")

#game engine/attempts
def gameEngineAndLives():
  global attempt
  a = random.randint(0,randintend)
  for i in range(attempt + 1):
      user_input = int(input("Enter Number: "))
  
      if user_input == (a):
          print('You won!')
          break
      else:
          print(f'Try again! {attempt} attempts left.')
          attempt -= 1
          continue


#replay loop?
  def replaySYS():
    global replayLoop
    print("Now that we have finished that, would you like to play again?")
    replay_input = input("Y,N    ").lower()
    
  
    if replay_input == "y":
      print("Let's play again")
      replayLoop = False
      gameEngineAndLives()
    
    else:
      print("Goodbye")
      replayLoop = True
    
  while replayLoop == False:
    gameEngineAndLives()
    replaySYS()

#PLs work well
def plsrun():
  welcome()
  gameEngineAndLives()
  replaySYS()


plsrun()