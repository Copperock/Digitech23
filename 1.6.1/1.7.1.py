def ty():
  ##AreWeThereYet.py loop code def start##
    global AreWeThereyetstat
    AreWeThereyetstat = False

    def AreWeThereyet():
        global AreWeThereyetstat
        AreWeThereyet = input("Are we there yet? (Yes/No)")
        if AreWeThereyet.lower() == "yes":
            print("WOOOOOOOOO")
            AreWeThereyetstat = True
            quit()
        elif AreWeThereyet.lower() == "no":
            print("Then when?")
            AreWeThereyetstat = False
        else:
            print("That's not a bloody answer, ya Jeremy Clarkson looking fool!")
            AreWeThereyetstat = False

    while not AreWeThereyetstat:
        AreWeThereyet()

ty()
##AreWeThereYet.py loop def run##

def ie():
  ## ifelse with a certain output from a hidden input to achive desired result from work/task set def start##
    ### This is mostly a code from "AreWeThereYet.py" with a slight fun modifacation.     ###
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
    elif AreWeThereyet == "Sir you are drunk" or AreWeThereyet == "Are you drunk?" or AreWeThereyet == "911" or AreWeThereyet == "111" or AreWeThereyet == "are you drunk?" or AreWeThereyet == "are you drunk" :
      sleep(3)
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

ie()
## ifelse with a certain output from a hidden input to achive desired result from work/task set def run##