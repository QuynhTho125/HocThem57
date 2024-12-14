"""
"For" Exercise
Exercise 7: Power Calculation
Task: Input two positive integers a and b and calculate a^b.

Steps:
    Input two integers a and b.
    Use a loop or the * operator to calculate a^b.
    Print the result.

Input: Two integers a and b (e.g., 2 and 3).
Output: Result of a^b (e.g., 8 for 2^3).
"""
a=int(input("Enter integer a: "))
b=int(input("Enter integer b: "))
result=1
for i in range(b):
    result*=a
print(f"The result of {a}^{b} is: {result}")