"""
"For" Exercise
Exercise 3: Calculate the Sum of Numbers from 1 to N

Write a program to calculate the sum of all integers from 1 to N,
where N is a positive integer. Use a for loop to iterate through the numbers
and accumulate their sum in a variable.

Example: If N=10, the sum is 1 + 2 +3 +...+ 10 = 55.
"""
n = int(input("Enter a positive int n: "))
s=0
for i in range(1, n + 1):  
    s=s+i
print(f"The sum of all integers from 1 to {n} is: {s}")
