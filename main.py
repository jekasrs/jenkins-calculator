from jenkins_calculator.math import calculate
from jenkins_calculator.utils import read_number, read_operation

if __name__ == "__main__":
    a = read_number()
    while (a != None):
        a = read_number()

    b = read_number() 
    while b != None:
        b = read_number()

    operation = read_operation()
    while(operation != None):
        operation = read_operation()

    result = calculate(a, b, operation)
    print("The result is", result)
