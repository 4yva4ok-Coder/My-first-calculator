while True:
    first_value = float(input("Enter the first value: "))
    if first_value == float('inf') or first_value == float('-inf'):
        print("Error: Invalid first value!")
        exit()
    operation = input('Enter the operation (+, -, *, /): ')
    if operation not in ['+', '-', '*', '/']:
        print("Error: Invalid operation!")
        exit()
    second_value = float(input("Enter the second value: "))
    if second_value == float('inf') or second_value == float('-inf'):
        print("Error: Invalid second value!")
        exit()
    if operation == '+':
        print("Result:", first_value + second_value)
    elif operation == '-':
        print("Result:", first_value - second_value)
    elif operation == '*':
        print("Result:", first_value * second_value)
    elif operation == '/':
        if second_value != 0:
            print("Result:", first_value / second_value)
        else:
            print("Error: Division by zero!")
    continue_calc = input("Do you want to calculate again? (yes/no): ").lower()
    if continue_calc != 'yes':
        print("Goodbye!")
        break
