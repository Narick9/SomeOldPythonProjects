# Pong

import random

import pygame
import pygame.locals as pylocals


class PlayerBoard():
    """Игрок-доска"""

    def __init__(self, screen, key_dc, settings, side):
        self.screen = screen
        self.settings = settings
        self.side = side

        dis = settings["distance_from_side"]
        if side == "left":
            x = screen.get_width()/dis - settings["width"]/2
        elif side == "right":
            x = screen.get_width()/dis*(dis - 1) - settings["width"]/2
        y = (screen.get_height() - settings["height"])/2
        
        self.rect = pygame.Rect(x, y, settings["width"], settings["height"])

    def moving(self):
        """Перемещает игрока по командам"""
        new_top = self.rect.top
        if key_dc[self.settings[self.side]["up"]]:
            new_top -= self.settings["speed"]
        if key_dc[self.settings[self.side]["down"]]:
            new_top += self.settings["speed"]

        if (    new_top < 0
             or new_top + self.settings["height"] > self.screen.get_height()
            ):
            return
        self.rect.top = new_top

    def update(self):
        """Перемещает и выводит на экран игрока"""
        self.moving()
        pygame.draw.rect(self.screen, self.settings["colour"], self.rect)


class Ball():
    """Мяч"""

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        speed = settings["speed"]
        self.dx = random.choice((-speed, speed))
        self.dy = random.choice((-speed, speed))

        x_pos = screen.get_width()/2
        y_pos = random.randrange(screen.get_height())
        radius = settings["radius"]

        self.rect = pygame.Rect(x_pos, y_pos, 2*radius, 2*radius)

    def moving(self):
        """Перемещает мячик по экрану и обрабатывает отскоки от стен"""
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.dy = -self.dy
            
    
    def update(self):
        """Перемещает и выводит мячик на экран"""
        self.moving()
        pygame.draw.circle(screen, self.settings["colour"],
                           (self.rect.centerx, self.rect.centery),
                           self.settings["radius"])

        
class MiddleLine():
    """Разделяющая линия посередине экрана"""

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.line_rects = []

        self.make_middle_line()

    def make_middle_line(self):
        """Строит линии"""
        x = (self.screen.get_width() - self.settings["width"]) / 2
        top = 0
        while top + self.settings["height"] < self.screen.get_height():
            line = pygame.Rect(x, top,
                               self.settings["width"], self.settings["height"])
            self.line_rects.append(line)
            top += self.settings["height"] + self.settings["distance"]

    def update(self):
        """Выводит все части линии на экран"""
        for rect in self.line_rects:
            pygame.draw.rect(self.screen, self.settings["colour"], rect)


class Pong():
    """Сама игра и всё, что в ней"""

    def __init__(self, screen, key_dc, settings):
        self.screen = screen
        self.key_dc = key_dc
        self.settings = settings
        self.sprites = []

        self.ball = Ball(screen, settings["ball"])
        self.sprites.append(self.ball)

        self.players = []
        for side in ("left", "right"):
            player = PlayerBoard(screen, key_dc, settings["player"], side)
            self.players.append(player)
        self.sprites += self.players

        self.sprites.append(MiddleLine(screen, settings["middle_line"]))

    def collider(self):
        """Обрабатывает столкновения"""
        for player in self.players:
            if self.ball.rect.colliderect(player.rect):
                if player.side == "left":
                    self.ball.dx = abs(self.ball.dx)
                if player.side == "right":
                    self.ball.dc = -abs(self.ball.dx)
                if player.rect.left < self.ball.rect.centerx < player.rect.right:
                    self.ball.dy = - self.ball.dy
            
    def update(self):
        self.collider()
        for sprite in self.sprites:
            sprite.update()

        
settings = {
    "display": {
        "resolution": (800, 600),
        "fps": 75,
        "caption": "Pong",
        "background_colour": (0, 0, 0),
    },
    "game": {
        "middle_line": {
            "width": 2,
            "height": 10,
            "distance": 20,
            "colour": (255, 255, 255),
        },
        "player": {
            "width": 10,
            "height": 80, #30
            "colour": (255, 255, 255),
            "speed": 10,
            "distance_from_side": 8,
            "left": {
                "up": pylocals.K_w,
                "down": pylocals.K_s,
            },
            "right": {
                "up": pylocals.K_UP,
                "down": pylocals.K_DOWN,
            },
        },
        "ball": {
            "radius": 5,
            "colour": (255, 255, 255),
            "speed": 3,
        },
    }
}


def keyboard_update(key_dc):
    """Регестрирует нажатые клавиши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            key_dc[event.key] = True
        if event.type == pygame.KEYUP:
            key_dc[event.key] = False
    
        
if __name__ == "__main__":
    pygame.init()
    key_dc = {i: False for i in range(300)}

    dis_settings = settings["display"]
    screen = pygame.display.set_mode(dis_settings["resolution"], 0, 32)
    pygame.display.set_caption(dis_settings["caption"])
    FrameTime = pygame.time.Clock()

    pong = Pong(screen, key_dc, settings["game"])

    active = True
    pause = False
    while active:
        FrameTime.tick(dis_settings["fps"])
        
        keyboard_update(key_dc)
        if key_dc[pylocals.K_ESCAPE]:
            active = False
        if key_dc[pylocals.K_SPACE]:
            pause = not pause

        screen.fill(dis_settings["background_colour"])    
        if not pause:
            pong.update()
                
        pygame.display.flip()
    pygame.quit()

