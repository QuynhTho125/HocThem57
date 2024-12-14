""" "While" Exercise
Exercise 10: Shape Calculator
Task: Develop a program to calculate the perimeter and area of shapes based on a menu of options.

Menu:
    Calculate the perimeter and area of a rectangle.
    Calculate the perimeter and area of a triangle.
    Calculate the perimeter and area of a circle.
    Exit.

Steps:
    Display the menu to the user.
    Input the user's choice.
    Use a loop to continue until the user exits.
    For each shape, input relevant dimensions (e.g., radius, sides).
    Calculate and print the perimeter and area.

Input: User's menu choice and shape dimensions.
Output: Perimeter and area of the selected shape. """
import math

def cal_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    area = length * width
    print(f"Perimeter of the rectangle: {perimeter}")
    print(f"Area of the rectangle: {area}")

def cal_triangle():
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    perimeter = side1 + side2 + side3
    s = perimeter / 2  # Semi-perimeter for Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print(f"Perimeter of the triangle: {perimeter}")
    print(f"Area of the triangle: {area}")

def cal_circle():
    radius = float(input("Enter the radius of the circle: "))
    perimeter = 2 * math.pi * radius  # Circumference
    area = math.pi * radius ** 2
    print(f"Perimeter (circumference) of the circle: {perimeter}")
    print(f"Area of the circle: {area}")

def menu():
    print("Menu:")
    print("1. Calculate the perimeter and area of a rectangle")
    print("2. Calculate the perimeter and area of a triangle")
    print("3. Calculate the perimeter and area of a circle")
    print("4. Exit.")


while True:
    menu()
    choice = int(input("Your choice (1-4): "))

    if choice == 1:
        cal_rectangle()
    elif choice == 2:
        cal_triangle()
    elif choice == 3:
        cal_circle()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")