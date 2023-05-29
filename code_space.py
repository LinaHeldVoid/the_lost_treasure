import pygame
import sys
from picture_manager import Room
from sound_manager import define_sound


def run():

    pygame.init()
    screen = screen = pygame.display.set_mode((1150, 640))
    pygame.display.set_caption('Затерянное сокровище')
    bg_color = (0, 0, 0)
    picture = Room(screen, pygame.image.load('locations/door/1_start.png'))
    pic = 'locations/door/2_trapped.png'
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


class Button():
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()

        if x < mouse[0] < x + self.width:
            if x < mouse[1] < x + self.height:
                pygame.draw.rect(display)


screen = pygame.display.set_mode((1150, 640))
run()
