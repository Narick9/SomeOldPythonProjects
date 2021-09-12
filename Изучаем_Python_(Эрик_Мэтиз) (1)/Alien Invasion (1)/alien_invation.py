import time

import pygame

from ship import Ship

settings = {
    "display": {
        "fps": 15,
        "width": 800,
        "height": 600,
        "caption": "Alien Invasion",
        "back_ground_colour": (230, 230, 230),
        },
    "ship": {
        "speed": 8,
        "bullet": {
            "width": 3,
            "height": 15,
            "speed": 1,
            "colour": (0, 0, 0),
            "delay": 2,
            },
        },
    }
keyboard = {key: False for key in range(300)}

def run_game():
    """Основная фукнция игры. Создает игру и меняет кадры"""
    pygame.init()

    screen = pygame.display.set_mode((settings["display"]["width"],
                                      settings["display"]["height"]))
    pygame.display.set_caption(settings["display"]["caption"])

    ship = Ship(screen, settings["ship"], keyboard)
    
    last_frame_time = 0
    delay = 1/settings["display"]["fps"]

    play = True
    while play:
        if time.time() - last_frame_time < delay:
            time.sleep(delay)
        last_frame_time = time.time()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                keyboard[event.key] = True
            if event.type == pygame.KEYUP:
                keyboard[event.key] = False

        screen.fill(settings["display"]["back_ground_colour"])
        ship.update()

        pygame.display.flip()
        last_frame_time = time.time()

    pygame.quit()


if __name__ == "__main__":
    run_game()
