
import pygame


if __name__ == "__main__":
    print("\nThis is a module. It should be imported.")
    input("Press enter to continue...")


class Bullet():
    """Представление пули, летящей вверх"""

    def __init__(self, settings, screen, centery, left):
        self.settings = settings
        self.screen = screen
        
        self.rect = pygame.Rect(left, centery,
                                self.settings["width"],
                                self.settings["height"])

    def show(self):
        """Выводит пулю на экран"""
        pygame.draw.rect(self.screen, self.settings["colour"], self.rect)

    def update(self):
        """Выводит пулю на экран чуть выше"""
        self.show()
        self.rect.right += self.settings["speed"]
        
