
numbers = []
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)


print("\nFirst element:", numbers[0])
print("Last element:", numbers[-1])


print("\nAll elements:")
for num in numbers:
    print(num)


reversed_numbers = numbers[::-1]
print("\nReversed list:")
for num in reversed_numbers:
    print(num)
