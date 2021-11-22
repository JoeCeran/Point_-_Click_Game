import pygame, glob
from main_code.characters.Player import Player
from main_code.Object import Object


asset_dict = {
    1: {'type': "backgrounds", 'location': []},
    2: {'type': "music", 'location': []},
    3: {'type': "sounds", 'location': []},
    4: {'type': "sprites", 'location': []}}

game_dict = {
    1: {'type': "character"},
    2: {'type:': "object"}
}

level_dict = {
    0: {'name': "station",
        'background': [0],
        'music': [0],
        'sound': [0],
        'character': [0, 1],
        'object': [0, 1]},
}

main_code_stuff = ['characters', 'rooms']
option = 'search'
character_map = []
object_map = []
all_sprites = pygame.sprite.Group()
bg = ""
sound = ""
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
    for i in range(1, (len(asset_dict) + 1)):
        for keys, values in asset_dict[i].items():
            for files in glob.glob('assets/' + str(values) + '/*'):
                asset_dict[i]['location'].append(files)

def load_assets(room_id):

    global bg
    global sound
    global all_sprites
    global player

    for keys, values in level_dict[0].items():
        print(keys)
        for value in level_dict[0][keys]:
            load_number = value
            match keys:
                case 'name':
                    print("Room " + str(load_number) + " Has been loaded in!")
                case 'background':
                    bg = pygame.image.load(asset_dict[1]['location'][load_number])
                case 'music':
                    print('music')
                case 'sound':
                    sound = pygame.mixer.Sound(asset_dict[3]['location'][load_number])
                    print('sound' + str(sound))
                case 'character':
                    print('character')
                case 'object':
                    print('object')

    print(load_number)
    pygame.mixer.music.load(asset_dict[2]['location'][load_number])

    image = pygame.image.load(asset_dict[4]['location'][0]).convert_alpha()
    image2 = pygame.image.load(asset_dict[4]['location'][1]).convert_alpha()
    image3 = pygame.image.load(asset_dict[4]['location'][2]).convert_alpha()
    player = Player(100, 400, image)
    desk = Object("desk", 1, 10, 10, 700, 450, image2)
    pot = Object("pot", 1, 10, 10, 700, 340, image3)
    all_sprites.add(player)
    all_sprites.add(desk)
    all_sprites.add(pot)
    character_map.append(player)
    object_map.append(desk)

    return bg, sound, player, desk

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
    global sound
    global player
    global all_sprites

    load_assets(0)

    pygame.mixer.music.play()

    while not gameExit:

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    quit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT: option = 'search'
                        case pygame.K_RIGHT: option = 'walk'
                        case pygame.K_UP: option = 'talk'
                        case pygame.K_DOWN: option = 'grab'

                case pygame.MOUSEBUTTONUP:
                    match option:
                        case 'search':
                            try:
                                if character_map[0].search(object_map[0], sound):
                                    all_sprites.remove(object_map[0])
                                    object_map.remove(object_map[0])
                            except IndexError:
                                print("There's nothing there!")
                        case 'walk':
                            pos = pygame.mouse.get_pos()
                            player.walk(pos[0], pos[1])
                        case 'talk':
                            print("Character will talk")
                        case 'grab':
                            print("Character will pick up")

            draw_screen(bg)

def main():
    import_assets()
    game_loop()
    pygame.quit()
    quit()


if __name__=="__main__":
    main()

