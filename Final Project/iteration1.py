#Title: iteration1/number guessing game
#Creater: Caleb Young
#Current version: 0.1
#StartDate: 4/3/23
#FinishDate: 
#Description: Hopefully a file of which will contain the first version of a number guessing game that I will create.


#code start here
#import time, numbers etc
#Where I got a the colour from: https://www.geeksforgeeks.org/how-to-add-colour-to-text-python/
from time import sleep
import random

#greeting statment
print("Hello and welcome to my number guessing game!\n\nThis game will contain a list of numbers ranging from \"0\" to \"100\"\nOnly one of these numbers within the 100 possible anwsers will be the correct one.\n\nWhen you guess this number correctly you will win a wonderful prize of \"Completing this game!\"\n Well now, lets see. I should probably get to know your name?\n\nAfter all we are going to be here for quite a while well you guess this number.\n\n")
name = input("So what is your name?\n")

print(name + ", thats a nice name. ")