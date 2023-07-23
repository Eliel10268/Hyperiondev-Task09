

import operator

def calculate(num1, num2, op):
    # Dictionary mapping operators to corresponding functions from the 'operator' module
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    return ops[op](num1, num2)

def save_equation(num1, num2, op, result):
    # Append the equation and its result to the 'equations.txt' file
    with open("equations.txt", "a") as f:
        f.write(f"{num1} {op} {num2} = {result}\n")

def read_equations(filename):
    try:
        # Open the specified file and read equations line by line
        with open(filename, "r") as f:
            equations = f.readlines()
            for equation in equations:
                print(equation.rstrip())  # Print each equation without trailing newline character
    except FileNotFoundError:
        print(f"File not found: {filename}")

def run_calculator():
    while True:
        try:
            #this will be displayed on the user's screen to choose an option
            choice = input("Enter '1' to enter two numbers and an operator, or '2' to read equations from a file: ")
            if choice == "1":
                # User can choose to enter numbers and operator manually
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                op = input("Enter the operator (+,-,*,/): ")
                result = calculate(num1, num2, op)  # Perform calculation
                print(f"{num1} {op} {num2} = {result}")  # Print the result
                save_equation(num1, num2, op, result)  # Save the equation to 'equations.txt'
            elif choice == "2":
                # User can choose to read equations from a file
                while True:
                    try:
                        filename = input("Enter the name of the file to read equations from: ")
                        read_equations(filename)  # Read and print equations from the specified file
                        break  # Break out of the loop if equations are read successfully
                    except FileNotFoundError:
                        print(f"File not found: {filename}")
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice! Please enter '1' or '2' only.")
        except ZeroDivisionError:
            print("Cannot divide by zero! Please enter a non-zero second number.")
        except KeyError:
            print("Invalid operator! Please enter +,-,*,/ only.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        else:
            break

run_calculator()
