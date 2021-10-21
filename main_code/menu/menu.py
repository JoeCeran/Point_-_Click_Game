import pygame


class menu(pygame.sprite.Sprite):

    def __init__(self, name, id, width, height, x, y, sprite):
        super().__init__()
        self._name = name
        self._x = x
        self._y = y
        self.image = sprite
        self.rect = self.image.get_rect(center=(x,y))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

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

    #def remove(self):
