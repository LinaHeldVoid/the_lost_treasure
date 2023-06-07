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

    # параметр, определяющий скорость печати текста
    text_settings = True
    while True:
        print('В данной игре текст появляется постепенно - это имитирует взаимодействие с реальной книгой. ' + '\n'
              'Желаете ли вы включить эту опцию?' + '\n'
              '1) Да, включить "медленную" печать"' + '\n'
              '2) Нет, включить мгновенную печать' + '\n')
        option = input('Введите любую цифру из предложенных: ')
        if option == '1':
            break
        elif option == '2':
            text_settings = False
            break
        else:
            print(wrong_input())
            continue
    print('\n' + 'Принято!' + '\n')

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
                run_game_console(text_settings)
                return
            else:
                run_game_web(voice_settings)
                return
        else:
            wrong_input()
            continue
