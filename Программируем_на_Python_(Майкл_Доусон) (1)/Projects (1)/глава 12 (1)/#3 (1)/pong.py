# Pong

from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 600, fps = 75)
    
class Player_board(games.Sprite):
    """Игрок-доска"""
    try:
        name_image = "board.png"
        image = games.load_image(name_image, transparent = False)
    except:
        print("Error: файл " + name_image + " не найден")
        exit()
    
    def __init__(self, player = 0):
        super().__init__(image = Player_board.image,
                         y = games.screen.height / 2)
        self.player = player
        self.score = games.Text(value = 0,
                                size = 150,
                                color = color.white,
                                top = 10)

        if self.player:
            self.right = games.screen.width / 8 * 7
            self.score.x = games.screen.width / 3 * 2
        else:
            self.left = games.screen.width / 8 * 1
            self.score.x = games.screen.width / 3 * 1
        
        games.screen.add(self)
        games.screen.add(self.score)

    def update(self):
        if self.player:
            if games.keyboard.is_pressed(games.K_UP):
                self.y -= 5
            if games.keyboard.is_pressed(games.K_DOWN):
                self.y += 5
        else:
            if games.keyboard.is_pressed(games.K_w):
                self.y -= 5
            if games.keyboard.is_pressed(games.K_s):
                self.y += 5
        
        if self.top < 0:
            self.top = 0
        if self.bottom > games.screen.height:
            self.bottom = games.screen.height

        for ball in self.get_overlapping_sprites():
            if self.player:
                ball.dx = -abs(ball.dx)
            else:
                ball.dx = abs(ball.dx)
            if self.left < ball.x < self.right:
                ball.dy = -ball.dy

    def win(self):
        self.score.value += 1

class Ball(games.Sprite):
    """Мяч"""
    try:
        name_image = "ball.png"
        image = games.load_image(name_image)
    except:
        print("Error: файл " + name_image + " не найден")
        exit()
    size_image = 30
    speed = 5 * size_image / games.screen.fps
    boost = 1 / 1000

    def __init__(self, left, right):
        super().__init__(image = Ball.image,
                         x = games.screen.width / 2,
                         y = random.randint(Ball.size_image,
                                games.screen.height - Ball.size_image),
                         dy = random.choice([-Ball.speed, Ball.speed]),
                         dx = random.choice([-Ball.speed, Ball.speed]))
        self.player_left = left
        self.player_right = right
        self.wait_time = 0
        
        games.screen.add(self)

    def update(self):
        if self.dx > 0:
            self.dx += Ball.boost
        elif self.dx < 0:
            self.dx -= Ball.boost
        if self.dy > 0:
            self.dy += Ball.boost
        elif self.dy < 0:
            self.dy -= Ball.boost
        
        if self.wait_time == 1:
            Ball(left = self.player_left, right = self.player_right)
            self.destroy()

        if self.top < 0 or self.bottom > games.screen.height:
            self.dy = -self.dy
        
        if self.right < 0 and not self.wait_time:
            player_right.win()
            self.wait_time = 5 * games.screen.fps
        if self.left > games.screen.width and not self.wait_time:
            player_left.win()
            self.wait_time = 5 * games.screen.fps

        if self.wait_time > 0:
            self.wait_time -= 1


def middle_line():
    line_image = games.load_image("middle.png", transparent = False)
    height = 0
    while height < games.screen.height:
        line = games.Sprite(image = line_image,
                            x = games.screen.width / 2,
                            top = height)
        games.screen.add(line)
        line_height = line.bottom - line.top
        height += line_height + line_height * 2


if __name__ == "__main__":
    player_left = Player_board(player = 0)
    player_right = Player_board(player = 1)
    Ball(left = player_left, right = player_right)
    
    middle_line()
    
    games.screen.event_grab = True
    games.mouse.is_visible = False

    games.screen.mainloop()









    
