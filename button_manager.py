import sys

import pygame
from code_space import screen

objects = []


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
