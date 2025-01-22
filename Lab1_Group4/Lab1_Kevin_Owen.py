
import random
import string


# Variables and arrays
MAX_LENGTH = 28
MIN_LENGTH = 4

is_valid = True
error_message_valid = "Please enter a valid integer"
#Create a while loop for error checking
while is_valid == True:
        is_valid1 = True
        is_valid2 = True
        is_valid3 = True
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
                # Check the password length is equal to or between 4 and 28
            elif passwordLength >= MIN_LENGTH and passwordLength <= MAX_LENGTH:
                # Create a while loop for error checking
                while is_valid1 == True:
                    # Ask user for character length
                    passwordChars = input("Please enter the number of characters for the password: ")
                    # check if the string input is a integer
                    if passwordChars.isnumeric():
                        # Convert the string to an integer
                        passwordChars = int(passwordChars)
                        is_valid1 = False
                        # Create a while loop for error checking
                        while is_valid2 == True:
                            # Ask user for number length
                            passwordNumbers = input("Please enter the number of numbers for the password: ")
                            # Check if user string is an integer
                            if passwordNumbers.isnumeric():
                                # convert the string to an integer
                                passwordNumbers = int(passwordNumbers)
                                is_valid2 = False
                                # Create a while loop for validation
                                while is_valid3 == True:
                                    # Take user for special character length
                                    passwordSpecialChars = input("Please enter the number of special characters for the password: ")
                                    # Check the string if it is a integer
                                    if passwordSpecialChars.isnumeric():
                                        # If so convert the string into an integer
                                        passwordSpecialChars = int(passwordSpecialChars)
                                        is_valid3 = False
                                        is_valid = False
                                        # Check if the numbers add up to the length of password overall
                                        in_range = passwordChars + passwordNumbers + passwordSpecialChars
                                        if in_range != passwordLength:
                                            print("Please enter the correct length of characters")
                                            is_valid = True







                                    else:
                                        print(error_message_valid)
                            else:
                                print(error_message_valid)
                    else:
                        print(error_message_valid)
        else:
            print(error_message_valid)

randomPassword = []
for count in range(passwordChars):
    randomChoice=random.sample(alphebet)

    randomPassword.append(randomChoice)
