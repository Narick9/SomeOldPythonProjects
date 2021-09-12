
import sys

import pygame

RESOLUTION = (800, 600)
CAPTION = "Ракета"
WHITE = (255, 255, 255)

keyboard = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    }
settings = {
    "rocket_speed_factor": 1
    }

class Rocket():
    """Представляет интерактивную ракету"""
    IMAGE = pygame.image.load("images/rocket.bmp")
    
    def __init__(self, screen, settings, keyboard):
        """Инициализирует основные атрибуты"""
        self.screen = screen
        self.settings = settings
        self.keyboard = keyboard

        self.rect = Rocket.IMAGE.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.center = {
            "x": self.rect.centerx,
            "y": self.rect.centery,
            }

    def show(self):
        """Выводит картинку ракеты на экран"""
        self.screen.blit(Rocket.IMAGE, self.rect)

    def moving(self):
        """
        Если нажата одна из нужных клавиш, то передвегает ракету по экрану.
        """
        if self.keyboard[pygame.K_UP]:
            self.center["y"] -= self.settings["rocket_speed_factor"]
        if self.keyboard[pygame.K_DOWN]:
            self.center["y"] += self.settings["rocket_speed_factor"]
        if self.keyboard[pygame.K_LEFT]:
            self.center["x"] -= self.settings["rocket_speed_factor"]
        if self.keyboard[pygame.K_RIGHT]:
            self.center["x"] += self.settings["rocket_speed_factor"]

        self.rect.centerx = self.center["x"]
        self.rect.centery = self.center["y"]

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def update(self):
        """Обновление ракеты каждый кадр"""
        self.moving()
        self.show()
        

def play():
    """Оснавная функция игры"""
    pygame.init()

    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)

    player = Rocket(screen, settings, keyboard)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keyboard[event.key] = True
                print("1")
            if event.type == pygame.KEYUP:
                keyboard[event.key] = False

        screen.fill(WHITE)
        player.update()
        
        pygame.display.flip()


if __name__ == "__main__":
    play()
