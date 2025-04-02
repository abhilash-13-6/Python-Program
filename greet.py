def greet_user(name):
    """
    This function takes the user's name as input and prints a greeting message.
    """
    if name:
        print(f"Hello, {name}! Welcome to the Python world!")
    else:
        print("Hello! Please provide a name to receive a personalized greeting.")

def main():
    """
    Main function to execute the program.
    """
    print("Welcome to the Greeter Program!")
    user_name = input("Please enter your name: ").strip()
    greet_user(user_name)

if __name__ == "__main__":
    main()
