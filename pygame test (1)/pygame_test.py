# Изучение новой библиотеки

import pygame
import random

WIDTH = 640
HEIGHT = 480
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

r = 5
g = 5
b = 5

b_r = True
b_g = True
b_b = True
def new_colour():
    global r, g, b
    global b_r, b_g, b_b

    if r <= 4 or r >= 250:
        b_r = not b_r
    if g <= 4 or g >= 250:
        b_g = not b_g
    if b <= 4 or b >= 250:
        b_b = not b_b
        
    if b_r:
        r += random.randint(1, 5)
    else:
        r -= random.randint(1, 5)
    if b_g:
        g += random.randint(1, 5)
    else:
        g -= random.randint(1, 5)
    if b_b:
        b += random.randint(1, 5)
    else:
        b -= random.randint(1, 5)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

    screen.fill((r, g, b))
    new_colour()
        
    pygame.display.flip()

pygame.quit()
