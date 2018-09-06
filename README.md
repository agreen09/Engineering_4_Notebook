# Engineering 3 Notebook

This is where all of our stuff will go!

## Hello Python

### Lessons Learned

This assignment allowed us to become more familiar with how Python's format and syntax. It is much different than programming for the Arduino but after a coding for a bit we got used to it. By the end of the assignment, 
we knew how to write 'for' loops and print strings.

### [Code](https://github.com/agreen09/Engineering_4_Notebook/blob/master/Python/lesson00.py)

```python
import random


running = True
num = 0

while running:
    key = input("Press Enter to roll a die or press 'x' to exit: ")
    if(key == "x"):
        print("Exiting")
        running = False
    else:
        num = random.randint(1, 6)
        print("You rolled a " + str(num) + ".")
```

## Python - Calculator

### Lessons Learned

In this assignment we learned how to use user input to create a functioning interface, and we learned how to create and use functions. With this knowledge, we created a calculator program that adds, subtracts, multiplies,
and divides numbers, as well as finding modulos. We can easily add more operations if needed since we contained the calculations within a single function. 

### [Code](https://github.com/agreen09/Engineering_4_Notebook/blob/master/Python/calculator.py)

```python
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
```

## Python - Quad Solver

### Lessons Learned
		
The knowledge we gained from the calculator assignment helped us complete this one fairly easily. The only thing we had to research was how to find the square root of a number ( import math & math.sqrt() ). We spent
some extra time writing code to format the equation in a neat manner but the math side of this assignment was fairly easy.

### [Code](https://github.com/agreen09/Engineering_4_Notebook/blob/master/Python/quad_solver.py)

```python
import math

running = True

a = 0
b = 0
c = 0

equation = 0
result = 0
roots = [0, 0]

def solveQuad(a, b, c):
    return (b ** 2) - (4 * a * c)

def findRoots(a, b, c):
    return [((b * -1) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a), ((b * -1) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)]


while(running):
    if(input("Press enter to continue or 'x' to exit: ") == 'x'):
        running = False
    else:
        a = int(input("Input the coefficient for x^2: "))
        b = int(input("Input the coefficient for x: "))
        c = int(input("Input the y-intercept: "))

        #generate the equation string in three passes (for readability)
        equation = "x^2" if (a == 1) else (str(a) + "x^2")
        if(not b == 0):
            equation += " + x" if (b == 1) else " - x" if (b == -1) else ((" - " + str(b * -1)) if (b < 0) else (" + " + str(b))) + "x"
        if(not c == 0):
            equation += (" - " + str(c * -1)) if (c < 0) else (" + " + str(c))
        
        result = solveQuad(a, b, c)

        if(result < 0):
            print(equation + " has no roots.\n")
        else:
            roots = findRoots(a, b, c)
            
            if(roots[0] == roots[1]):
                print("The root of " + equation + " is: " + str(roots[0]) + "\n")
            else:
                print("The roots of " + equation + " are: " + str(roots[0]) + ", " + str(roots[1]) + "\n")
```
