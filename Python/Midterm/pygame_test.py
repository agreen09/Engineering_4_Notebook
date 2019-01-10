import pygame
import random

pygame.init()

pygame.display.set_caption('Midterm!!')
screen = pygame.display.set_mode((1000,1000))

running = True

print("Window initialized successfully")

def randomColor(tc1, tc2, tc3):
    for i in range(0, len(colors[0])):
        if(tc1 == colors[0][i] and tc2 == colors[1][i] and tc3 == colors[2][i]):
            print(str(tc1) + ', ' + str(tc2) + ', ' + str(tc3))
            return False
    else:
        colors[0].append(tc1)
        colors[1].append(tc2)
        colors[2].append(tc3)
        return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((51, 153, 255))
    
    colors = [[], [], []]

    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)

    for i in range(0, 1000):
        while(not randomColor(c1, c2, c3)):
            c1 = random.randint(0, 255)
            c2 = random.randint(0, 255)
            c3 = random.randint(0, 255)
        color = (c1, c2, c3)
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        pygame.draw.rect(screen, color, (x, y, 10, 10), 0)
    
    pygame.display.flip()
    running = False
                                 


while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
