running = True

string = None

while(running):
    if(input("Press enter to continue or 'x' to exit: ") == 'x'):
        running = False
    else:
        string = input("\nEnter some text: ")
        print("")
        for i in string:
            print(i)
        print("")
