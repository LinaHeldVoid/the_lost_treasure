import pygame

from wed_game import run_game_web
from console_game import run_game_console
from console_game import wrong_input


# функция, управляющая запуском игры
def run():
    print('Приветствуем, путник!')
    print('Данная игра имеет несколько реализаций. Сейчас вам предстоит выбрать наиболее удобную.')
    while True:
        print('В каком формате вы хотите играть?' + '\n'
              '1) Открыть игру в консоли' + '\n'
              '2) Открыть игру в отдельном окне' + '\n')
        game_choice = input('Введите любую цифру из предложенных: ')
        if game_choice != '1' and game_choice != '2':
            wrong_input()
            continue
        else:
            break
    print('\n' + 'Отлично!' + '\n')
    while True:
        print('Данная игра имеет опцию озвучивания текста. Желаете ли вы включить её?' + '\n'
              '1) Да' + '\n'
              '2) Нет' + '\n')
        sound_choice = input('Введите любую цифру из предложенных: ')
        if sound_choice == '1':
            print('Извините, данная опция пока не доступна( Выберите второй вариант ответа.' + '\n')
            continue
        elif sound_choice == '2':

            # параметр, определяющий включение-выключение озвучки текста
            voice_settings = False

            if game_choice == '1':
                run_game_console(voice_settings)
            else:
                run_game_web(voice_settings)
        else:
            wrong_input()
            continue
