num1 = int(input("Enter a number: "))
op = input("Enter an operator +, -, /, *: ")
num2 = int(input("Enter another number: "))

match op:
    case '+':
        print("Result:", num1 + num2)
    case '-':
        print("Result:", num1 - num2)
    case '*':
        print("Result:", num1 * num2)
    case '/':
        print("Result:", num1 / num2)
    case _:
        print("Invalid operator")