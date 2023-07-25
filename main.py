import pygame
from game_manager import run

from pprint import pprint


if __name__ == '__main__':
    print(pygame.font.match_font('gabriola'))
    pprint(pygame.font.get_fonts())
    run()
