import pygame
import sys

from sound_manager import screen_mp3
from web_game.screen_manager import Button, Picture, print_text


def run_game_web():
    screen_mp3.set_volume(0.2)
    screen_mp3.play(-1)
    main_screen()


# запуск игры в отдельном окне
def main_screen():
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('Затерянное сокровище')

    icon = pygame.image.load('visuals/icon.png')
    pygame.display.set_icon(icon)

    button = Button(screen, 200, 50)

    picture = pygame.image.load('visuals/screen.png')
    screen.blit(picture, (235, 0))

    pygame.display.update()

    while True:

        button.draw(640, 320, 'Начать игру')
        button.draw(640, 380, 'Галерея', choose_media, 50)
        button.draw(640, 440, 'Настройки', None, 29)
        button.draw(640, 500, 'Выход', exit_game, 55)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def choose_media():

    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('Затерянное сокровище')

    icon = pygame.image.load('visuals/icon.png')
    pygame.display.set_icon(icon)

    button = Button(screen, 200, 50)

    picture = pygame.image.load('visuals/screen.png')
    screen.blit(picture, (235, 0))

    pygame.display.update()

    while True:
        button.draw(640, 380, 'Достижения', show_achievements, 10)
        button.draw(640, 440, 'Концовки', show_endings, 40)
        button.draw(640, 500, 'Назад', main_screen, 55)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def show_achievements():
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('Затерянное сокровище')

    icon = pygame.image.load('visuals/icon.png')
    pygame.display.set_icon(icon)

    button = Button(screen, 200, 50)
    pic = Picture(screen)

    picture = pygame.image.load('visuals/achievements/screen_achievements.png')
    screen.blit(picture, (235, 0))

    pygame.display.update()

    while True:

        # рисуем медали
        medal_gold = pygame.image.load('visuals/achievements/medal_gold.png')
        screen.blit(medal_gold, (300, 230))

        medal_silver = pygame.image.load('visuals/achievements/medal_silver.png')
        screen.blit(medal_silver, (300, 400))

        medal_bronze = pygame.image.load('visuals/achievements/medal_bronze.png')
        screen.blit(medal_bronze, (300, 570))

        # рисуем подписи к достижениям
        print_text(screen, 'Не открыто', 490, 330)
        print_text(screen, 'Не открыто', 690, 330)
        print_text(screen, 'Не открыто', 890, 330)
        print_text(screen, 'Не открыто', 490, 500)
        print_text(screen, 'Не открыто', 690, 500)
        print_text(screen, 'Не открыто', 890, 500)
        print_text(screen, 'Не открыто', 490, 670)
        print_text(screen, 'Не открыто', 690, 670)
        print_text(screen, 'Не открыто', 890, 670)

        # рисуем значки достижений
        pic.draw('visuals/achievements/locked.png', 465, 190)
        pic.draw('visuals/achievements/locked.png', 665, 190)
        pic.draw('visuals/achievements/locked.png', 865, 190)
        pic.draw('visuals/achievements/locked.png', 465, 360)
        pic.draw('visuals/achievements/locked.png', 665, 360)
        pic.draw('visuals/achievements/locked.png', 865, 360)
        pic.draw('visuals/achievements/locked.png', 465, 530)
        pic.draw('visuals/achievements/locked.png', 665, 530)
        pic.draw('visuals/achievements/locked.png', 865, 530)

        # кнопка выхода из меню
        while True:
            button.draw(640, 725, 'Назад', choose_media, 55)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


def show_endings():
    screen = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption('Затерянное сокровище')

    icon = pygame.image.load('visuals/icon.png')
    pygame.display.set_icon(icon)

    button = Button(screen, 200, 50)
    pic = Picture(screen)

    picture = pygame.image.load('visuals/endings/screen_endings.png')
    screen.blit(picture, (235, 0))

    pygame.display.update()

    while True:

        # рисуем подписи к концовкам
        print_text(screen, 'Торжество прогресса', 420, 330, font_size=35)
        print_text(screen, 'Обыкновенное чудо', 434, 500, font_size=35)
        print_text(screen, 'Вечно молодой', 459, 670, font_size=35)
        print_text(screen, 'Герой заслужил свой отдых', 790, 330, font_size=35)
        print_text(screen, 'Нет, лучше посох и сума', 812, 500, font_size=35)
        print_text(screen, 'Безумству храбрых', 834, 670, font_size=35)

        # рисуем значки концовок
        pic.draw('visuals/achievements/locked.png', 463, 190)
        pic.draw('visuals/achievements/locked.png', 463, 360)
        pic.draw('visuals/achievements/locked.png', 463, 530)
        pic.draw('visuals/achievements/locked.png', 863, 190)
        pic.draw('visuals/achievements/locked.png', 863, 360)
        pic.draw('visuals/achievements/locked.png', 863, 530)

        pygame.display.update()

        # кнопка выхода из меню
        while True:
            button.draw(640, 725, 'Назад', choose_media, 55)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


def exit_game():
    exit()
