# Calculator - Python Edition
# Nikhil Paranjape - indianpoptart
# 2018-07-22

import time

class Calculator:
    print("Test")


def print_menu():  # Calc menu
    print(30 * "-", "MENU", 30 * "-")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Root")
    print("8. Quit")
    print("9. Help")
    print(67 * "-")



def help_menu():  ## Calc help menu
    print(28 * "-", "HELP MENU", 28 * "-")
    print("1. Addition - Adds two values together")
    print("2. Subtraction - Takes minuend and subtracts by the subtrahend")
    print("3. Division - Takes the dividend and divides by the divisor")
    print("4. Multiplication - Multiplies two values together")
    print("5. Modulus - Takes the dividend mod the divisor")
    print("6. Exponentiation - Takes the base and raises it to an exponent")
    print("7. Root - Takes the radicand and finds the root based on some degree")
    print("8. Quit - Quits program enter Y or N to confirm")
    print("9. Help - Prints this information to help you!")
    print(67 * "-")
    time.sleep(5)
    print("")


# Define invalid choice function
def invalid():
    print("INVALID CHOICE!")


# Extra credit variable
result = "null"
# Main calculator while loop
while True:
    print_menu()

    choice = input("Please enter an option: ")

    # Addition
    if choice == '1':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter a value: '))

        # Run main program
        number_2 = float(input('Enter another value: '))
        print('{} + {} = '.format(number_1, number_2))
        result = number_1 + number_2
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()

        if var == 'n':
            result = "null"
            print("")

    # Subtraction
    elif choice == '2':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter minuend: '))

        # Run main program
        number_2 = float(input('Enter subtrahend: '))
        print('{} - {} = '.format(number_1, number_2))
        result = number_1 - number_2
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()
        if var == 'n':
            result = "null"
            print("")

    # Division
    elif choice == '3':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter dividend: '))

        # Run main program
        number_2 = float(input('Enter divisor: '))
        print('{} / {} = '.format(number_1, number_2))
        result = number_1 / number_2
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()

        if var == 'n':
            result = "null"
            print("")

    # Multiplication
    elif choice == '4':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter a value: '))

        # Run main program
        number_2 = float(input('Enter another value: '))
        print('{} * {} = '.format(number_1, number_2))
        result = number_1 * number_2
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()

        if var == 'n':
            result = "null"
            print("")

    # Modulus
    elif choice == '5':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter dividend: '))

        # Run main program
        number_2 = float(input('Enter divisor: '))
        print('{} % {} = '.format(number_1, number_2))
        result = number_1 % number_2
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()

        if var == 'n':
            result = "null"
            print("")

    # Exponentiation
    elif choice == '6':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter base: '))

        # Run main program
        number_2 = float(input('Enter exponent: '))
        print('{}^{} = '.format(number_1, number_2))
        result = number_1 ** number_2
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()

        if var == 'n':
            result = "null"
            print("")
    # Root
    elif choice == '7':
        # Check for last result
        if result != "null":
            number_1 = result
        else:
            number_1 = float(input('Enter raddicand: '))

        # Run main program
        number_2 = float(input('Enter degree: '))
        print('{}^{} = '.format(number_1, number_2))
        result = number_1 ** (1 / number_2)
        print(result)

        # Check if user wants to store number
        var = input("Do you want to store the result for the next operation? Enter y/n : ").lower()

        if var == 'n':
            result = "null"
            print("")

    # Quit
    elif choice == '8':
        var = input("Are you sure you would like to quit? Enter y/N : ").lower()
        if var == 'y':
            print("Program ending.")
            break

        elif var == 'n':
            print("Alright")
    # Help menu
    elif choice == '9':
        help_menu()
    # If an invalid input is selected
    else:
        invalid()
