def doCalculation(calculation, num1, num2):
    if calculation == 1:
        return num1 + num2
    elif calculation == 2:
        return num1 - num2
    elif calculation == 3:
        return num1 * num2
    elif calculation == 4:
        return num1 / num2
    elif calculation == 5:
        return num1 % num2
    else:
        return None

def main():
    try:
        print("1. Add (+) \n2. Subtract (-) \n3. Multiply (*) \n4. Divide (/) \n5. Modulus (%) \n")
        calculation = int(input("Enter a number from 1 to 5 for your desired operation: ").strip())
        num1 = float(input("Enter your first number: ").strip())
        num2 = float(input("Enter your second number: ").strip())
        result = doCalculation(calculation, num1, num2)
        print(f"Result: {result} \n")
    except ValueError:
        print("Please enter a number... \n")
    main()

if __name__ == "__main__":
    main()