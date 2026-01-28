# Lab Solutions

# Ask user for an input
user_in = int(input('Please enter a number to check if it is odd or even:'))

if user_in % 2 == 0:
    print(user_in, ' is an even number')
else:
    print(user_in, ' is an odd number')


# Ask user for an input
user_in = int(input('Please enter a number to check if it is odd, even or zero:'))

if user_in <= 0:
    print('Please enter a number greater than 0')
elif user_in % 2 == 0:
    print(user_in, ' is an even number')
else:
    print(user_in, ' is an odd number')


    # Ask user for an input - does not cover negative numbers
user_in = int(input('Please enter a number to check the number of digits:'))

if user_in >= 0 and user_in < 10:
    print(user_in,' is a single digit number')
elif user_in >= 10 and user_in < 100:
    print(user_in,' is a two digit number')
elif user_in >= 100 and user_in < 1000:
    print(user_in,' is a three digit number')
else:
    print('The entered number is composed of more than 3 digits')


    # Ask user for an input
user_in = input('Please enter a character for verification:')

if user_in >= 'A' and user_in <= 'Z':
    print(user_in, ' is an upper case character')
elif user_in >= 'a' and user_in <= 'z':
    print(user_in, ' is a lower case character')
elif user_in >= '0' and user_in <= '9':
    print(user_in, ' is a digit')
else:
    print(user_in, ' is a special character')
if user_in in "aeiouAEIOU":
    print(user_in, " is a vowel")


    # This is nicer using the string library where we can
user_in = input('Please enter a character for verification:')

if user_in.isupper():
    print(user_in, ' is an upper case character')
elif user_in.islower():
    print(user_in, ' is a lower case character')
elif user_in.isdigit():
    print(user_in, ' is a digit')
else:
    print(user_in, ' is a special character')
if user_in in "aeiouAEIOU":         # Or alternatively user_in.lower() in "aeiou"
    print(user_in, " is a vowel")



year = int(input('Please enter the year you would like to check:'))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, '- is a leap year')
else:
    print(year, '- is not a leap year')
