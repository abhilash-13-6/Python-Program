def is_palindrome(num):
    
    num_str = str(num)
    return num_str == num_str[::-1]


number = int(input("Enter a number: "))


if is_palindrome(number):
    print(f"The number {number} is a palindrome.")
else:
    print(f"The number {number} is not a palindrome.")