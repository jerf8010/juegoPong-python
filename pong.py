import pygame, sys
import random
pygame.init()

size = (800, 600 )
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game_over = False

BLACK = ( 0, 0, 0 )
WHITE = ( 255, 255, 255 )
GREEN = ( 0, 255, 0 )
RED = ( 255, 0, 0 )
BLUE = ( 0, 0, 255 )

speed_y1 = 0
speed_y2 = 0

y1 = 255
y2 = 255

pelotax = 400
pelotay = 300

pelotax_speed = 5
pelotay_speed = 5


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_y2 = -4
            if event.key == pygame.K_DOWN:
                speed_y2 = +4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed_y2 = 0
            if event.key == pygame.K_DOWN:
                speed_y2 = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                speed_y1 = -4
            if event.key == pygame.K_x:
                speed_y1 = +4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                speed_y1 = 0
            if event.key == pygame.K_x:
                speed_y1 = 0


    if y1 < 0:
        y1 = 0
    if y1 > 510:
        y1 = 510

    if y2 < 0:
        y2 = 0
    if y2 > 510:
        y2 = 510

    y1 += speed_y1
    y2 += speed_y2

    if (pelotay < 10 or pelotay > 590):
        pelotay_speed *= -1


    if (pelotax < 10 or pelotax > 790 ):
        pelotax = 400
        pelotay = 300
        pelotax_speed *= -1
        pelotay_speed *= -1

    pelotax += pelotax_speed
    pelotay += pelotay_speed
    
    screen.fill(BLACK)

    jugador1 = pygame.draw.rect( screen, WHITE, ( 50, y1, 15, 90))
    jugador2 = pygame.draw.rect( screen, WHITE, ( 750, y2, 15, 90))
    pelota = pygame.draw.circle( screen, WHITE, (pelotax, pelotay), 10)


    if pelota.colliderect( jugador1 ) or pelota.colliderect( jugador2 ):
        pelotax_speed *= -1
    
    pygame.display.flip()
    clock.tick(30)