""" "WHILE" Exercise 13: Validate User Input
Write a program in Python that uses a while loop to validate user input for entering a valid age.
The program should ensure that the age entered is between 0 and 120 (inclusive).
If the user enters an invalid value, the program should display an error message
and prompt the user to re-enter the age.

Requirements:
    1.Prompt the user to enter their age.
    2.Use a do-while loop to check if the entered age is valid:
        A valid age is any integer between 0 and 120 (inclusive).
        If the input is invalid, display an error message: Invalid age. Please try again. and prompt the user again.
    3.Once a valid age is entered, display: Age successfully recorded: [age]. """

while True:
    age = int(input("Your age: "))
    if 0 <= age <= 120:
        print("Age successfully recorded!")
        break
    else:
        print("Invalid age. Please try again.")
