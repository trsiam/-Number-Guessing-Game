'''
Number Guessing Game:
 Write a program where the computer randomly selects a number, and
the user has to guess it. The program should give hints whether the guess is too high or too low.
'''

from termcolor import colored # FOR TERMINAL COLOR
from random import randint  # For  Random Value
import sys
temp_V=0                    # Variables 
temp_Vone=0
temp_Vtwo=0
temp_Vthree=0


def game():      # Main Game Logic function
    global temp_Vone,temp_Vtwo,temp_Vthree

    print()
    temp_Vone=randint(1,100)
    try:
        temp_Vtwo=int(input("Guess a number Betweeen 1 to 100--> "))   # Try catch exception 
    except ValueError:
        print(colored("Please Input a Number","red"))
        game()
    if(temp_Vone == temp_Vtwo):                     # If the numbers are same print Congratulation
        print("<------You have found the number------->",temp_Vone)
        print("Congratulation 🎊🎊")
    elif (temp_Vone < temp_Vtwo):                   # If the number is bigger than the random number 
        if(temp_Vone < temp_Vtwo  <=temp_Vone+10):
            print("You are Very close")
            print("The number is-->",temp_Vone)
        elif(temp_Vone < temp_Vtwo  <=temp_Vone+20):
                print("You are close but not so close")
                print("The number is-->",temp_Vone)
        else:
            print("You are far away")
            print("The number is-->",temp_Vone)
    elif (temp_Vone > temp_Vtwo):                   # If the number is smaller that the random number
        if(temp_Vone > temp_Vtwo  >=temp_Vone-10):
            print("You are Very close")
            print("The number is-->",temp_Vone)   
        elif(temp_Vone > temp_Vtwo  >= temp_Vone-20):
                print("You are close but not so close")
                print("The number is-->",temp_Vone)
        else:
            print("You are far away")
            print("The number is-->",temp_Vone)
    t=int(input("play Again  press 1  Return to menu press 2 -->"))
    if(t==1):
        game()
    if(t==2):
        what_to_Do()
    

def Exit():
    print("Exiting....")
    sys.exit()

def what_to_Do():                   # Main Menu function
    global temp_V
    print()
    print("1. 🎲Start Game")   
    print("2. 💢Exit")
    print()
    try:
        temp_V=int(input("What you want to Do---> "))    # Try catch exception 
    except ValueError:
        print(colored("Please Input a Number","red"))
        what_to_Do()
    if(temp_V ==1):
        game()
    if(temp_Vone == 2):
        Exit()

what_to_Do()

































