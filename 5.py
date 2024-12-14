"""
"For" Exercise
Exercise 5: Calculate the Product of Numbers from 1 to M
Write a program to calculate the product of all integers from 1 to M,
where M is a positive integer. Use a for loop to multiply each number
in the range and store the result in a variable.

Note: If M is too large, the result may exceed the limits of the data type.

Example: If M=5, the product is 1 × 2 × 3 × 4 × 5 = 120
"""

M = int(input("Positive int M: "))
product = 1

for int in range(1, M + 1):
    product = product * int

print(f"The product of numbers from 1 to {M} is: {product}")
