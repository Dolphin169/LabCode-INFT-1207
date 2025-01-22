import random
import string


MIN_VALUE = 4
MAX_VALUE = 28
# Functions
def random_char():
    character = random.choice(string.ascii_letters)
    return character

def random_number():
    number = random.choice(string.digits)
    return number

def random_special():
    special = random.choice(string.punctuation)
    return special
# Function to get user input (skeleton)
def get_user_input(prompt, min_value, max_value):
    # Implement logic to get valid user input within a range
        if prompt < min_value or prompt > max_value:
            # Print error message
            print(f"Password is not in range: Please enter a integer between {min_value} and {max_value}")
        else:
            pass
            return True

# Function to generate a password (skeleton)
def generate_password(length, num_letters, num_digits, num_specials):
    # Ensure total requested characters do not exceed length
    if length != (num_letters + num_digits + num_specials):
        print("The amount of letters, numbers, and special characters isn't the length")
    # Generate required characters (letters, digits, specials)
    # Fill remaining characters
    # Shuffle and return password
    pass

# Main function (skeleton)
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs for password length and character distribution
    is_valid = True
    while is_valid == True:
            password_length = input("Please enter the desired password length between 4-28: ")
            if password_length.isnumeric():
                password_length = int(password_length)
                if get_user_input(password_length, MIN_VALUE, MAX_VALUE):
                    is_valid = False
            else:
                print("Please enter a valid integer")
    # Step 2: Validate user inputs
    is_valid = True
    while is_valid == True:
        try:
            password_letters = int(input("Please enter the amount of letters: "))
            password_numbers = int(input("Please enter the amount of numbers: "))
            password_special = int(input("Please enter the amount of special characters: "))
            generate_password(password_length, password_letters, password_numbers, password_special)
        except:
            print("error: Invalid integer, Please enter again")

    # Step 3: Generate the password

    # Step 4: Display the generated password

    # Step 5: Save password to file

# Entry point of the script
if __name__ == "__main__":
    main()
