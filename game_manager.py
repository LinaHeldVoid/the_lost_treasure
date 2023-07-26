from web_game.wed_game import run_game_web
from console_game.console_game import run_game_console
from pprint import pprint

def wrong_input():
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


def settings_input():
    settings = {}

    """Подбираем режим запуска игры"""
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

    # записываем параметры запуска в файл
    console = False
    if game_choice == '1':
        console = True
    settings['console'] = console
    settings['text_settings'] = text_settings
    settings['voice_action_settings'] = voice_action_settings
    settings['voice_person_settings'] = voice_person_settings
    settings['music_settings'] = music_settings
    settings['sound_settings'] = sound_settings

    with open('game_logs/settings_log.txt', 'w', encoding='utf-8') as file:
        for key, value in settings.items():
            file.write(f'{key}: {value}\n')

    return settings


# функция, управляющая запуском игры
def check_settings():

    settings = {}

    """Проверяем, запускали ли ранее игру на этом устройстве"""
    try:
        with open('game_logs/settings_log.txt', 'r', encoding='utf-8') as file:
            for line in file:
                key, value = line.split(': ')
                settings.update({key: value})

        # достаём данные из словаря
        console_mode = settings['console']
        text_settings = settings['text_settings']
        voice_action_settings = settings['voice_action_settings']
        voice_person_settings = settings['voice_person_settings']
        music_settings = settings['music_settings']
        sound_settings = settings['sound_settings']

        # готовим данные к печати
        if console_mode == 'True\n':
            mode = 'консоль'
        else:
            mode = 'отдельное окно'
        if text_settings == 1:
            text = 'включена'
        else:
            text = 'выключена'
        if voice_action_settings == 'True\n':
            voice_action = 'включено'
        else:
            voice_action = 'выключено'
        if voice_person_settings == 'True\n':
            voice_person = 'включено'
        else:
            voice_person = 'выключено'
        if music_settings == 'True\n':
            music = 'включена'
        else:
            music = 'выключена'
        if sound_settings == 'True\n':
            sound = 'включены'
        else:
            sound = 'выключены'
        pprint(settings)

        while True:
            print('Приветствуем снова, путник!')
            print('В прошлый раз вами были выбраны следующие параметры игры:' + '\n'
                  '\n'
                  f'    Режим запуска: {mode}' + '\n'
                  f'    Замедленная печать текста (имитация чтения книги): {text}' + '\n'
                  f'    Озвучивание реплик персонажа и слов от автора: {voice_person}' + '\n'
                  f'    Озвучивание технического текста: {voice_action}' + '\n'
                  f'    Музыка: {music}' + '\n'
                  f'    Звуковые эффекты: {sound}' + '\n'
                  '\n'
                  'Желаете применить данные параметры снова?' + '\n'
                  '1) Да, оставьте всё так' + '\n'
                  '2) Нет, я хочу кое-что поменять' + '\n')
            option = input('Введите любую цифру из предложенных: ')
            if option == '1':
                return settings
            elif option == '2':
                settings = settings_input()
                return settings

    except FileNotFoundError:
        print('Приветствуем, путник!')
        settings = settings_input()
        return settings


def run():
    # запуск игры

    # достаём данные из словаря
    settings = check_settings()
    console_mode = settings['console']
    text_settings = settings['text_settings']
    voice_action_settings = settings['voice_action_settings']
    voice_person_settings = settings['voice_person_settings']
    music_settings = settings['music_settings']
    sound_settings = settings['sound_settings']

    while True:
        if console_mode == 'True\n':
            run_game_console(text_settings, voice_action_settings,
                             voice_person_settings, music_settings, sound_settings)
            return
        else:
            run_game_web()
