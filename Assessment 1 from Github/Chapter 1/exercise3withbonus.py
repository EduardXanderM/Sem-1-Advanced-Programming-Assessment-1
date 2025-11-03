def doTriangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Correct, these sides form a triangle.")
        if a == b == c:
            print("It is an Equilateral triangle.")
        elif a == b or b == c or a == c:
            print("It is an Isosceles triangle.")
        else:
            print("It is a Scalene triangle.")
    else:
        print("These sides do not form a triangle.")

a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))
doTriangle(a, b, c)