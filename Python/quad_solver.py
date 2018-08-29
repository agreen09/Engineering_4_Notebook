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
