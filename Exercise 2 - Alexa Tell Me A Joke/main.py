import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
jokes_path = os.path.join(script_dir, 'randomJokes.txt')

def loadJokes(filename):
    jokes = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if "?" in line:
                setup, punchline = line.split("?", 1)
                jokes.append((setup + "?", punchline))
    return jokes

def tellJoke(jokes):
    setup, punchline = random.choice(jokes)
    print("\nAlexa:", setup)
    input("Press Enter to see the punchline...")
    print("\nAlexa:", punchline, "\n")

def main():
    jokes = loadJokes(jokes_path)
    print("Type 'Alexa tell me a joke' to hear one, or 'quit' to exit.")
    while True:
        command = input("\nYou: ").strip().lower()
        if command == "alexa tell me a joke":
            tellJoke(jokes)
        elif command == "quit":
            print("Alexa: Goodbye! Hope you laughed")
            break
        else:
            print("Alexa: I can only tell jokes or say goodbye!")

if __name__ == "__main__":
    main()