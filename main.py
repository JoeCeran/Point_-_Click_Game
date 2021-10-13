import pygame, os, random, glob
from main_code.characters.Player import Player

asset_stuff = ['backgrounds', 'music', 'sounds']
file_type = ['jpg', '.ogg', '.ogg']
main_code_stuff = ['characters', 'rooms']

option = 'search'
background_list = []
music_list = []
sound_list = []

i = 0

bg = pygame.image.load('assets/backgrounds/Police_station_img2.jpg')
############MUSIC###################
pygame.init()
pygame.mixer.init()

voice = pygame.mixer.Sound('assets/sounds/voice.ogg')
GREEN = (0, 255, 0)
HEIGHT = 100
WIDTH = 100

############SPRITES########################
all_sprites = pygame.sprite.Group()
player = Player(GREEN, WIDTH, HEIGHT)
all_sprites.add(player)

############WINDOW & BACKGROUND#############
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Officer Doodly')

#def action_select(event):

def load_assets():
    global i

    for assets in asset_stuff:
        print(assets)
        for files in glob.glob('assets/' + asset_stuff[i] + '/*.' + file_type[i]):
            print(files)
            print(i)
            if (assets == 'backgrounds'):
                background_list.append(files)
            elif (assets == 'music'):
                music_list.append(files)
                pygame.mixer.music.load(music_list)
                pygame.mixer.music.play()
            elif (assets == 'sounds'):
                sound_list.append(files)
            i = i + 1

def game_loop():
    gameExit = False
    option = 'search'

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    option = 'search'
                if event.key == pygame.K_RIGHT:
                    option = 'walk'
                if event.key == pygame.K_UP:
                    option == 'talk'
                if event.key == pygame.K_DOWN:
                    option == 'grab'

            if event.type == pygame.MOUSEBUTTONUP:
                #print(option)
                if (option == 'search'):
                    pos = pygame.mouse.get_pos()
                    if ((pos)[0] >= 182) and ((pos)[0] <= 670) and ((pos)[1] >= 107) and ((pos)[1] <= 430):
                        voice.play()
                        print("Voice will play")
                elif (option == 'walk'):
                    pos = pygame.mouse.get_pos()
                    player.walk((pos)[0], (pos)[1])
                    print("Character will walk")
                elif (option == 'talk'):
                    print("Character will talk")
                elif (option == 'grab'):
                    print == ("Character will pick up")

            #action_select(event)

        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(bg, (175, 100))
        all_sprites.draw(gameDisplay)
        pygame.display.flip()

load_assets()
game_loop()
pygame.quit()
quit()

