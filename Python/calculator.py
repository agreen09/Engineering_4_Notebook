running = True
mode = 2
num1 = 0
num2 = 0
operation = 0
result = 0
action = 0

def doMath(num1, num2, operation):
    if(operation == '+'):
        return num1 + num2
    if(operation == '-'):
        return num1 - num2
    if(operation == '*'):
        return num1 * num2
    if(operation == '/'):
        return num1 / num2
    if(operation == '%'):
        return num1 % num2

while running:
    if(mode == 0):
        num1 = input("Enter the first number: ")
        operation = input("Enter the operation: ")
        num2 = input("Enter the second number: ")

        if(num1 == 'x' or num2 == 'x' or operation == 'x'):
            running = False
        else:
            result = round(doMath(int(num1), int(num2), operation), 2)
            print("\n" + num1 + " " + str(operation) + ' ' + num2 + " = " + str(result) + "\n")

        action = input("Press enter to continue, or type 'x' to go back: ")

        if(action == 'x'):
            mode = 2

    if(mode == 1):
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        if(num1 == 'x' or num2 == 'x' or operation == 'x'):
            running = False
        else:
            result = round(doMath(int(num1), int(num2), '+'), 2)
            print("\nThe sum of " + num1 + " and " + num2 + " equals " + str(result))
            result = round(doMath(int(num1), int(num2), '-'), 2)
            print("\nThe difference of " + num1 + " and " + num2 + " equals " + str(result))
            result = round(doMath(int(num1), int(num2), '*'), 2)
            print("\nThe product of " + num1 + " and " + num2 + " equals " + str(result))
            result = round(doMath(int(num1), int(num2), '/'), 2)
            print("\nThe quotient of " + num1 + " and " + num2 + " equals " + str(result))
            result = round(doMath(int(num1), int(num2), '%'), 2)
            print("\nThe moduluo of " + num1 + " and " + num2 + " equals " + str(result) + "\n")

        action = input("Press enter to continue, or type 'x' to go back: ")

        if(action == 'x'):
            mode = 2

    if(mode == 2):
        action = input("\nType '1' or '2' to select the desired mode, or press 'x' to exit: ")
        if(action == 'x'):
            running = False
        else:
            print("\n___MODE " + str(action) + "___\n")
            mode = int(action) - 1
