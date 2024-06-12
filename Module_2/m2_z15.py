result = 0
operand = 0
operator = None
wait_for_number = True

while True:

    if wait_for_number:
        operand = input("Input a number: ")
        try:
            operand = int(operand)
            wait_for_number = not wait_for_number

        except ValueError:
            print(f"val {operand} is not a number")
            operand = (input("Input a number: "))
            operand = int(operand)
            wait_for_number = not wait_for_number

    if operator == None or operator == '+':
        result = result + operand
    elif operator == '-':
        result = result - operand
    elif operator == '*':
        result = result * operand
    elif operator == '/':
        result = result / operand

    if not wait_for_number:
        operator = input("Input operator: ")

        if operator == "+" or operator == '-' or operator == '*' or operator == '/':
            wait_for_number = not wait_for_number

        elif operator == '=':
            break
        else:
            print(f"symbol {operator} is not a operator")
            operator = input("Input operator: ")
            wait_for_number = not wait_for_number


print(result)
