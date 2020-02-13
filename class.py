# Midterm
# by Jeremy Johann
# This is the midterm for CIS-115, this program features 5 True/False and 5 MC questions, and automatically calculates a grade
# CIS-115 Jan 23, 2020

print("Welcome to the CIS-115 midterm!")
print("")
print("Hope you studied")

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