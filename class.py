# Midterm
# by Jeremy Johann
# This is the midterm for CIS-115, this program features 5 True/False and 5 MC questions, and automatically calculates a grade
# CIS-115 Jan 23, 2020 

#import these things
import sys
import os
from os import system, name  
import time

#Clear console function (TY STACKOVERFLOW <3)
def clear_console(): 
  
    if name == "nt": 
        _ = system("cls") 
    else: 
        _ = system("clear") 

def order_110(): #if you are stupid enough
    print("        [ ALERT ALERT ALERT ]         ")
    print("______________________________________")
    print("|    User has a grade below a 60     |")
    print("|                                    |")
    print("| Everyone shall throw grapes at him |")
    print("--------------------------------------")

# Variables
print("")
print("_____________________")
FirstName = input("What is your name?: ")
print("")

TotalScore = 0

LetterGrade = ""

Question1Answer = None
Question2Answer = None
Question3Answer = None
Question4Answer = None
Question5Answer = None
Question6Answer = None
Question7Answer = None
Question8Answer = None
Question9Answer = None
Question10Answer = None

user_is_dumb = None

CorrectAnswer = """
_____________
|           |
|  Correct! |
|           |
|___________|
"""


quiz_start = input("Are you ready to begin your attempt? Y/N: ")



if quiz_start == "Y":
    quiz_start = True
else:
    quiz_start = False

