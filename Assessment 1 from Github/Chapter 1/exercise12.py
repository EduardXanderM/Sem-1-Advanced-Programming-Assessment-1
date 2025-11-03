import math

def calculateShape(shape):
    if shape == 1:
        side = float(input("\nWhat is the side of the square? ").strip())
        print(f"The area of your square is {side*side} units.")
    elif shape == 2:
        radius = float(input("\nWhat is the radius of the circle? ").strip())
        print(f"The area of your square is {math.pi*radius**2} units.")
    else:
        base = float(input("\nWhat is the base of the triangle? ").strip())
        height = float(input("\nWhat is the height of the triangle? ").strip())
        print(f"The area of your square is {(base*height)/2} units.")

shape = int(input("1: Calculate the area of a square \n2: Calculate the area of a circle \n3: Calculate the area of a triangle \nEnter a number from 1 to 3: ").strip())

area = calculateShape(shape)