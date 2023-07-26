import pygame

from sound_manager import button_wav


pygame.font.init()


# вывод текста на экран
def print_text(screen, message, x, y, font_size=25, font_colour=(250, 250, 250),
               font_type='C:/Windows/Fonts/Gabriola.ttf'):

    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    screen.blit(text, (x, y))


# системная кнопка
def print_text_button(screen, message, x, y, font_size, font_colour=(0, 0, 0), font_type='C:/Windows/Fonts/Gabriola.ttf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    screen.blit(text, (x, y))
    return


class Button():
    """создание класса кнопки (в процессе)"""

    def __init__(self, screen, width, height):
        self.display = screen
        self.width = width
        self.height = height
        self.inactive_color = (164, 248, 250)
        self.active_color = (42, 239, 243)

    def draw(self, x, y, message, action=None, x_text=None, y_text=None, font_size=40):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if not x_text:
            x_text = 20
        if not y_text:
            y_text = 10

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:

                pygame.display.update()
                pygame.draw.rect(self.display, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_wav.play()
                    pygame.time.wait(300)
                    if action is not None:
                        action()
        else:
            pygame.display.update()
            pygame.draw.rect(self.display, self.inactive_color, (x, y, self.width, self.height))

        print_text_button(self.display, message=message, x=x+x_text, y=y+y_text, font_size=font_size)


class Picture():
    def __init__(self, screen, clickable=False):
        self.display = screen
        self.clickable = clickable

    def draw(self, path, x, y):
        if self.clickable:
            pass
        else:
            pic = pygame.image.load(path)
            self.display.blit(pic, (x, y))
