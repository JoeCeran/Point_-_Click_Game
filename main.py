import pygame
import random
from characters.Player import Player

bg = pygame.image.load('assets/backgrounds/Police_station_img2.jpg')

############MUSIC###################
pygame.init()
pygame.mixer.init()

file = 'assets/music/TheStation.ogg'
pygame.mixer.music.load(file)
pygame.mixer.music.play()

voice = pygame.mixer.Sound('assets/sounds/voice.ogg')

############SPRITES########################
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

############WINDOW & BACKGROUND#############
display_width = 1600
display_height = 1200

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Officer Doodly')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_change = -5
            #     if event.key == pygame.K_RIGHT:
            #         x_change = 5
            #         voice.play()
            #
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_change = 0

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if ((pos)[0] >= 182) and ((pos)[0] <= 670) and ((pos)[1] >= 107) and ((pos)[1] <= 430):
                    voice.play()
                    print("Voice will play")

        all_sprites.update()

        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(bg, (175, 100))
        #all_sprites.draw()
        pygame.display.flip()

game_loop()
pygame.quit()
quit()