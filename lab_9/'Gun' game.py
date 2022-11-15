import math
from random import choice
from random import randint as rnd
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
shots = 0
my_time = 0  # счётчик кадров - для реализованного пока не нужен
mini_count = 0

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball.

        Args:
        x - начальное положение мяча по горизонтали;
        y - начальное положение мяча по вертикали.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self, dt):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки.
        То есть, обновляет значения self.x и self.y
            с учетом скоростей self.vx и self.vy, силы гравитации
                и стен по краям окна (размер окна 800х600).
        """
        if gun.color == RED:
            self.color = RED
        elif gun.color == YELLOW:
            self.color = YELLOW
        elif gun.color == MAGENTA:
            self.color = MAGENTA
        self.ky = 0.4  # коэффициент затухания скорости vy при соударении
        self.kx = 0.4  # коэффициент затухания скорости vx при соударении
        self.g = 1  # ускорение свободного падения
        self.vy += self.g * dt
        self.x += self.vx * dt
        self.y += self.vy * dt + (self.g * dt ** 2) / 2
        if self.y + self.r >= HEIGHT and self.vy > 0:
            self.vy = -self.vy * self.ky
            self.y -= self.y + self.r - HEIGHT
        if self.x + self.r >= WIDTH and self.vx > 0:
            self.vx = -self.vx * self.kx
            self.x -= self.x + self.r - WIDTH

    def stop(self, balls):
        """
        Останавливает и удаляет мяч, который остановился на нижней границе окна.

        Args:
        balls - массив, в котором хранятся снаряды пушки.
        """
        if self.y + self.r == HEIGHT:
            self.live -= 6
        if self.live < 5:
            self.vx = 0
        if self.live <= 0:
            pygame.time.delay(10)
            balls.remove(b)

    def draw(self):
        """Рисует новый снаряд пушки."""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью,
                описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели.
                В противном случае возвращает False.
        """
        if abs(obj.x - self.x) <= (self.r + obj.r) and \
                abs(obj.y - self.y) <= (self.r + obj.r):
            return True
        else:
            return False


class Gun:
    """Конструктор класса Gun."""
    def __init__(self, screen, x, y):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = x
        self.y = y
        self.tx = 0
        self.ty = 0
        self.ux = 0
        self.uy = 5
        self.color = choice([RED, YELLOW, MAGENTA])
        self.n = 1.25  # множитель мощности пушки
        self.n_max = 25  # максимальная мощность пушки

        self.color_corpus = GREY  # превращение пушки в танк
        self.width = 20  # характеристики корпуса пушки
        self.height = 30

    def fire2_start(self, event):
        """Инициализация стрельбы из пушки."""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy
            зависят от положения мыши.
        """

        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0] -
                                                         new_ball.x))
        new_ball.vx = self.n * self.f2_power * math.cos(self.an)
        new_ball.vy = self.n * self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def movement(self, dt):
        """Осуществление движения пушки по игровому полю в некоторых пределах.

        Args:
        dt - время, которое прошло с предыдущего кадра
        """
        self.y += self.uy * dt
        if self.y - self.height / 2 <= 100 or self.y + \
                self.height / 2 >= HEIGHT - 100:
            self.uy = -self.uy

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""

        if event:
            self.tx = event.pos[0]
            self.ty = event.pos[1]
            if (event.pos[0]-self.y) == 0:
                self.an = 0
            else:
                self.an = math.atan((event.pos[1]-self.x) /
                                    (event.pos[0]-self.y))
            if self.f2_on:
                self.color = (0, 255, 0)

    def draw(self):
        """Рисование пушки на экране при прицеливании."""
        dx = self.tx - self.x
        dy = self.ty - self.y
        r = (dx**2 + dy**2)**0.5
        dx *= self.f2_power * 4 / r
        dy *= self.f2_power * 4 / r
        pygame.draw.line(self.screen, self.color, (self.x, self.y),
                         (self.x+dx, self.y + dy), 7)
        pygame.draw.rect(self.screen, self.color_corpus, (self.x -
                         self.width / 2, self.y - self.height / 2,
                         self.width, self.height), 10)

    def power_up(self):
        """Осуществление зарядки и увеличении мощности пушки при стрельбе."""
        if self.f2_on:
            if self.f2_power < self.n_max:
                self.f2_power += 1
            self.color = GREEN


class Target:
    def __init__(self, screen):
        """Конструктор класса Target."""
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()
        self.Vy = 5
        self.Vx = 3

    def motion(self, dt):  # в планах реализовать окружность
        """Осуществление движения цели в некотором пространстве."""
        self.y += self.Vy * dt
        self.x += self.Vx * dt
        if self.y - self.r <= 100 or self.y + self.r >= HEIGHT - 50:
            self.Vy = -self.Vy
        if self.x + self.r >= WIDTH or self.x - self.r <= WIDTH / 2 :
                self.Vx = -self.Vx

    def new_target(self):
        """Инициализация новой цели."""
        x = self.x = rnd(500, 730)
        y = self.y = rnd(100, 500)
        r = self.r = rnd(5, 40)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        """Рисование цели."""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Игра \"Пушка\" ")

bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen, 50, 450)
target = Target(screen)
finished = False
dt = clock.tick(FPS) / 60  # рекомендуемое значение для dt, 
                             # полученное в ходе эксперимента

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target.live = 1
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Уничтожено целей:', target.points)
            print('Потрачено выстрелов:', shots)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            shots += 1
            mini_count += 1
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    gun.movement(dt)
    target.motion(dt)
    for b in balls:
        b.move(dt)
        b.stop(balls)
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
            print('Вы уничтожили цель за', mini_count, 'выстрелов (-а)!')
            # есть баг, если одним снарядом уничтожить 2 цели одновременно
            mini_count = 0

    gun.power_up()