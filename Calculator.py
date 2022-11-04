def calculate(number1, number2, operation):
    if operation == '+':
        return add(number1, number2)
    elif operation == '-':
        return sub(number1, number2)
    elif operation == '*':
        return mul(number1, number2)
    elif operation == '/':
        return div(number1, number2)
    elif operation == '%':
        return mod(number1, number2)
    else:
        print("operation not valid")


def add(number1, number2):
    return number1 + number2


def sub(number1, number2):
    return number1 - number2


def mul(number1, number2):
    return number1 * number2


def div(number1, number2):
    return number1 / number2


def mod(number1, number2):
    return number1 % number2
