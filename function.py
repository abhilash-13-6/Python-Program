numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
squared_numbers = map(lambda x: x**2, numbers)

# Convert the map object to a list and print the result
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
