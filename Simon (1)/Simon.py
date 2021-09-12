# По условию задачи №2 главы 12

from livewires import games
import random, winsound

games.init(screen_width = 800, screen_height = 600, fps = 75)
fps = games.screen.fps

class Simon(games.Sprite):
    """Simon"""
    LIGHT_TIME = 1
    TIME_BETWEEN_LIGHT = 0.5
    NEW_ROUND_TIME = 3
    
    colours = [[games.load_image("arrow_left.png"), 100],
                [games.load_image("arrow_up.png"), 200],
                [games.load_image("arrow_right.png"), 300],
                [games.load_image("arrow_down.png"), 400]]
    light_image = games.load_image("arrow_light.png")

    neutral_image = games.load_image("center_neutral.png")
    right_image = games.load_image("center_right.png")
    wrong_image = games.load_image("center_wrong.png")
    
    def __init__(self):
        self.lvl = 2
        self.wait_time = 0
        self.light_sprite = None
        self.is_new_round = False
        center = [games.screen.width / 2,
                  games.screen.height / 2]
        
        super().__init__(image = Simon.neutral_image,
                         x = center[0],
                         y = center[1])

        self.colours = []
        self.sequence = []
        self.light_sequence = []
        self.player_sequence = []
        
        buffer = int( 0.75 * get_image_width(Simon.colours[0][0]) ) + 5
        coors = [[ center[0] - buffer, center[1] ],
                 [ center[0], center[1] - buffer ],
                 [ center[0] + buffer, center[1] ],
                 [ center[0], center[1] + buffer ]]
        for i in range(4):
            colour = games.Sprite(image = Simon.colours[i][0],
                                  x = coors[i][0],
                                  y = coors[i][1])
            self.colours.append(colour)
            
        for colour in self.colours:
            games.screen.add(colour)
        games.screen.add(self)

    def update(self):
        if self.wait_time > 0:
            if self.wait_time < Simon.TIME_BETWEEN_LIGHT * fps:
                self.light_sprite.destroy()
            self.wait_time -= 1
        elif self.is_new_round:
            self.is_new_round = False
            self.play()
        elif self.light_sequence:
            self.light(self.light_sequence.pop(0))
        else:
            ways = (games.K_LEFT, games.K_UP, games.K_RIGHT, games.K_DOWN)
            for way in ways:
                if games.keyboard.is_pressed(way):
                    self.player_sequence.append(ways.index(way))
                    self.light(ways.index(way), Simon.LIGHT_TIME)
                    
                    for i in range(len(self.player_sequence)):
                        if self.player_sequence[i] != self.sequence[i]:
                            new_image(self, Simon.wrong_image)     
                            self.set_wait_time(Simon.NEW_ROUND_TIME)
                            self.is_new_round = True
                            
                    if not self.is_new_round:
                        if len(self.player_sequence) == len(self.sequence):
                            new_image(self, Simon.right_image)
                            self.is_new_round = True
                            self.set_wait_time(Simon.NEW_ROUND_TIME)
                            self.lvl += 1
                
    def play(self):
        new_image(self, Simon.neutral_image)
        self.player_sequence = []

        while len(self.sequence) < self.lvl:
            choice = random.randrange(4)
            self.sequence.append(choice)
        self.light_sequence = self.sequence[:]

    def light(self, id_colour, time = LIGHT_TIME):
        self.light_sprite = games.Sprite(image = Simon.light_image,
                             left = self.colours[id_colour].left - 5,
                             top = self.colours[id_colour].top - 5,
                             angle = id_colour * 90)
        games.screen.add(self.light_sprite)

        winsound.Beep(Simon.colours[id_colour][1], Simon.LIGHT_TIME * fps)
        
        self.colours[id_colour].destroy()
        games.screen.add(self.colours[id_colour])
        
        self.set_wait_time(time + Simon.TIME_BETWEEN_LIGHT)

    def set_wait_time(self, time):
        self.wait_time = time * fps


def new_image(sprite, image):
    sprite.destroy()
    sprite.image = image
    games.screen.add(sprite)

def get_image_width(image):
    sprite = games.Sprite(image = image)
    return sprite.width


if __name__ == "__main__":
    game = Simon()
    game.play()
    
    games.screen.mainloop()
