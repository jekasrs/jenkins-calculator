def read_number():
    number = None
    try:
        number = int(input("Enter number\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
    finally:
        return number

def read_operation():
    operation = input("Enter math operation: +, -, *, /\n")
    operations = ["+", "-", "*", "/"]
    if operation not in operations:
        operation = None
    return operation
