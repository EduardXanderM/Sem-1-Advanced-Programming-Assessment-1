def productOfList(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

my_list = [2, 3, 4, 5] 
result = productOfList(my_list)

print("List:", my_list)
print("Product of list items:", result)