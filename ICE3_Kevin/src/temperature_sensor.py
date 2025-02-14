# Author: Kevin Thomas
# Student ID: 100989562
# Date: 2025-01-29
# Last Modified: 2025-01-29
# Description: Code that finds the min, max, and average for a list of temperatures and validates that they are all valid and
# if so then it will display the information if not then it informs the user of errors in the list
# File: .py
import statistics


def validate_temperature(value):
    try:
        # make given value float to check if it is a number that can be a float
        value = float(value)
        # check if the float value given is in the range
        if -50 <= value <= 150:
            #if the value is able to be a float and is in range then return that float to the calling
            return value
    # If the value cant conform to either condition
    except ValueError:
        # show invalid input for not a number
        return f"Invalid input: '{value}' is not a valid number"
    # show invalid input for not in range
    return f"Invalid input: {value} out of range"



def process_temperatures(temp_list):
    """Process the list of temperatures and return min, max, and avg."""
    #valid_temps = [float(temp) for temp in temp_list]
    valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]

    if not valid_temps:
        return "No valid input provided."
    # make 2 arrays for separating invalid inputs
    valid_temps = []
    invalid_inputs = []

    for temp in temp_list:
        # make a variable that is temp in the validate function
        result = validate_temperature(temp)
        # checks if result is a float which we made it be in the function before as long as its valid
        if isinstance(result, float):
            #append the valid temperature to the valid array
            valid_temps.append(result)
        else:
            # if not a float then add it to the invalid array
            invalid_inputs.append(result)

    if invalid_inputs:
        return f"Invalid inputs detected: {', '.join(map(str, invalid_inputs))}"
    valid_temps.sort()
    min_temp = valid_temps[0]
    max_temp = valid_temps[-1]
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# Test Cases
# Students should analyze and ensure the correctness of the outputs

test_cases = [
    [20],
    [15, 35],
    [],
    [10,-10,30],
    [-50,20,150,25],
    [10,"abc",30],
    [2**31 - 1, - 2**31],
    [10,10,10],
    ["asdf",12345,"!@#$%"],
    ["Eight",9999999999999999999],
    [-50],
    [150],
    [-49, 149],
    [-60,20,160],
    [20, "abc", 30],
    [10, "@", -40],
    [2**31 - 1, -2**31],
    [50, 50, 50],
    []
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)