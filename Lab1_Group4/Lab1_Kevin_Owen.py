# Name: Kevin, Owen
# Date 2025-01-21
# Last Modified: 2025-01-
# Description: A program that generates secure passwords based on user
# criteria such as length, number of letters, digits, and special characters

import random
# Variables and arrays
MAX_LENGTH = 28
MIN_LENGTH = 4
alphebet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<',
    '>', '/', '?'
]
is_valid = True
error_message_valid = "Please enter a valid integer"
#Create a while loop for error checking
while is_valid == True:
        # Ask user for password length
        passwordLength = input("Please enter the desired password length between 4-28: ")
        # Check if the string input is an integer
        if passwordLength.isnumeric():
            # Convert the string to an integer
            passwordLength = int(passwordLength)
            # Check the password length is not between 4 and 28
            if passwordLength < MIN_LENGTH or passwordLength > MAX_LENGTH:
                # Print error message
                print("Password is not in range: Please enter a integer between 4 and 28")
                # Check the password length is between 4 and 28
            elif passwordLength > MIN_LENGTH and passwordLength < MAX_LENGTH:
                # Create a while loop for error checking
                while is_valid == True:
                    # Ask user for character length
                    passwordChars = input("Please enter the number of characters for the password: ")
                    # check if the string input is a integer
                    if passwordChars.isnumeric():
                        # Convert the string to an integer
                        passwordChars = int(passwordChars)
                        # Create a while loop for error checking
                        while is_valid == True:
                            # Ask user for number length
                            passwordNumbers = input("Please enter the number of numbers for the password: ")
                            # Check if user string is an integer
                            if passwordNumbers.isnumeric():
                                # convert the string to an integer
                                passwordNumbers = int(passwordNumbers)
                                # Create a veriable for collecting the overall range
                                in_range = passwordChars + passwordNumbers
                                if in_range > passwordLength:
                                    print("To many Alphanumeric characters. Please enter less Numbers")
                                while is_valid == True:
                                    passwordSpecialChars = input("Please enter the number of special characters for the password: ")
                                    if passwordSpecialChars.isnumeric():
                                        passwordSpecialChars = int(passwordSpecialChars)
                                        in_range = passwordChars + passwordNumbers + passwordSpecialChars
                                        if in_range > passwordLength:
                                            print("To many Alphanumeric characters. Please enter less Numbers")
                                    else:
                                        print(error_message_valid)
                            else:
                                print(error_message_valid)
                    else:
                        print(error_message_valid)
        else:
            print(error_message_valid)
