import pygame
import sys
from picture_manager import Room
from sound_manager import define_sound


screen = pygame.display.set_mode((1150, 640))
pygame.display.set_caption('Затерянное сокровище')
bg_color = (0, 0, 0)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# def print_text(message, x, y, font_color=(0, 0, 0))


class Button():
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if x < mouse[1] < x + self.height:
                pygame.draw.rect(screen, (23, 204, 48), (x, y, self.width, self.height))

                if click[0] == 1:
                    # pygame.mixer.Sound.play(button_pressed)
                    pygame.time.delay(300)
                    if action is not None:
                        action()

        else:
            pygame.draw.rect(screen, (13, 162, 58), (x, y, self.width, self.height))

        # print_text(message, )


def run():

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


run()
