
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Calculator import calculate


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('use my calculator')
    choices = {'+': 'Add', '-': 'Sub', '*': 'Mul',
               '/': 'Div', '%': 'mod', 'e': 'exit'}
    while True:
        op = input("enter the operation")
        if op not in choices:
            print('operation not allowed')1
        elif op == 'e':
            print('exiting....')
            break
        else:
            _num1_ = float(input('enter first number'))
            _num2_ = float(input('enter second number'))

            print(f'{_num1_} {op} {_num2_}')
            result = calculate(_num1_, _num2_, op)
            print(result)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
