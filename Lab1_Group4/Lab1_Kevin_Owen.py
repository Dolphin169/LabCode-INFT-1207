import random
import string
from operator import index
from random import shuffle

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

def generate_password(totalLength, charLength, numberLength, specialLength):
    valid = True
    while valid:
        if totalLength >= charLength + numberLength + specialLength:
            valid = False
        else:
           return print("Please enter an amount of characters less then your total length")
    password = []
    for counter in range(charLength):
        character = random_char()
        password.append(character)

    for counter in range(numberLength):
        number = random_number()
        password.append(number)

    for counter in range(specialLength):
        special = random_special()
        password.append(special)

    random.shuffle(password)

    final_password = "".join(password)
    return final_password

# Function to get user input (skeleton)
def get_user_input(prompt, min_value, max_value):
    # Implement logic to get valid user input within a range
        if prompt < min_value or prompt > max_value:
            # Print error message
            print(f"Password is not in range: Please enter a integer between {min_value} and {max_value}")
        else:
            pass
            return True



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
            is_valid = False
        except:
            print("error: Invalid integer, Please enter again")
        final_password = generate_password(password_length, password_letters, password_numbers, password_special)

        print(f"Your password is: " + final_password)


    # Step 3: Generate the password
    print("Your user generated password is: ")
    generate_password(password_length, password_letters, password_numbers, password_special)


    # Step 4: Display the generated password

    # Step 5: Save password to file

# Entry point of the script
if __name__ == "__main__":
    main()
