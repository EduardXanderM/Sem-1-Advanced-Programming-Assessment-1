def doMath(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "x":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "%":
        return num1 % num2
    else:
        return "?"

operation = input("Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%) \nPlease enter the symbol for your desired operation: ").strip()
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
result = doMath(operation, num1, num2)
print(f"Result: {result}")