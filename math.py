def calculate(a: int, b: int, operation: str):
    result = 0.0
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            raise Exception("Cannot divide by zero.")
        result = a / b
    else:
        raise Exception("Unknown math operation")
    return result