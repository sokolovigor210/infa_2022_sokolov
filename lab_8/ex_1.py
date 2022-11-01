import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 120)
#левый глаз
circle(screen, (255, 0, 0), (140, 150), 25)
circle(screen, (0, 0, 0), (140, 150), 10)
# правый глаз
circle(screen, (255, 0, 0), (260, 150), 20)
circle(screen, (0, 0, 0), (260, 150), 10)
#граница
circle(screen, (0, 0, 0), (200, 175), 120, 1)
#рот
rect(screen, (0, 0, 0), (140, 220, 120, 20))
#брови (левая и правая соответственно)
##circle(screen, (255, 0, 0), (140, 150), 25)##
polygon(screen, (0, 0, 0), [(110, 105), (110,125), (190,145), (190,125)])
polygon(screen, (0, 0, 0), [(210,145), (210,125), (290,100), (290,120)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()