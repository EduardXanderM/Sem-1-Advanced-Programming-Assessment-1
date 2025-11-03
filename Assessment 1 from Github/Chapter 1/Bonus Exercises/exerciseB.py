locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

print(locations)
print(f"The length of this list is {len(locations)}.")
print(f"Sorted: {sorted(locations)}")
print(f"Original: {locations}")
print(f"Sorted in Reverse: {sorted(locations, reverse=True)}")
print(f"Original: {locations}")
locations.reverse()
print(f"Reversed List: {locations}")
locations.sort(key=str.lower)
print(f"Sorted in Alphabetical Order: {locations}")
locations.sort(key=str.lower, reverse=True)
print(f"Sorted in Reverse Alphabetical Order: {locations}")