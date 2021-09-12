
import sys

import pygame


blue = (0, 0, 130)

def run_blue_screen():
    """Создаёт окно с синим фоном"""
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Синее небо")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(blue)

        pygame.display.flip()


run_blue_screen()
