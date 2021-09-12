# Классическая змейка

from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 600, fps = 75 * 2)

class Collider(games.Sprite):
    """Часть тела"""
    def collide(self, snake):
        self.Collider_collide(snake)
        
    def Collider_collide(self, snake):
        snake.die()
        
class Map():
    """Границы экрана"""
    image = games.load_image("wall.png")
    
    def __init__(self, buffer = 50, x = 60, y = 50):
        self.buffer = buffer
        self.image_size = check_image(Map.image)
        self.x = x
        self.y = y
        self.x_size = x * self.image_size
        self.y_size = y * self.image_size
        
        for ky in range(y):
            for kx in range(x):
                if (ky == 0 or ky == y - 1 \
                   or kx == 0 or kx == x - 1):

                    if (kx == 0 and ky == 0 \
                        or kx == x - 1 and ky == 0 \
                        or kx == 0 and ky == y - 1 \
                        or kx == x - 1 and ky == y - 1):
                        continue
                    
                    if kx == 0:
                        angle = 0
                    elif kx == x - 1:
                        angle = 180
                    elif ky == 0:
                        angle = 90
                    elif ky == y - 1:
                        angle = 270
                        
                    wall = Collider(image = Map.image,
                                    angle = angle,
                                    left = self.buffer + kx * self.image_size,
                                    top = self.buffer + ky * self.image_size)
                    games.screen.add(wall)
                    

class Apple(Collider):
    """Яблоко"""
    image = games.load_image("apple.png", transparent = False)
    
    def __init__(self, _map):
        super().__init__(image = Apple.image)
        self.image_size = check_image(Apple.image)
        self._map = _map

        self.new_coor()

        games.screen.add(self)

    def new_coor(self):
        buffer = self._map.buffer + self._map.image_size
        x = random.randint(buffer + self._map.image_size,
                           buffer + self._map.x_size - self._map.image_size)
        self.right = x - x % 10
        y = random.randint(buffer + self._map.image_size,
                           buffer + self._map.y_size - self._map.image_size)
        self.top = y - y % 10

        if self.overlapping_sprites:
            self.new_coor()

    def collide(self, snake):
        self.Apple_collide(snake)

    def Apple_collide(self, snake):
        snake.lvl_up()
        self.new_coor()
        
        
class Snake(games.Sprite):
    """Змейка"""
    image = games.load_image("snake_body.png", transparent = False)
    START_SIZE = 8
    GAME_OVER_TIME = 5
    START_WAY = "right"

    def __init__(self,
                 game,
                 speed = 1):
        super().__init__(image = Snake.image)
        self.way = Snake.START_WAY
        self.way_is_free = True
        self.game = game
        x = self.game.map.x_size / 2
        y = self.game.map.y_size / 2
        self.right = self.game.map.buffer + x - x % 10
        self.top = self.game.map.buffer + y - y % 10
        
        self.speed = speed
        self.time_to_shift = self.height / self.speed
        self.new_bodyes = 0
        self.game_over = 0
        
        self.body = []
        self.body.append(self)

        for i in range(Snake.START_SIZE - 1):
            body_part = Collider(image = Snake.image,
                                     right = self.body[i].left,
                                     top = self.body[i].top)
            self.body.append(body_part)

        self.coor_buffer = [self.body[-1].right, self.body[-1].top]

        for body_part in self.body:
            games.screen.add(body_part)

    def update(self):
        if self.game_over:
            if self.game_over == 1:
                for body_part in self.body:
                    body_part.destroy()
                    self.destroy()
                self.game.new_game()
            self.game_over -= 1
        else:
            self.shift()

            for sprite in self.overlapping_sprites:
                sprite.collide(self)

    def shift(self):
        if self.way_is_free:
            if games.keyboard.is_pressed(games.K_UP):
                if self.way != "down":
                    self.way = "up"
                    self.way_is_free = False
            elif games.keyboard.is_pressed(games.K_DOWN):
                if self.way != "up":
                    self.way = "down"
                    self.way_is_free = False
            elif games.keyboard.is_pressed(games.K_LEFT):
                if self.way != "right":
                    self.way = "left"
                    self.way_is_free = False
            elif games.keyboard.is_pressed(games.K_RIGHT):
                if self.way != "left":
                    self.way = "right"
                    self.way_is_free = False

        if self.time_to_shift <= 0:
            self.way_is_free = True
            
            i = len(self.body) - 1
            while i > 0:
                self.body_buffer = [self.body[-1].right, self.body[-1].top]
                
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
                i -= 1
            
            if self.way == "up":
                self.y -= self.height
            elif self.way == "down":
                self.y += self.height
            elif self.way == "left":
                self.x -= self.height
            elif self.way == "right":
                self.x += self.height
            self.time_to_shift = self.height / self.speed

            while self.new_bodyes:
                games.screen.add(self.body[-self.new_bodyes])
                self.new_bodyes -= 1
                
        self.time_to_shift -= 1
        self.coor_buffer = [self.body[-1].right, self.body[-1].top]

    def lvl_up(self):
        new_body_part = Collider(image = Snake.image)

        print(self.coor_buffer)
        right, top = self.coor_buffer
        new_body_part.right = right
        new_body_part.top = top
        
        self.body.append(new_body_part)
        games.screen.add(self.body[len(self.body) - 1])

    def die(self):
        self.game_over = Snake.GAME_OVER_TIME * games.screen.fps


class Game(games.Text):
    MAP_BUFFER = 50
    MAP_X = 50
    MAP_Y = 50
    INFO_SIZE = 20
    
    def __init__(self):
        self.map = Map(buffer = Game.MAP_BUFFER,
                       x = Game.MAP_X,
                       y = Game.MAP_Y)
        self.apple = Apple(self.map)
        self.snake = Snake(self)

        self.info = []      
        self.textes = ("x: " + str(self.snake.right),
                       "y: " + str(self.snake.top),)
        i = 0
        for text in self.textes:
            msg = games.Text(value = text,
                        size = Game.INFO_SIZE,
                        color = color.white,
                        top = i * Game.INFO_SIZE,
                        left = 5)
            self.info.append(msg)
            i += 1

        super().__init__(value = "size: " + str(len(self.snake.body)),
                         size = Game.INFO_SIZE,
                         color = color.white,
                         left = 5,
                         top = i * Game.INFO_SIZE)
        self.info.append(self)

        for msg in self.info:
            games.screen.add(msg)

    def update(self):
        self.textes = ("x: " + str(self.snake.right),
                       "y: " + str(self.snake.top),
                       "size: " + str(len(self.snake.body)))
        i = 0
        for text in self.textes:
            self.info[i].value = text
            i += 1
    
    def new_game(self):
        self.snake = Snake(self)


def check_image(image):
        test = games.Sprite(image = Map.image)
        return test.height
        

if __name__ == "__main__":
    Game()

    games.screen.mainloop()
