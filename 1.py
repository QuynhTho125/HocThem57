"""
"For" Exercise
Exercise 1: Display Even Numbers
Task: Write a program that takes an integer n as input
and displays all even numbers from n up to 100.

Steps:
    Input an integer n.
    Loop through numbers from n to 100.
    Check if a number is even (divisible by 2).
    Print the even numbers.

Input:
    An integer n (e.g., 90).
Output:
    All even numbers from n to 100 (e.g., 90 92 94 96 98 100).
"""
n = int(input("Integer n: "))

for int in range(n, 101):
    if int % 2 == 0:
        print(int, end=" ")




