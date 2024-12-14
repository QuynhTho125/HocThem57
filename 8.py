"""
"While" Exercise
Exercise 8: Count Numbers Divisible by X

Write a program that takes three integers A, B, and X (A < B),
and counts how many numbers between A and B (inclusive) are divisible by X.
Use a while loop to iterate through the range.

Example: If A = 1, B = 10, and X = 2 , the count is 5 (2, 4, 6, 8, 10).
"""
A=int(input("Enter starting int A (A<B): "))
B=int(input("Enter ending int B: "))
X=int(input("Enter divisor X: "))
if A>B:
    print("Invalid Input: A should be less than B")
else:
    count = 0
    while A<B:
        if A%X==0:
            count+=1
        A+=1
    print(f"The count of numbers between {A} and {B} divisible by {X} is: {count}")
