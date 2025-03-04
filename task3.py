import random
import string

def generate_password(length, complexity):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Create a pool of characters based on desired complexity
    char_pool = lower
    if complexity >= 2:
        char_pool += upper
    if complexity >= 3:
        char_pool += digits
    if complexity >= 4:
        char_pool += symbols

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    length = int(input("Enter the desired length of the password: "))
    
    # Get user input for password complexity
    print("Select complexity level:")
    print("1. Lowercase letters only")
    print("2. Lowercase and uppercase letters")
    print("3. Lowercase, uppercase letters, and digits")
    print("4. Lowercase, uppercase letters, digits, and symbols")
    complexity = int(input("Enter the complexity level (1-4): "))
    
    # Validate user input
    if complexity not in [1, 2, 3, 4]:
        print("Invalid complexity level. Please choose a number between 1 and 4.")
        return

    # Generate and display the password
    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
