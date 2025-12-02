if __name__ == "__main__":
    print("================================")
    print("      ** Calculator **          ")
    print("================================")
    print("Supported operations: +, -, *, /")

    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        result = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero (0).")
            else:
                result = num1 / num2
        else:
            print("Error: Invalid operation choice.")

        if result is not None:
            print(f"\nResult: {num1} {operation} {num2} = **{result}**")

    except ValueError:
        print("\nError: Invalid number input. Please enter valid numerical values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")