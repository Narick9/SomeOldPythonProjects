
import sys

import pygame


class Person():
    """Игровой персонаж"""

    IMAGE = pygame.image.load("images\person.jpg")
    
    def __init__(self, screen):
        """Инициализирует основные атрибуты и положение картинки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = Person.IMAGE.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Выводит персонажа на экран"""
        self.screen.blit(Person.IMAGE, self.rect)


WHITE = (255, 255, 255)
RESOLUTION = (800, 600)
CAPTION = "Игровой персонаж"

def run_display_person():
    """Создаёт экран и добавляет на него персонажа"""

    pygame.init()

    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(CAPTION)

    player = Person(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(WHITE)
        player.blitme()
        
        pygame.display.flip()


run_display_person()        
        
