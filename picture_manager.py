import pygame


class Room():

    def __init__(self, screen, pic):
        """добавляем картинку"""
        self.screen = screen
        self.image = pic
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """рисуем картинку"""
        self.screen.blit(self.image, self.rect)

