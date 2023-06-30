import pygame
import sys
from picture_manager import Room
from sound_manager import define_sound

# def print_text(message, x, y, font_color=(0, 0, 0))


# запуск игры в отдельном окне
def run_game_web():
    screen = pygame.display.set_mode((1150, 640))
    pygame.display.set_caption('Затерянное сокровище')
    bg_color = (0, 0, 0)

    icon = pygame.image.load('../icon.png')
    pygame.display.set_icon(icon)

    picture = Room(screen, pygame.image.load('../locations/door/1_start.png'))
    pic = 'locations/door/1_start.png'
    bg_sound = define_sound(pic)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event == 'Начать игру!':
                pass
            elif event == 'Выйти':
                sys.exit()
        screen.fill(bg_color)
        bg_sound.play()
        picture.output()
        pygame.display.flip()
