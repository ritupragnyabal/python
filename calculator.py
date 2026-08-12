print('Hello World!')

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
operation = input('Enter an operation (+, -, *, /): ')
if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)           
elif operation == '/':
    if num2 != 0:
        result = num1 // num2
        print(result)
    else:
        result = 'Error: Division by zero'
        print(result)
else:
    result = 'Error: Invalid operation'
    print(result)