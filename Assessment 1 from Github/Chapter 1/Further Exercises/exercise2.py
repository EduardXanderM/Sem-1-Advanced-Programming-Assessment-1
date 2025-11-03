def main():
    try:
        print("Would you like to know what the sum of all the digits in number is? \n") 
        num = float(input("Enter any number here: ").strip())
        sumOfDigits = 0
        for ch in str(num):
            if ch.isdigit():
                sumOfDigits += int(ch)
        print(f"Result: {sumOfDigits}")
    except ValueError:
        print("Please enter a number... \n")
    main()

if __name__ == "__main__":
    main()