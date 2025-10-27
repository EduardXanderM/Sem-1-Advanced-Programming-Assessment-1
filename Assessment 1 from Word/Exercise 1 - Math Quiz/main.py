import random

def displayMenu(): # Display difficulty selection menu
    print("\nDIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced \n")
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter a number from 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def randomInt(level): # Function to generate random number based on difficulty level
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)
    
def decideOperation(): # Randomly decide between addition and subtraction
    return random.choice(['+', '-'])

def displayProblem(num1, num2, op): # Display the math problem and get user answer
    question = f"{num1} {op} {num2} = "
    try:
        answer = int(input(question))
        return answer
    except ValueError:
        print("Please enter a number...")
        return displayProblem(num1, num2, op)

def isCorrect(user_answer, correct_answer, attempt): # Check if the user's answer is correct
    if user_answer == correct_answer:
        if attempt == 1:
            print("Correct! +10 points.")
            return 10
        else:
            print("Correct on the second try! +5 points.")
            return 5
    else:
        if attempt == 1:
            print("Incorrect. Try again!")
        else:
            print(f"Wrong again. The correct answer was {correct_answer}.")
        return 0

def displayResults(score): # Display final score and rank
    print("\nFinal Score:", score, "/ 100")
    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    elif score >= 50:
        rank = "D"
    else:
        rank = "F"
    print("Rank: ", rank)
    print("")

def playQuiz(): # Main quiz function
    level = displayMenu()
    score = 0
    for i in range(1, 11):
        num1 = randomInt(level)
        num2 = randomInt(level)
        op = decideOperation()

        if op == '+':
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2

        print(f"\nQuestion {i}:")
        user_answer = displayProblem(num1, num2, op)
        points = isCorrect(user_answer, correct_answer, attempt=1)

        if points == 0:
            user_answer = displayProblem(num1, num2, op)
            points = isCorrect(user_answer, correct_answer, attempt=2)

        score += points

    displayResults(score)

def main(): # Main function loop to run the quiz
    while True:
        playQuiz()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()