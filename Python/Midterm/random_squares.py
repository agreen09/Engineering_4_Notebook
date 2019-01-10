import pygame
import random

WIDTH = 500
HEIGHT = 500

pygame.init()

pygame.display.set_caption('Midterm!!')
screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

print("Window initialized successfully")

num = int(input("Enter # of squares (0 = fill entire screen): "))

counter = 0
renderCounter = 0

background = (51, 153, 255)
colors = [[], [], []]

def screenFilled():
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            pixel = screen.get_at((i, j))[:3]
            if pixel == background:
                return False
    return True            

def randomColor(tc1, tc2, tc3):
    #print('')
    #print(counter)
    #print(str(tc1) + ', ' + str(tc2) + ', ' + str(tc3))
    #print(colors)
    for i in range(0, len(colors[0])):
        if(tc1 == colors[0][i] and tc2 == colors[1][i] and tc3 == colors[2][i]):
            print('')
            print(counter)
            print(str(tc1) + ', ' + str(tc2) + ', ' + str(tc3))
            #print(str(colors[0][i]) + ', ' + str(colors[1][i]) + ', ' + str(colors[2][i]))
            return False
    
    colors[0].append(tc1)
    colors[1].append(tc2)
    colors[2].append(tc3)
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(background)
    
    

    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)

    if(num > 0):
        for i in range(0, num):
            while True:
                counter += 1
                renderCounter += 1
                c1 = random.randint(0, 255)
                c2 = random.randint(0, 255)
                c3 = random.randint(0, 255)
                if(randomColor(c1, c2, c3)):
                    break
            color = (c1, c2, c3)
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            pygame.draw.rect(screen, color, (x, y, 10, 10), 0)
            if(renderCounter > 100):
                pygame.display.update()
                renderCounter = 0

    else:
        while(not screenFilled):
            while True:
                counter += 1
                renderCounter += 1
                c1 = random.randint(0, 255)
                c2 = random.randint(0, 255)
                c3 = random.randint(0, 255)
                if(randomColor(c1, c2, c3)):
                    break
            color = (c1, c2, c3)
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            pygame.draw.rect(screen, color, (x, y, 10, 10), 0)
            if(renderCounter > 100):
                pygame.display.update()
                renderCounter = 0
    
    pygame.display.update()
    running = False
                                 


while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
