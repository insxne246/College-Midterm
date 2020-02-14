# Midterm
# by Jeremy Johann
# This is the midterm for CIS-115, this program features 5 True/False and 5 MC questions, and automatically calculates a grade
# CIS-115 Jan 23, 2020

import sys
import os
from os import system, name  
import time

#Clear console function
def clear(): 
  
    if name == "nt": 
        _ = system("cls") 
    else: 
        _ = system("clear") 



# Variables
FirstName = input("What is your name?: ")

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

elapsed_time = None

quiz_start = None

quiz_start = input("Are you ready to begin your attempt? Y/N: ")

CorrectAnswer = """
_____________
|           |
|  Correct! |
|           |
|___________|
"""



if quiz_start == "Y":
    quiz_start = True
else:
    quiz_start = False

if quiz_start == True:

    #Quiz start

    print("Welcome to the CIS-115 midterm!")
    print("")
    print("Hope you studied")

    #______________________________________________________________________________

    #Question 1
    print("")
    print("___________________________")
    print("Question 1: (True or False)")
    print("")
    print("CIS-115 is my favorite course?")

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
    clear()

    #______________________________________________________________________________

    #Question 2
    print("")
    print("___________________________")
    print("Question 2: (True or False)")
    print("")
    print("All humans are mammals")

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
    clear()
    #______________________________________________________________________________

    #Question 3
    print("")
    print("___________________________")
    print("Question 3: (True or False)")
    print("")
    print("North Carolina is in the USA")

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
    clear()

    #______________________________________________________________________________

    #Question 4
    print("")
    print("___________________________")
    print("Question 1: (True or False)")
    print("")
    print("2 + 2 = 9121232")

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
    clear()

    #______________________________________________________________________________

    #Question 5
    print("")
    print("___________________________")
    print("Question 5: (True or False)")
    print("")
    print("The USA is fake")

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

    print("Movng to question 6 in 5 seconds...")
    time.sleep(5)
    clear()
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

    if Question6Answer == "a" or "Python":
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
    clear()
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


    print(FirstName + ", your grade was a " + LetterGrade)

else:
    print("Restart the program when you are ready")
    time.sleep(5)
    exit