import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, GREEN, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        #self.name = name
        #self.id = id
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def walk(self, x, y):
        self.rect.x = x
        self.rect.y = y

    #def talk(self):
    #def pick_up
    #def search