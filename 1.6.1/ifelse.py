### This is mostly a code from "AreWeThereYet.py" with a slight fun modifacation. ###
from time import sleep
AreWeThereyetstat = False
def AreWeThereyet():
  AreWeThereyet = input("Are we there yet? (Yes,No)")
  if AreWeThereyet == "Yes" or AreWeThereyet == "yes" :
    print ("WOOOOOOOOO")
    AreWeThereyetstat = True
    quit()
  elif AreWeThereyet == "no" or AreWeThereyet == "No":
    print ("Then when?")
    AreWeThereyetstat = False
  elif AreWeThereyet == "Sir you are drunk" or AreWeThereyet == "Are you drunk?" :
    sleep(5)
    print("Police officer pulls up behind the car and comes over to your driver. Police officer proceds to conduct a breath test on the driver.")
    sleep(5)
    print("beep beep - \"machine\"")
    sleep(2)
    print ("I am sorry sir, but you are over the legal limit.  You must now accompany me to the station")
    AreWeThereyetstat = True
    quit()
  else:
    print("Thats not a bloody anwser, ya Jeremy Clarkson looking fool!")
    AreWeThereyetstat = False

while AreWeThereyetstat == False:
  AreWeThereyet()