if quiz_start == True:

    #Quiz start
    clear_console()
    print("")
    print("")
    print("Welcome to the CIS-115 midterm!")
    print("")
    print("Hope you studied u_u")
    print("")
    print("ALL ANSWERS ARE CASE SENSITIVE >:(")

    #______________________________________________________________________________

    #Question 1
    print("")
    print("___________________________")
    print("Question 1: (True or False)")
    print("")
    print("CIS-115 is my favorite course?")
    print("___________________________")
    print("")

    Question1Answer = input("T/F: ")

    if Question1Answer == "T":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, CIS-115, is your favorite class")
        TotalScore = TotalScore + 0

    print("Movng to question 2 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 2
    print("")
    print("___________________________")
    print("Question 2: (True or False)")
    print("")
    print("All humans are mammals")
    print("___________________________")
    print("")

    Question2Answer = input("T/F: ")

    if Question2Answer == "T":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, you must be a fish")
        TotalScore = TotalScore + 0

    print("Movng to question 3 in 5 seconds...")
    time.sleep(5)
    clear_console()
    #______________________________________________________________________________

    #Question 3
    print("")
    print("___________________________")
    print("Question 3: (True or False)")
    print("")
    print("North Carolina is in the USA")
    print("___________________________")
    print("")

    Question3Answer = input("T/F: ")

    if Question3Answer == "T":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, you must be a canadian")
        TotalScore = TotalScore + 0

    print("Movng to question 4 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 4
    print("")
    print("___________________________")
    print("Question 1: (True or False)")
    print("")
    print("2 + 2 = 9121232")
    print("___________________________")
    print("")

    Question1Answer = input("T/F: ")

    if Question1Answer == "F":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, you must be dyslexic")
        TotalScore = TotalScore + 0

    print("Movng to question 5 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 5
    print("")
    print("___________________________")
    print("Question 5: (True or False)")
    print("")
    print("The USA is fake")
    print("___________________________")
    print("")

    Question3Answer = input("T/F: ")

    if Question3Answer == "F":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, you must be a canadian")
        TotalScore = TotalScore + 0

    print("Movng to question 6 in 5 seconds...")
    time.sleep(5)
    clear_console()
    #______________________________________________________________________________

    #Question 6
    print("")
    print("___________________________")
    print("Question 6: (Multiple choice)")
    print("")
    print("The language we are using is:")
    print("|(a) Python  |")
    print("|(b) Java    |")
    print("|(c) Nerd    |")
    print("|(a) C++     |")

    Question6Answer = input("Answer: ")

    if Question6Answer == "a" or Question6Answer == "Python":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, answer A, or Python, was the correct answer")
        TotalScore = TotalScore + 0

    print("Movng to question 7 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 7
    print("")
    print("___________________________")
    print("Question 6: (Multiple choice)")
    print("")
    print("The number that comes after 7 is:")
    print("|(a) 3             |")
    print("|(b) 5             |")
    print("|(c) 8             |")
    print("|(a) 198238u31     |")
    print("___________________________")
    print("")

    Question7Answer = input("Answer: ")

    if Question7Answer == "c" or Question7Answer == "8":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, answer c, or 8, was the correct answer")
        TotalScore = TotalScore + 0

    print("Movng to question 8 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 8
    print("")
    print("___________________________")
    print("Question 8: (Multiple choice)")
    print("")
    print("Red is a:")
    print("|(a) Number             |")
    print("|(b) Color              |")
    print("|(c) Sexual Identity    |")
    print("|(a) Animal name        |")
    print("___________________________")
    print("")

    Question8Answer = input("Answer: ")

    if Question8Answer == "b" or  Question8Answer == "Color":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, answer b, or Color, was the correct answer")
        TotalScore = TotalScore + 0

    print("Movng to question 9 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 9
    print("")
    print("___________________________")
    print("Question 9: (Multiple choice)")
    print("")
    print("If john buys 10 oranges and nothing else, how many apples will he have?: ")
    print("|(a) 0              |")
    print("|(b) 5              |")
    print("|(c) -56            |")
    print("|(a) ∞              |")
    print("___________________________")
    print("")

    Question9Answer = input("Answer: ")

    if Question9Answer == "a" or  Question9Answer == "None":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect,answer A, or None, was the correct answer, some people....")
        TotalScore = TotalScore + 0

    print("Movng to question 9 in 5 seconds...")
    time.sleep(5)
    clear_console()

    #______________________________________________________________________________

    #Question 10
    print("")
    print("___________________________")
    print("Question 10: (Multiple choice)")
    print("")
    print("How many inches are in one foot (Ft.)")
    print("|(a) 0              |")
    print("|(b) 36             |")
    print("|(c) hello          |")
    print("|(a) 12             |")
    print("___________________________")
    print("")

    Question10Answer = input("Answer: ")

    if Question10Answer == "a" or  Question10Answer == "12":
        print("")
        print("")
        print(CorrectAnswer)
        print("")
        print("")        
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, answer A, or 12, was the correct answer, some people....")
        TotalScore = TotalScore + 0

    quiz_start = False

    print("Calculating your grade...")
    time.sleep(5)
    clear_console()
    #______________________________________________________________________________
    
    if TotalScore >= 90:
        LetterGrade = "A"
    elif TotalScore >= 80:
        LetterGrade = "B"
    elif TotalScore >= 70:
        LetterGrade = "C"
    elif TotalScore >= 60:
        LetterGrade = "D"
    else:
        LetterGrade = "F"

    print("|_________________________________________________")
    print("|" + FirstName + ", your grade was a " + LetterGrade)
    print("|_________________________________________________")
    print("| Visualized Grade:")
    print("|____________________________________________________________")
    print("|")

    display = ""
    spacing = ""

    if int(TotalScore) <= 9:
        spacing = "                                        "
    elif int(TotalScore) <= 15:
        display = "####"
        spacing = "                                    "
    elif int(TotalScore) <= 25:
        display = "########"
        spacing = "                                "
    elif int(TotalScore) <= 35:
        display = "############"
        spacing = "                            "
    elif int(TotalScore) <= 45:
        display = "################"
        spacing = "                        "
    elif int(TotalScore) <= 55:
        display = "####################"
        spacing = "                    "
    elif int(TotalScore) <= 65:
        display = "########################"
        spacing = "                "
    elif int(TotalScore) <= 75:
        display = "############################"
        spacing = "      "
    elif int(TotalScore) <= 85:
        display = "################################"
        spacing = "        "
    elif int(TotalScore) <= 95:
        display = "####################################"
        spacing ="    "
    elif int(TotalScore) == 100:
        display = "########################################"
        spacing = ""

    print("| 0 (F) [" + display + spacing + "] 100 (A)" )
    print("|____________________________________________________________")
    print("")
    
    if TotalScore < 60:
        user_is_dumb = True
        order_110()

    print("")
    print("Code Repository: https://github.com/insxne246/College-Midterm/")
    print("")
    print("Automatically closing in 30 seconds..")
    time.sleep(30)
    exit()

else:
    print("Restart the program when you are ready")
    time.sleep(5)
    exit