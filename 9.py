""" "While" Exercise
Exercise 9: Smallest Number Divisible by 3, 5, and 7
Task: Find the smallest positive number divisible by 3, 5, and 7.

Steps:
    Initialize a variable n = 1.
    Use a loop to check divisibility by 3, 5, and 7.
    Stop when a number satisfying the condition is found.
    Print the result.

Input: None (the calculation is fixed).
Output: The smallest positive number divisible by 3, 5, and 7 (e.g., 105). """
n=1
while True:
    if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
        break
    n+=1
print(f"The smallest positive number divisible by 3, 5, and 7 is: {n}")

