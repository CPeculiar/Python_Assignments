# Basic Calculator Program
# This program performs basic arithmetic operations on two numbers

def main():
    print("=" * 40)
    print("      BASIC CALCULATOR PROGRAM")
    print("=" * 40)
    
    try:
        # Get input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("\nAvailable operations:")
        print("+ for Addition")
        print("- for Subtraction") 
        print("* for Multiplication")
        print("/ for Division")
        
        operation = input("\nEnter the operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
            
        elif operation == '-':
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
            
        elif operation == '*':
            result = num1 * num2
            print(f"\n{num1} * {num2} = {result}")
            
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"\n{num1} / {num2} = {result}")
            else:
                print("\nError: Division by zero is not allowed!")
                
        else:
            print(f"\nError: '{operation}' is not a valid operation!")
            print("Please use +, -, *, or /")
    
    except ValueError:
        print("\nError: Please enter valid numbers!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    
    print("\nThank you for using the calculator!")

# Enhanced version with additional features
def enhanced_calculator():
    print("=" * 45)
    print("    ENHANCED CALCULATOR PROGRAM")
    print("=" * 45)
    
    while True:
        try:
            # Get input from user
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            print("\nAvailable operations:")
            print("1. + (Addition)")
            print("2. - (Subtraction)") 
            print("3. * (Multiplication)")
            print("4. / (Division)")
            print("5. % (Modulus)")
            print("6. ** (Exponentiation)")
            
            operation = input("\nEnter the operation (+, -, *, /, %, **): ").strip()
            
            # Dictionary to store operations and their results
            operations = {
                '+': (num1 + num2, f"{num1} + {num2} = {num1 + num2}"),
                '-': (num1 - num2, f"{num1} - {num2} = {num1 - num2}"),
                '*': (num1 * num2, f"{num1} * {num2} = {num1 * num2}"),
                '%': (num1 % num2, f"{num1} % {num2} = {num1 % num2}"),
                '**': (num1 ** num2, f"{num1} ** {num2} = {num1 ** num2}")
            }
            
            # Handle division separately for zero check
            if operation == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"\n{num1} / {num2} = {result}")
                else:
                    print("\nError: Division by zero is not allowed!")
            elif operation in operations:
                result, display = operations[operation]
                print(f"\n{display}")
            else:
                print(f"\nError: '{operation}' is not a valid operation!")
                print("Please use +, -, *, /, %, or **")
            
            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
            if continue_calc not in ['y', 'yes']:
                break
                
        except ValueError:
            print("\nError: Please enter valid numbers!")
        except ZeroDivisionError:
            print("\nError: Division by zero is not allowed!")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
    
    print("\nThank you for using the enhanced calculator!")

# Run the programs
if __name__ == "__main__":
    # Run basic calculator
    main()
    
    # Ask if user wants to try enhanced version
    print("\n" + "=" * 50)
    try_enhanced = input("Would you like to try the enhanced calculator? (y/n): ").strip().lower()
    if try_enhanced in ['y', 'yes']:
        enhanced_calculator()