import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0

def new_ball():
    '''
    Рисует новый шарик.
    x, y - координаты центра шарика на экране, являющиеся случайными целыми числами.
    r - радиус шарика, являющийся случайным целым числом.
    color - цвет шарика, который произвольно выбирается из массива цветов, созданного ранее,
            заданный в формате, подходящем для pygame.Color.
    '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def score():
    '''
    Выводит текстовые сообщения о том, попал ли игрок в шарик, пересчитывая итог при каждом успешном клике
    points - счёт игрока
    x, y, r - координаты и радиус шарика, находящегося на экране
    '''
    global points
    if ((x-pygame.mouse.get_pos()[0])**2 + (y-pygame.mouse.get_pos()[1])**2) <= r**2:
        print('Goal!')
        points += 1
    else:
        print ('Miss!')


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Итого очков: ', points)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score()

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()