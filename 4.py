"""
"For" Exercise
Exercise 4: Count Numbers Divisible by X
Write a program to count how many numbers are divisible by X in the range from A to B,
where A<=B, and X is a positive integer. Use a for loop to check each number in the range.

Example: If A=1, B=50, and X=5, there are 10 numbers divisible by 5: 5,10,15,...,50
"""

while True:
    A = int(input("Starting int A: "))
    B = int(input("Ending int B: "))

    if A > B:
        print("Error: A must be less than or equal to B. Please try again.")
    else:
        break

X = int(input("Enter the divisor X (positive integer): "))
i=0
for int in range(A, B + 1):
    if int % X == 0:
        i=i+1
print(f"The number of integers divisible by {X} from {A} to {B} is: {i}")
