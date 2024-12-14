"""Exercise 12: Calculator Menu
Create a program that displays a menu with basic arithmetic operations and allows the user
to perform calculations repeatedly until they choose to exit.
Use a do-while loop to display the menu and handle user choices.

Display cal menu:
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    5.Exit
    Enter your choice:
    Enter the 1st number:
    Enter the 2nd number:

Display the result of num1/ num2 if num2≠0.
If num2=0, display an error message: Division by zero is not allowed..
If the user enters an invalid option, display Invalid choice. Please try again. and show the menu again.
The program should continue to display the menu until the user chooses 5.
"""

def menu():
    print("Calculator Menu:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 5 :
        print("Exit...")
        break
    else:
        a=int(input("Enter the 1st number: "))
        b=int(input("Enter the 2nd number: "))

        match choice:
            case 1:
                print(f"a+b = {a+b}")
            case 2:
                print(f"a-b = {a-b}")
            case 3:
                print(f"a*b = {a*b}")
            case 4:
                if b!=0:
                    print(f"a/b = {a/b}")
                else:
                    print("Division by zero is not allowed.")
            case _:
                print("Invalid choice")
