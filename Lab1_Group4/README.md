what program is about:
- This program is all about creating random secure passwords using numbers, letters,
- and special characters

inputs and outputs:
- The inputs would be: password length as int, amount of numbers in password as int,
- amount of letters in password as int, amount of special characters in password as int.
- The outputs would be: randomly generated password as string, writing password in file as string

what are the functions used:
- The functions used would be: random_char which generates a random character when called,
random_number which generates a random number when called, random_special which generates a random
special character when called

explain code:
The code is intended to take the input of the user and generate a password. How it works:
there are 4 separate functions needed to for the function to work. 3 Functions give random
characters of each type (alphabetic, numeric, and special characters). Another Function uses
the 3 Functions to generate a random password. This is done by taking the length of the characters
wanted, the length of alphabetic characters wanted, the length of numbers wanted, and lastly
the length of special characters wanted. Lastly the function to take the user input within
a specified length, if it isn't within the length it will return false and print an error message for the length
The main code starts by prompting the user for the length of the password and stores the input 
as a string. This is done in a while loop to allow for validation that will repeat until the 
right kind of input is collected. The input that is expected is a integer so to make sure it is
one we check the string using the isnumeric function. Once it is valid the code casts the variable
to a integer for later calculation. Lastly it will check if the integer is between the MIN and MAX 
length limit and if so will set the while loop to false. After this validation there is another for loop
intended for validating the input of the length wanted for the alphabetic characters, numbers, and special
characters. We use a try and except statement to attempt to take the user inputs as an integer until they are
valid and then sets the while loop to false. after all these conditions are valid, we use the generate password
function created earlier to generate a password. It takes the previous inputs and uses them in the function. 
within the function it will first check if the 3 lengths are equal to the overall length and if not will return
nothing. If it is fine the process continues into generating the letters for the password and adding them to a
created array to hold each generated piece of the password. It does this using for loops which will run
the amount of times the length of letters are requested, then it generates a letter and then adds it to an array.
It does this same process for the numbers and the special characters as well. Finally it will scramble the
array randomly and then return the contents as a string. finally we print the Password to the user and
then save the string to a .txt file to be stored

how to execute:
To execute the program you can do it in 2 ways. You can open the file in a editor and run it from there,
or you can run it through the command console directly by finding the .py file in your directories
and running the program. in both instances you'll be given a prompt for a length you want
the password to be and once you give it a password length between 4-28 it will request how many letters,
numbers, and special characters you would like. Finally, it will promptly give you a generated password
you can use as you like.