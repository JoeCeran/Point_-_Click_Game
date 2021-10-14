import pygame, os, random, glob
from main_code.characters.Player import Player

asset_stuff = ['backgrounds', 'music', 'sounds']
file_type = ['jpg', '.ogg', '.ogg']
main_code_stuff = ['characters', 'rooms']

option = 'search'
background_list = []
music_list = []
sound_list = []

############MUSIC###################
pygame.init()
pygame.mixer.init()

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
    i = 0
    j = 0
    for assets in asset_stuff:
        for files in glob.glob('assets/' + asset_stuff[i] + '/*'):
            if (assets == 'backgrounds'):
                print("background: " + files)
                background_list.append(files)
            elif (assets == 'music'):
                print("music: " + files)
                music_list.append(files)
            elif (assets == 'sounds'):
                print("sounds: " + files)
                sound_list.append(files)
            i = i + 1

def game_loop():
    gameExit = False
    option = 'search'

    with open('main_code/game_data.txt') as f:
        lines = f.readlines()
        print(lines)
        loaded_background = int(lines[0].replace('\n', ''))
        loaded_music = int(lines[1].replace('\n', ''))
        loaded_sound = int(lines[2].replace('\n', ''))

        bg = pygame.image.load(background_list[loaded_background])
        pygame.mixer.music.load(music_list[loaded_music])
        pygame.mixer.music.play()
        voice = pygame.mixer.Sound(sound_list[loaded_sound])

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            j = 0

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

