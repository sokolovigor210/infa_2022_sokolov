import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''
    Рисует новый шарик.
    x, y - координаты центра шарика на экране, являющиеся случайными целыми числами.
    r - радиус шарика, являющийся случайным целым числом.
    N - количество шариков, одновременно находящихся на экране, являющееся случайным числом.
    color - цвет шарика, который произвольно выбирается из массива цветов, созданного ранее,
            заданный в формате, подходящем для pygame.Color.
    v - скорость шарика
    '''
    global x, y, r, N
    N = randint(1, 4)
    A=[]
    for i in range (N):
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)

def click(event):
    '''
    Определяет координаты шарика, находящегося на экране.
    event - событие, представляющее собой клик мыши по экрану
    N - количество шариков, находящихся на экране
    '''
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()