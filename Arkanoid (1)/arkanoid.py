# Классический Arkanoid

from livewires import games, color

games.init(screen_width = 800, screen_height = 600, fps = 75)
fps = games.screen.fps



def get_image_info(image, choice):
    sprite = games.Sprite(image = image)

    if choice == "width":
        return sprite.width
    if choice == "height":
        return sprite.height
    else:
        printe(choice, "не определён в get_image_info")
        exit()

class Board(games.Sprite):
    """Доски, которые сбивают"""

    image = games.load_image("board.png")
    image_width = get_image_info(image, "width")
    image_height = get_image_info(image, "height")


class Ball(games.Sprite):
    """Отталкивающийся шарик"""

    image = games.load_image("ball.png")
    image_size = get_image_info(image, "width")

    def __init__(self, game, speed):
        speed = Ball.image_size * speed / fps
        super().__init__(image = Ball.image,
                         x = game.player.x,
                         bottom = game.player.top,
                         dx = speed,
                         dy = speed)

        self.map_bottom = game.map_buffer + game.map_height - Arkanoid.map_image_size

    def update(self):
        for sprite in  self.overlapping_sprites:
            if sprite.left < self.x < sprite.right:
                self.dy = - self.dy
            if sprite.top < self.y < sprite.bottom:
                self.dx = - self.dx

            if type(sprite) == Board:
                game.boards.remove(sprite)
                sprite.destroy()

        if not game.boards:
            game.play()
        if self.bottom >= self.map_bottom:
            game.game_over()
    

class Player(games.Sprite):
    """Игрок-доска"""

    image = games.load_image("player_board.png", transparent = False)
    image_width = get_image_info(image, "width")

    def __init__(self, map_left, map_right, bottom, speed):
        self.speed = speed * Player.image_width / fps
        self.map_left = map_left
        self.map_right = map_right

        super().__init__(image = Player.image,
                        x = (map_left + map_right) / 2,
                        bottom = bottom)

    def update(self):
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= self.speed
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += self.speed
            
        if self.left < self.map_left:
            self.left = self.map_left
        if self.right > self.map_right:
            self.right = self.map_right

class Arkanoid():
    """Сама игра и всё что в ней"""

    map_image = games.load_image("wall.png")
    map_image_size = get_image_info(map_image, "width")
    
    
    def __init__(self,
                 map_buffer = 50,
                 map_part_x = 32,
                 map_part_y = 40,
                 player_speed = 5,
                 ball_speed = 18):
        self.lvl = 0
        
        self.map_buffer = map_buffer
        self.map_part_x = map_part_x
        self.map_part_y = map_part_y
        self.map_width = map_part_x * Arkanoid.map_image_size
        self.map_height = map_part_y * Arkanoid.map_image_size

        self.player_speed = player_speed
        self.ball_speed = ball_speed

        self.player = None
        self.ball = None
        self.boards = []

        self.make_map()

    def play(self):
        self.lvl += 1
        
        if self.player:
            self.player.destroy()
        if self.ball:
            self.ball.destroy()
        if self.boards:
            for board in self.boards:
                board.destroy()

        self.make_player()
        self.make_boards()

    def make_player(self):
        map_left = self.map_buffer + Arkanoid.map_image_size
        map_right = self.map_buffer+ self.map_width - Arkanoid.map_image_size
        bottom = self.map_buffer + self.map_height - Arkanoid.map_image_size
        
        self.player = Player(map_left = map_left,
                             map_right = map_right,
                             bottom = bottom,
                             speed = self.player_speed)
        games.screen.add(self.player)

        self.ball = Ball(game = self,
                         speed = self.ball_speed)
        games.screen.add(self.ball)
    
    def make_map(self):
        buffer = self.map_buffer
        part_size = Arkanoid.map_image_size

        for y in range(self.map_part_y):
            for x in range(self.map_part_x):
                if y == 0 or y == self.map_part_y - 1 \
                   or x == 0 or x == self.map_part_x - 1:
                    
                    if (x == 0 and y == 0) \
                        or (x == 0 and y == self.map_part_y - 1) \
                        or (x == self.map_part_x - 1 and y == 0) \
                        or(x == self.map_part_x - 1 and y == self.map_part_y - 1):
                        continue
                        
                    if y == 0:
                        angle = 90
                    elif y == self.map_part_y - 1:
                        angle = 270
                    elif x == 0:
                        angle = 0
                    elif x == self.map_part_x - 1:
                        angle = 180
                        
                    part = games.Sprite(image = Arkanoid.map_image,
                                        angle = angle,
                                        right = buffer + (x + 1) * part_size,
                                        top = buffer + y * part_size)
                    games.screen.add(part)

    def make_boards(self):
        right = self.map_buffer + Arkanoid.map_image_size + Board.image_width
        top = self.map_buffer + Arkanoid.map_image_size
        self.boards = []

        for _ in range(self.lvl):
            while right <= self.map_buffer + self.map_width:
                board = Board(image = Board.image,
                              right = right,
                              top = top)
                self.boards.append(board)
                right += Board.image_width
                games.screen.add(board)
            right = self.map_buffer + Arkanoid.map_image_size + Board.image_width
            top += Board.image_height

    def game_over(self):
        self.lvl -= 1
        self.play()

                    

if __name__ == "__main__":
    game = Arkanoid()
    game.play()

    games.screen.mainloop()
