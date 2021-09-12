# Bouncing Pizza
# Demonstrates dealing with screen boundaries

from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 2000) 

class Pizza(games.Sprite):
    """ A bouncing pizza. """
    def update(self):
        """ Reverse a velocity component if edge of screen reached. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

class Fp(games.Text):
    def update(self):
        self.value = games.screen.fps

def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    pizza_image = games.load_image("pizza.bmp")
    the_pizza_1 = Pizza(image = pizza_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    the_pizza_2 = Pizza(image = pizza_image,
                      x = games.screen.width/4,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    the_pizza_3 = Pizza(image = pizza_image,
                      x = games.screen.width - games.screen.width / 4,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)

    for pizza in (the_pizza_1, the_pizza_2, the_pizza_3):
        games.screen.add(pizza)

    text = Fp(value = games.screen.fps,
                      size = 40,
                      color = color.red,
                      x = 50,
                      y = 50)
    games.screen.add(text)

    games.screen.mainloop()

# kick it off!
main()
