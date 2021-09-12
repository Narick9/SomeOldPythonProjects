
import time

import pygame

from bullet import Bullet


if __name__ == "__main__":
    print("\nThis is a module. It should be imported.")
    input("Press enter to continue...")
    

class Ship():
    """Класс представления корабля и его основных действий"""

    IMAGE = pygame.image.load("images/rocket.bmp")

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

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.centery = self.rect.centery

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
                                       self.rect.centery,
                                       self.rect.right))
            self.last_bullet_time = time.time()

        for bullet in self.bullets[:]:
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
            bullet.update()

    def moving(self):
        """Корабль реагирует на команды"""
        if self.keyboard[pygame.K_UP]:
            self.centery -= self.settings["speed"]
        if self.keyboard[pygame.K_DOWN]:
            self.centery += self.settings["speed"]
        self.rect.centery = self.centery

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom

    def update(self):
        """Обновление корабля с каждым кадром"""
        print(len(self.bullets))
        self.moving()
        self.bullet_work()
        self.blitme()
