# По условию задачи №3 главы 11

from livewires import games, color

games.init(screen_width = 800, screen_height = 600, fps = 75)

class Player_board(games.Sprite):
    """Игрок-доска"""
    try:
        name_image = "board_mod.png"
        image = games.load_image(name_image, transparent = False)
    except:
        print("Error: файл " + name_image + " не найден")
        exit()
    
    def __init__(self):
        super().__init__(image = Player_board.image,
                         x = games.mouse.x,
                         bottom = games.screen.height)
        games.screen.add(self)

    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        if self.top < 0:
            self.top = 0
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height

        for ball in self.get_overlapping_sprites():
            if ((ball.bottom > self.top or self.bottom > ball.top)
                and ball.x > self.left and self.right > ball.x):
                ball.dy = -ball.dy
            if ((ball.right > self.left or self.right > ball.left)
                and ball.y > self.top and self.bottom > ball.y):
                ball.dx = -ball.dx

class Ball(games.Sprite):
    """Мяч"""
    try:
        name_image = "ball.png"
        image = games.load_image(name_image)
    except:
        print("Error: файл " + name_image + " не найден")
        exit()
    size_image = 30
    speed = 2 * size_image / games.screen.fps

    def __init__(self):
        super().__init__(image = Ball.image,
                         x = games.screen.width / 2,
                         y = games.screen.height / 2,
                         dx = Ball.speed, dy = Ball.speed)
        games.screen.add(self)

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            game_over()


def game_over():
    msg_over = games.Message(value = "GAME OVER",
                       size = 50,
                       color = color.red,
                       x = games.screen.width / 2,
                       y = games.screen.height / 2,
                       lifetime = games.screen.fps * 5,
                       after_death = exit)
    games.screen.add(msg_over)

if __name__ == "__main__":
    Player_board()
    Ball()

    games.screen.event_grab = True
    games.mouse.is_visible = False

    games.screen.mainloop()









    
