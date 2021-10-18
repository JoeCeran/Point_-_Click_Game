import pygame, glob
from main_code.characters.Player import Player
from main_code.Object import Object

asset_stuff = ['backgrounds', 'music', 'sounds', 'sprites']
file_type = ['jpg', '.ogg', '.ogg', 'png']
main_code_stuff = ['characters', 'rooms']

option = 'search'
background_list = []
sprite_list = []
music_list = []
sound_list = []
assets_map = []
character_map = []
object_map = []
all_sprites = pygame.sprite.Group()
bg = ""
voice = ""
player = Player
desk = Object
change_location = False

############MUSIC###################

pygame.init()
pygame.mixer.init()

############WINDOW & BACKGROUND#############
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Officer Doodly!')

def import_assets():
    i = 0
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
            elif (assets == 'sprites'):
                print("sprites: " + files)
                sprite_list.append(files)

        i = i + 1

def load_assets(room_id):

    global bg
    global voice
    global all_sprites
    global player

    with open('main_code/game_data.txt') as f:
        lines = f.readlines()
        loaded_background = int(lines[room_id].replace('\n', ''))
        loaded_sprite = int(lines[room_id].replace('\n', ''))
        loaded_music = int(lines[room_id].replace('\n', ''))
        loaded_sound = int(lines[room_id].replace('\n', ''))

        bg = pygame.image.load(background_list[loaded_background])

        pygame.mixer.music.load(music_list[loaded_music])
        pygame.mixer.music.play()

        voice = pygame.mixer.Sound(sound_list[loaded_sound])

        image = pygame.image.load(sprite_list[loaded_sprite]).convert_alpha()
        image2 = pygame.image.load(sprite_list[1]).convert_alpha()
        image3 = pygame.image.load(sprite_list[2]).convert_alpha()
        player = Player(100, 400, image)
        desk = Object("desk", 1, 10, 10, 700, 450, image2)
        pot = Object("desk", 1, 10, 10, 700, 340, image3)
        all_sprites.add(player)
        all_sprites.add(desk)
        all_sprites.add(pot)
        character_map.append(player)
        object_map.append(desk)

    return bg, voice, player, desk

def play_sound(sound):
    pygame.mixer.Sound.play(sound)

def draw_screen(bg):

    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(bg, (0, 0))
    all_sprites.draw(gameDisplay)
    pygame.display.flip()


def is_location_changed(change_location):

    if change_location:
        load_assets(1)
        change_location = False

    return change_location

def game_loop():
    gameExit = False
    global change_location
    option = 'search'
    global background
    global voice
    global player
    global all_sprites


    load_assets(0)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    option = 'search'
                elif event.key == pygame.K_RIGHT:
                    option = 'walk'
                elif event.key == pygame.K_UP:
                    option = 'talk'
                elif event.key == pygame.K_DOWN:
                    option = 'grab'

            if event.type == pygame.MOUSEBUTTONUP:
                if (option == 'search'):
                    try:
                        if character_map[0].search(object_map[0], voice):
                            all_sprites.remove(object_map[0])
                            object_map.remove(object_map[0])
                    except IndexError:
                        print("There's nothing there!")
                elif (option == 'walk'):
                    pos = pygame.mouse.get_pos()
                    player.walk(pos[0], pos[1])
                elif (option == 'talk'):
                    print("Character will talk")
                elif (option == 'grab'):
                    print("Character will pick up")

            draw_screen(bg)

def main():
    import_assets()
    game_loop()
    pygame.quit()
    quit()


if __name__=="__main__":
    main()

