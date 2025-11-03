numbers = [12, 5, 23, 7, 45, 19, 3, 31, 9, 27]

print("Numbers in list:")
for num in numbers:
    print(num, end=" ")
print("\n")

print(f"Highest Value: {max(numbers)}")
print(f"Lowest Value: {min(numbers)}")

numbers.sort()
print("List of numbers in ascending order: ", numbers)

numbers.sort(reverse=True)
print("List of numbers in descending order: ", numbers)

numbers.append(1)
numbers.append(50)

print(numbers)