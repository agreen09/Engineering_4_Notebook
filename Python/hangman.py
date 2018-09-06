import os

numWrong = 0
running = True
guessing = False
word = None
wordArray = []
guess = None
current = []
hits = []
drawing = [
    '  O\n',
    ' /',
    '|',
    '\\\n',
    '  | \n',
    ' / ',
    '\\']

def drawUI():
    os.system('clear')
    print(''.join(current))
    print('__\n  |')
    print(''.join(drawing[0:numWrong]))

while(running):
    if(guessing == False):
        numWrong = 0
        wordArray = []
        current = []
        hits = []
        os.system('clear')
        word = input("Player 1, enter a word: ").lower()
        for i in word:
            wordArray.append(i)
            current.append('_ ')
            hits.append(False)
        guessing = True
        os.system('clear')
    else:
        guess = input("Player 2, enter a letter to guess: ")
        if(guess == '/exit'):
            running = False
        else:
            counter = 0
            for i in range(0, len(wordArray)):
                if(wordArray[i] == guess):
                    hits[i] = True
                else:
                    counter += 1

            for i in range(0, len(current)):
                if(hits[i] == True):
                    current[i] = wordArray[i] + ' '
            if(counter == len(wordArray)):
                numWrong += 1
                
            drawUI()

            counter = 0
            for i in hits:
                if(i == True):
                    counter += 1
            if(counter == len(wordArray)):
                if(input("Congratulations, you won! Would you like to play again? (y/n): ") == 'y'):
                    guessing = False
                else:
                    running = False
            if(numWrong > len(drawing) - 1):
                if(input("Sorry, you lost! The word was " + str(word) + "\nWould you like to play again? (y/n): ") == 'y'):
                    guessing = False
                else:
                    running = False
        
        
