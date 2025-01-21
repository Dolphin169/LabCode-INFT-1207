# Name: Kevin, Owen
# Date 2025-01-21
# Last Modified: 2025-01-
# Description: A program that generates secure passwords based on user
# criteria such as length, number of letters, digits, and special characters

import random
MAX_LENGTH = 28
MIN_LENGTH = 4
is_valid = True
error_message_valid = "Please enter a valid integer"
while is_valid == True:
        passwordLength = input("Please enter the desired password length between 4-28: ")
        if passwordLength.isnumeric():
            passwordLength = int(passwordLength)
            if passwordLength < 4 or passwordLength > 28:
                print("Password is not in range: Please enter a integer between 4 and 28")
            elif passwordLength > 4 or passwordLength < 28:
                while is_valid == True:
                    passwordChars = input("Please enter the number of characters for the password: ")
                    if passwordChars.isnumeric():
                        passwordChars = int(passwordChars)
                        while is_valid == True:
                            passwordNumbers = input("Please enter the number of numbers for the password: ")
                            if passwordNumbers.isnumeric():
                                passwordNumbers = int(passwordNumbers)
                                in_range = passwordChars + passwordNumbers
                                if in_range > passwordLength:
                                    print("To many Alphanumeric characters. Please enter less Numbers")
                                else:
                                    print('yay')
                            else:
                                print(error_message_valid)
                    else:
                        print(error_message_valid)
        else:
            print(error_message_valid)
