import pygame
from pygame.draw import *
from random import randint
import math
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
    N - количество шариков, одновременно находящихся на экране, являющееся случайным числом.
    color - цвет шарика, который произвольно выбирается из массива цветов, созданного ранее,
            заданный в формате, подходящем для pygame.Color.
    v - скорость шарика
    '''
    global x, y, r, N, A, v, phi, color
    N = randint(1, 4)
    A=[]
    for i in range (N):
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        v = randint(1,5)
        phi = randint(0, 3) * math.pi/6
        A.append((x,y,r))
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)

#def motion():
    #for i in range (N):


def score():
    '''
    Производит подсчет очков игрока.
    m_points - промежуточное значение счёта игрока, которое выводится на экран при каждом попадании
    points - счёт игрока, который выводится в конце игрового сеанса
    A - массив списков, каждый из которых вида [x, y, r] - координаты центра шарика и его радиус
    '''
    global points
    m_points = 0
    for i in range(N):
        if ((A[i][0]-pygame.mouse.get_pos()[0])**2 + (A[i][1]-pygame.mouse.get_pos()[1])**2) <= A[i][2]**2:
            m_points += 1
    points += m_points
    print('+', m_points)
    m_points = 0



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
    pygame.time.delay(100)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()