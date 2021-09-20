import pygame
import sys
from random import randint

pygame.init()

row = [0 for x in range(18)]
rows = [row for x in range(18)]

black = (0, 0, 0)
red = (199, 20, 53)
green = (98, 207, 14)
white = (255, 255, 255)
blue = (102, 135, 255)

to_up = False
to_down = False
to_right = False
to_left = False

widthOfCell = 30
food = 0

snake = [[randint(2,15), randint(2,15)]]

sc = pygame.display.set_mode([485,485])

pygame.display.set_caption("Snake")

z, w = 0, 0
clock = pygame.time.Clock()
fps = 5
eatan = False

while True:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and to_down == False:
                z, w = 0, -1
                to_up = True
                to_left = to_right = to_down = False
            elif event.key == pygame.K_DOWN and to_up == False:
                z, w = 0, 1
                to_down = True
                to_left = to_right = to_up = False
            elif event.key == pygame.K_LEFT and to_right == False:
                z, w = -1, 0
                to_left = True
                to_up = to_down = to_right = False
            elif event.key == pygame.K_RIGHT and to_left == False:
                z, w = 1, 0
                to_right = True
                to_up = to_down = to_left = False

    snake.append([snake[-1][0]+z, snake[-1][1]+w])

    if not(eatan):
        del snake[0]
    else:
        eatan = False

    if snake[-1][0] == 0 or snake[-1][0] == 17 or snake[-1][1] == 0 or snake[-1][1] == 17:
        sys.exit()

    sc.fill(black)

    for x in range(1,17):
        for y in range(1,17):
            pygame.draw.rect(sc,blue, [(2+(x-1)*widthOfCell)+1, (2+(y-1)*widthOfCell)+1, widthOfCell-1, widthOfCell-1])

    if not(food):
        Ox, Oy = randint(1,16), randint(1,16)
        pygame.draw.rect(sc, red, [(2+(Ox-1)*widthOfCell)+1, (2+(Oy-1)*widthOfCell)+1, widthOfCell-1, widthOfCell-1])
        food = 1
    else:
        pygame.draw.rect(sc, red, [(2+(Ox-1)*widthOfCell)+1, (2+(Oy-1)*widthOfCell)+1,widthOfCell-1, widthOfCell-1])

    if snake[-1][0] == Ox and snake[-1][1] == Oy:
        food = False
        eatan = True

    for x in range(len(snake)-1):
        if snake[x] == snake[-1] and len(snake) > 1:
            sys.exit()

    for sn in snake:
        pygame.draw.rect(sc, green, [(2+(sn[0]-1)*widthOfCell)+1, (2+(sn[1]-1)*widthOfCell)+1,widthOfCell-1, widthOfCell-1])

    pygame.display.flip()