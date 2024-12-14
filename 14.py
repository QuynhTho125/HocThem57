""" WHILE Exercise 14: Guess the Number Game
Write a program to simulate a number guessing game:
The program randomly selects a number between 1 and 100.
The user repeatedly enters guesses.
Use a while loop to keep asking for input until the user guesses the correct number.
The program should provide hints like "Too high!" or "Too low!" after each guess.
Extension: Count the number of guesses and display it when the user wins."""

import random
random= random.randint(1, 100)
print("Guess number between 1 and 100!!")

isCheck=True
while isCheck:
    try:
        n=int(input("Enter the number to guess: "))
        if n<1 or n>100:
            raise ValueError
        elif n < random:
            print("Too low!")
        elif n > random:
            print("Too high!")
        else:
            print("Correct!")
            isCheck=False
    except ValueError:
        print("Please enter a number form 1-100!")
