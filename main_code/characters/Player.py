import pygame
from main_code.Object import Object


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, sprite):
        super().__init__()
        self._x = x
        self._y = y
        self.image = sprite
        print("Player: " + str(self.image))
        self.rect = self.image.get_rect(center=(self._x, self._y))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def walk(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self._x = x
        self._y = y

    #def talk(self):
    #def pick_up
    def search(self, Object, sound):
        print("Dooly: " + str(self._x) + " & " + str(self.y))
        print("Object: " + str(Object.x) + " & " + str(Object.y))
        try:
            if (self._x >= (Object.x + 50) or (self._x >= (Object.x - 50))) and ((self._y <= (Object.y + 50)) or (self._y >= (Object.y - 50))):
                print("You got the " + str(Object.name) + "!")
                pygame.mixer.Sound.play(sound)
                return True
            else:
                print("You need to get closer...")
        except IndexError:
            print("There's nothing there!")


