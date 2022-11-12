import pygame
from random import randint
import math

width = 1200
height = 900
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
points = 0
numb = 0
a = 1.5  # ускоряющий коэффициент


def new_ball():
    ''' Рисует новый шарик, задающийся следующими параметрами:
    (x, y) - координаты центра
    r - радиус шарика
    color - случайный цвет шарика из выборки
    v - скорость шарика
    phi - угол между скоростью шарика и осью Ox
    '''

    global x, y, r
    x = randint(200, 800)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    v = 3
    phi = math.pi / randint(2, 6)
    n_b = [x, y, r, v, phi, color]
    pygame.draw.circle(screen, color, (x, y), r)
    balls.append(n_b)


def score(balls):
    ''' Производит подсчет очков игрока
    m_points - промежуточный счётчик очков
    points - итоговый счётчик очков
    '''

    global points
    m_points = 0
    for b in balls:
        if ((b[0] - event.pos[0]) ** 2 +
                (b[1] - event.pos[1]) ** 2) <= b[2] ** 2:
            m_points += 1
    points += m_points
    print('+', m_points)
    m_points = 0


def goal(balls):
    '''
    Считывание попадания мыши по шарику и удаление его с поля
    '''
    for b in balls:
        if ((b[0] - event.pos[0]) ** 2 +
                (b[1] - event.pos[1]) ** 2) <= b[2] ** 2:
            balls.remove(b)


def move(balls):
    '''
    Движение шарика по экрану и учёт его соударений с границами поля
    n_b = (x, y, r, v, phi, color) - список с данными о шарике
    '''
    vx = b[3] * math.cos(b[4])
    vy = b[3] * math.sin(b[4])
    b[0] += vx
    b[1] += vy
    pygame.draw.circle(screen, b[5], (b[0], b[1]), b[2])
    if (b[0] <= b[2]) and (vx < 0):  # левая граница
        b[0] += b[2] - b[0]
        b[4] = math.pi - b[4]
    if (b[0] + b[2] >= width) and (vx > 0):  # правая
        b[0] -= b[2] - width + b[0]          # граница
        b[4] = math.pi - b[4]
    if (b[1] <= b[2]) and (vy < 0):  # верхняя граница
        b[1] += b[2] - b[1]
        b[4] = -b[4]
    if (b[1] + b[2] >= height) and (vy > 0):  # нижняя
        b[1] -= b[1] - height + b[2]          # граница
        b[4] = -b[4]


pygame.init()
FPS = 30
screen = pygame.display.set_mode((width, height))
balls = []
pygame.display.update()
clock = pygame.time.Clock()
dt = clock.tick(FPS) / 1000
finished = False
count = 0
while not finished:
    screen.fill((255, 255, 255))
    clock.tick(FPS)
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Ваш счёт:', points)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score(balls)
            goal(balls)

    if count % 50 == 0:  # создание нового шара каждые 50 кадров
        new_ball()

    for b in balls:
        move(balls)
        if count % 200 == 0:  # ускорение игры каждые 200 кадров
            b[3] *= a

    pygame.display.update()

pygame.quit()
