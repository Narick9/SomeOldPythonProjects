
import sys

import pygame

def run():
    """Основная функция программы"""
    pygame.init()
    pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Клавиши")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)

if __name__ == "__main__":
    run()
