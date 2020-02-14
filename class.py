# Midterm
# by Jeremy Johann
# This is the midterm for CIS-115, this program features 5 True/False and 5 MC questions, and automatically calculates a grade
# CIS-115 Jan 23, 2020

import time

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

#Timer I kinda stole
class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start_timer(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop_timer(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        #print(f"Elapsed time: {elapsed_time:0.4f} seconds")


if quiz_start == True:
    #Quiz start

    print("Welcome to the CIS-115 midterm!")
    print("")
    print("Hope you studied")
    quiz_start = input("Are you ready to begin your attempt? Y/N: ")

    if quiz_start == "Y":
        quiz_start = True
    else:
        quiz_start = False
        
    #______________________________________________________________________________

    #Question 1

    print("Question 1: (True or False)")
    print("")
    print("CIS-115 is my favorite course?")

    Question1Answer = input("T/F: ")

    if Question1Answer == "T" or "True":
        print("Correct")
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, CIS-115, is your favorite class")
        TotalScore = TotalScore + 0

    #______________________________________________________________________________

    #Question 2

    print("Question 2: (Multiple choice)")
    print("")
    print("The language we are using is:")
    print("|(a) Python  |")
    print("|(b) Java    |")
    print("|(c) Nerd    |")
    print("|(a) C++     |")

    Question2Answer = input("Answer: ")

    if Question2Answer == "a" or "Python":
        print("Correct")
        TotalScore = TotalScore + 10
    else:
        print("Incorrect, answer A, or Python, was the correct answer")
        TotalScore = TotalScore + 0

    #______________________________________________________________________________

    if TotalScore >= 90:
        LetterGrade == "A"
    elif TotalScore >= 80:
        LetterGrade == "B"
    elif TotalScore >= 70:
        LetterGrade == "C"
    elif TotalScore >= 60:
        LetterGrade == "D"
    else:
        LetterGrade == "F"

else:
    print("Restart the program when you are ready")
    time.sleep(5)
    exit