# Name: Kevin, Owen
# Date 2025-01-21
# Last Modified: 2025-01-
# Description: A program that generates secure passwords based on user
# criteria such as length, number of letters, digits, and special characters

import random
MAX_LENGTH = 28
MIN_LENGTH = 4
is_valid = True
while is_valid == True:
        passwordLength = input("Please enter the desired password length between 4-28: ")
        if passwordLength.isnumeric():
            passwordLength = int(passwordLength)
            if passwordLength < 4 or passwordLength > 28:
                print("error")
            elif passwordLength > 4 or passwordLength < 28:
                passwordChars = int(input("Numbers"))
                passwordNumbers = int(input("Numbers"))
                for count in range(passwordLength):
                    number = random.randint(0,9)
                    print(number, end="")
        else:
            print("Please enter a valid integer")
