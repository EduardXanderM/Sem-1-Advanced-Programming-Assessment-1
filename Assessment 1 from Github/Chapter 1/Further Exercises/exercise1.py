def getSeconds(days):
    seconds = days * 24 * 60 * 60
    return seconds

def main():
    try:
        print("Would you like to know how many seconds there are in a day? \n")
        daysInputted = float(input("Enter how many days you would like to know the seconds for: ").strip())
        result = getSeconds(daysInputted)
        print(f"There are {result} second(s) in {daysInputted} day(s). \n")  
    except ValueError:
        print("Please enter a number... \n")
    main()

if __name__ == "__main__":
    main()