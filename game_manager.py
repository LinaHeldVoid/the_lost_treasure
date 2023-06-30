from web_game.wed_game import run_game_web
from console_game.console_game import run_game_console


def wrong_input():
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


# функция, управляющая запуском игры
def run():

    """Подбираем режим запуска игры"""
    print('Приветствуем, путник!')
    print('Данная игра имеет несколько реализаций. Сейчас вам предстоит выбрать наиболее удобную.')
    print('Для этого вам нужно ответить на несколько несложных вопросов, после чего игра будет запущена.')
    while True:
        print('В каком формате вы хотите играть?' + '\n'
              '1) В консоли' + '\n'
              '2) В отдельном окне' + '\n')
        game_choice = input('Введите любую цифру из предложенных: ')
        if game_choice != '1' and game_choice != '2':
            wrong_input()
            continue
        else:
            break
    print('\n' + 'Отлично!' + '\n')

    """выбираем параметры запуска"""
    # скорость печати текста
    text_settings = True
    # озвучка технического текста
    voice_action_settings = True
    # озвучка реплик и слов от автора
    voice_person_settings = True
    # музыка
    music_settings = True
    # звуки
    sound_settings = True

    # текст
    while True:
        print('В игре текст может печататься постепенно - это имитирует взаимодействие с реальной книгой. ' + '\n'
              'Желаете ли вы включить эту опцию?' + '\n'
              '1) Да, включить "медленную" печать"' + '\n'
              '2) Нет, включить мгновенную печать' + '\n')
        text_option = input('Введите любую цифру из предложенных: ')
        if text_option == '1':
            break
        elif text_option == '2':
            text_settings = False
            break
        else:
            print(wrong_input())
            continue
    print('\n' + 'Принято!' + '\n')

    # озвучка
    while True:
        print('Игра имеет опцию озвучивания текста. Какой вариант больше подходит вам?' + '\n'
              '1) Озвучивать весь текст' + '\n'
              '2) Озвучивать только реплики и слова от автора' + '\n'         
              '3) Не озвучивать ничего' + '\n'
              '4) Озвучивать только действия' + '\n')
        record_choice = input('Введите любую цифру из предложенных: ')
        if record_choice == '1':
            break
        elif record_choice == '2':
            voice_action_settings = False
            break
        elif record_choice == '3':
            voice_action_settings = False
            voice_person_settings = False
            break
        elif record_choice == '4':
            voice_action_settings = True
            voice_person_settings = False
            break
        else:
            wrong_input()
            continue

    # музыка и звуковые эффекты
    while True:
        print('Игра имеет звуковые эффекты и музыку. Хотите их включить?' + '\n'
              '1) Включайте всё!' + '\n'
              '2) Оставьте только музыку' + '\n'
              '3) Оставьте только звуковые эффекты' + '\n'
              '4) Отключить звук' + '\n')
        sound_choice = input('Введите любую цифру из предложенных: ')
        if sound_choice == '1':
            break
        elif sound_choice == '2':
            sound_settings = False
            break
        elif sound_choice == '3':
            music_settings = False
            break
        elif sound_choice == '4':
            sound_settings = False
            music_settings = False
            break
        else:
            wrong_input()
            continue

    # запуск игры
    while True:
        if game_choice == '1':
            run_game_console(text_settings, voice_action_settings,
                             voice_person_settings, music_settings, sound_settings)
            return
        elif game_choice == '2':
            run_game_web()
            return
        else:
            print(wrong_input())
            continue
