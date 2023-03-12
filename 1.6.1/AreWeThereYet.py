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
  else:
    print("Thats not a bloody anwser, ya Jeremy Clarkson looking fool!")
    AreWeThereyetstat = False

while AreWeThereyetstat == False:
  AreWeThereyet()