import pygame

# button_pressed = pygame.mixer.Sound('sound/button.wav')


def define_sound(picture):

    """определяем, какая музыка нужна для локации"""

    if picture == 'locations/door/2_trapped.png':
        sound = 'danger_death.wav'
    elif picture.startswith('locations/room_2/'):
        sound = 'room_2.wav'
    else:
        sound = 'room_1.wav'

    sound_path = 'sound/locations/' + sound
    bg_sound = pygame.mixer.Sound(sound_path)
    return bg_sound


pygame.mixer.init()
room_1_mp3_path = 'sound/locations/room_1.wav'
room_1_mp3 = pygame.mixer.Sound(room_1_mp3_path)
dd_mp3_path = 'sound/locations/danger_death.wav'
dd_mp3 = pygame.mixer.Sound(dd_mp3_path)
room_2_mp3_path = 'sound/locations/room_2.wav'
room_2_mp3 = pygame.mixer.Sound(room_2_mp3_path)
