"""  "WHILE" Exercise 11:
Create a program in Python that displays a menu of items (as shown in the image) and allows the user to select an o
Use a while loop to keep showing the menu until the user selects the "Exit Menu" option.

Requirements:
    1.Display the menu
    2. Allow the user to input their choice (an integer from 1 to 5).
    3. Use a switch statement to handle each menu option:
    If the user selects 1, display You selected Coke. Price: $1.25.
    If the user selects 2, display You selected Pepsi. Price: $1.00.
    If the user selects 3, display You selected Water. Price: $2.00.
    If the user selects 4, display You selected Coffee. Price: $1.50.
    4. If the user selects 5, exit the menu and display Exiting the menu. Goodbye!.
    5. If the user enters an invalid option, display Invalid choice. Please try again. and show the menu again.
    6. The program should keep running until the user chooses 5.
"""
def menu():
    print("Show menu:")
    print("1.Coke : $1.25")
    print("2.Pepsi : $1.00")
    print("3.Water  : $2.00")
    print("4.Coffee : $1.5")
    print("5.Exit")

while True:
    menu()
    choice = int(input("Your choice (1-5):"))

    match choice:
        case 1:
            print("You selected Coke. Price: $1.25.")
        case 2:
            print("You selected Pepsi. Price: $1.00.")
        case 3:
            print("You selected Water. Price: $2.00.")
        case 4:
            print("You selected Coffee. Price: $1.50.")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")
