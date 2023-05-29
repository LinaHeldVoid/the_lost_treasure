import pygame


def define_sound(picture):

    """определяем, какая музыка нужна для локации"""

    if picture == 'locations/door/2_trapped.png':
        sound = 'danger_death.mp3'
    elif picture.startswith('locations/room_2/'):
        sound = 'room_2.mp3'
    else:
        sound = 'room_1.mp3'

    sound_path = 'sound/locations/' + sound
    bg_sound = pygame.mixer.Sound(sound_path)
    return bg_sound
