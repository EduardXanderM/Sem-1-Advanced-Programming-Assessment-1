loops = 0
choice = input("Would you like to continue in this journey? (Y/N): ")

while choice.upper() == "Y":
    loops += 1
    print("Time loop executed", loops, "time(s).")
    choice = input("Would you like to continue on this journey? (Y/N): ")

print("The while loop executed", loops, "time(s) in total. \nProgram ended...")