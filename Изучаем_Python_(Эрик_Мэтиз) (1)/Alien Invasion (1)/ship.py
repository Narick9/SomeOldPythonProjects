
import time

import pygame

from bullet import Bullet


if __name__ == "__main__":
    print("\nThis is a module. It should be imported.")
    input("Press enter to continue...")
    

class Ship():
    """Класс представления корабля и его основных действий"""

    IMAGE = pygame.image.load("images/ship.bmp")

    def __init__(self, screen, settings, keyboard):
        """Инициализация основных атрибутов корабля"""
        self.settings = settings
        self.keyboard = keyboard
        self.screen = screen
        self.image = Ship.IMAGE
        self.bullets = []

        # Для картинки
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = self.rect.centerx

        # Для времени
        self.last_bullet_time = 0

    def blitme(self):
        """Выводит корабль на экран"""
        self.screen.blit(self.image, self.rect)

    def bullet_work(self):
        """Работает с пульками"""
        # Если после последнего выстрела прошло больше 2 секунд
        # и нажат пробел, то можно выпустить новую пульку
        bullet_time_difference = time.time() - self.last_bullet_time
        delay = self.settings["bullet"]["delay"]
        if bullet_time_difference > delay and self.keyboard[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.settings["bullet"],
                                       self.screen,
                                       self.rect.centerx,
                                       self.rect.top))
            self.last_bullet_time = time.time()

        for bullet in self.bullets[:]:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
            bullet.update()

    def moving(self):
        """Корабль реагирует на команды"""
        if self.keyboard[pygame.K_LEFT]:
            self.centerx -= self.settings["speed"]
        if self.keyboard[pygame.K_RIGHT]:
            self.centerx += self.settings["speed"]
        self.rect.centerx = self.centerx

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def update(self):
        """Обновление корабля с каждым кадром"""
        self.moving()
        self.bullet_work()
        self.blitme()
