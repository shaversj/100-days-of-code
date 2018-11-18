# Simple calculator


def main():
    print('Select operation.')
    print('1. Add \n2. Subtract \n3. Multiply \n4. Divide')
    choice = int(input('Enter choice(1/2/3/4): '""))
    num1 = int(input('Enter first number: '""))
    num2 = int(input('Enter second number: '""))

    while True:
        if choice == 1:
            print(f'{num1} + {num2} = {add(num1, num2)}')
            break
        elif choice == 2:
            print(f'{num1} - {num2} = {subtract(num1, num2)}')
            break
        elif choice == 3:
            print(f'{num1} * {num2} = {multiply(num1, num2)}')
            break
        elif choice == 4:
            print(f'{num1} / {num2} = {divide(num1, num2)}')
            break


def add(num1, num2):

    return num1 + num2


def subtract(num1, num2):

    return num1 - num2


def multiply(num1, num2):

    return num1 * num2


def divide(num1, num2):

    return float(num1 / num2)


if __name__ == "__main__":
    main()
