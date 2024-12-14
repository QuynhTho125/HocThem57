"""
"For" Exercise
Exercise 2: Numbers Divisible by 3 and 5
Task: Write a program that takes two integers a and b and displays
all numbers between them divisible by both 3 and 5.

Steps:
    Input two integers a and b.
    Loop through numbers from a to b.
    Check if each number is divisible by both 3 and 5.
    Print the valid numbers.
Input:
    Two integers a and b (e.g., 1 and 50).
Output:
    All numbers = divisible by both 3 and 5 (e.g., 15 30 45).
"""

a = int(input("Int a: "))
b = int(input("Int b: "))

for int in range(a, b + 1):
    if int % 3 == 0 and int % 5 == 0:
        print(int, end=" ")
