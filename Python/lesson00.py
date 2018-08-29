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
    

    
