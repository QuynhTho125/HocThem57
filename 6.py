"""
"For" Exercise
Exercise 6: Count Divisors
Task: Write a program that inputs an integer n and displays the number of its divisors.

Steps:
    Input an integer n.
    Loop through numbers from 1 to n.
    Check if each number divides n evenly.
    Count and print the divisors.
Input:
    An integer n (e.g., 12).
Output:
    Number of divisors (e.g., 6 for 12).
"""

n = int(input("Input n: "))
divisors = 0

for int in range(1, n + 1):
    if n % int == 0:
        divisors += 1

print(f"The number of divisors of {n} is: {divisors}")
