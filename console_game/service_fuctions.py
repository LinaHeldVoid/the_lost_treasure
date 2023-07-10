import time
import pygame
import random

from colorama import Fore, Style

from scenario_generator import generate_base
from sound_manager import dd_mp3


def set_generator_1(line):
    i = 0
    g = generate_base('text/2_room_1.txt')
    while i < line:
        next(g)
        i += 1
    return g


def set_generator_2(line):
    i = 0
    g = generate_base('text/3_room_2.txt')
    while i < line:
        next(g)
        i += 1
    return g


def set_generator_dnd(line):
    i = 0
    g = generate_base('text/8_death&determination.txt')
    while i < line:
        next(g)
        i += 1
    return g


# переводим случайные реплики в списки
def revival_generator():
    revivals = []
    i = 0
    g = set_generator_dnd(11)
    while i < 6:
        revivals.append(next(g))
        i += 1
    return revivals


def warning_generator():
    warnings = []
    i = 0
    g = set_generator_dnd(24)
    while i < 3:
        warnings.append(next(g))
        i += 1
    return warnings


def death_generator():
    deaths = []
    i = 0
    g = set_generator_dnd(30)
    while i < 3:
        deaths.append(next(g))
        i += 1
    return deaths


# неверный ввод
def wrong_input(t_settings, v_a_settings):
    sound_effect('sound/voice_actions/wrong_input.wav', v_a_settings)
    time.sleep(5) if not t_settings and v_a_settings else None
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


# проверяем корректность введённых цифр
def numbers_check(num_list):
    message = 'Ввод должен состоять из четырёх разных цифр. Попробуйте снова!'

    """проверяем длину ввода"""
    if len(num_list) != 4:
        print(message)
        time.sleep(1)
        return

    """проверяем состав ввода"""
    good_list = [1, 2, 3, 4]
    for i in num_list:
        if i.isnumeric():
            if int(i) not in good_list:
                print(message)
                time.sleep(1)
                return
        else:
            print(message)
            time.sleep(1)
            return

    """проверяем уникальность чисел"""
    if len(set(num_list)) != len(num_list):
        print(message)
        print(4)
        time.sleep(1)
        return
    else:
        return True


# имитация чтения книги
def print_effect(text, t_settings):
    if t_settings:
        for i in text:
            time.sleep(0.07)
            print(i, end='', flush=True)
    else:
        print(text, end='')


# управление запуском звука
def sound_effect(sound_path, settings):
    if settings:
        record = pygame.mixer.Sound(sound_path)
        record.play()
        return record
    else:
        return


# меню выхода из игры
def quit_menu(t_settings, v_a_settings):
    sound_effect('sound/voice_actions/option.wav', v_a_settings)
    time.sleep(1) if v_a_settings else None
    print('Вы уверены, что хотите выйти из игры?' + '\n'
          '1) Да, выйти' + '\n'
          '2) Нет, остаться' + '\n')
    record = sound_effect('sound/voice_actions/quit_menu.wav', v_a_settings)
    option = input('Введите цифру: ')
    record.stop() if v_a_settings else None
    while True:
        if option == '1':
            exit()
        elif option == '2':
            return
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue


def death_menu(t_settings, v_a_settings, m_settings):
    while True:
        g = set_generator_dnd(1)
        print(next(g))
        next(g)
        print(f'1) {next(g)}'
              f'2) {next(g)}' + '\n')
        record = sound_effect('sound/voice_actions/room_1/10_death_menu.wav', v_a_settings)
        option = input(f'Введите цифру: ')
        record.stop() if v_a_settings else None
        if option == '1':
            pygame.mixer.fadeout(2) if m_settings else None
            sound_effect('sound/voice_actions/room_1/11_game_resume.wav', v_a_settings)
            print('')
            next(g)
            next(g)
            print(Fore.YELLOW, f'{next(g)}')
            print(Style.RESET_ALL)
            time.sleep(2.5) if not t_settings and v_a_settings else None
            break
        elif option == '2':

            """конец игры"""
            exit()
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue


# случайная реакция в ответ на попытку выполнить действие дважды
def random_no(t_settings, v_p_settings, no_use):
    choose_no_use = random.choice(no_use)
    if choose_no_use == next(set_generator_2(146)):
        sound_effect('sound/voice_person/no_use.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_no_use == next(set_generator_2(147)):
        sound_effect('sound/voice_person/no_use_2.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    elif choose_no_use == next(set_generator_2(148)):
        sound_effect('sound/voice_person/no_use_3.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    elif choose_no_use == next(set_generator_2(149)):
        sound_effect('sound/voice_person/no_use_4.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/no_use_5.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    return


# случайная реакция на воскрешение
def random_revival(t_settings, v_p_settings):
    choose_revival = random.choice(revival_generator())
    if choose_revival == next(set_generator_dnd(11)):
        sound_effect('sound/voice_person/d&d/11.wav', v_p_settings)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(12)):
        sound_effect('sound/voice_person/d&d/12.wav', v_p_settings)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(13)):
        sound_effect('sound/voice_person/d&d/13.wav', v_p_settings)
        print_effect(choose_revival, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(14)):
        sound_effect('sound/voice_person/d&d/14.wav', v_p_settings)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(15)):
        sound_effect('sound/voice_person/d&d/15.wav', v_p_settings)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/d&d/16.wav', v_p_settings)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None


# случайное предупреждение о низкой решимости
def random_warning(t_settings, v_p_settings):
    choose_warning = random.choice(warning_generator())
    if choose_warning == next(set_generator_dnd(24)):
        sound_effect('sound/voice_person/d&d/24.wav', v_p_settings)
        print_effect(choose_warning, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_warning == next(set_generator_2(25)):
        sound_effect('sound/voice_person/d&d/25.wav', v_p_settings)
        print_effect(choose_warning, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/d&d/26.wav', v_p_settings)
        print_effect(choose_warning, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None


# случайное уведомление об окончательной смерти персонажа
def random_death(t_settings, v_p_settings):
    choose_warning = random.choice(death_generator())
    if choose_warning == next(set_generator_dnd(30)):
        sound_effect('sound/voice_person/d&d/30.wav', v_p_settings)
        print_effect(choose_warning, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    elif choose_warning == next(set_generator_2(31)):
        sound_effect('sound/voice_person/d&d/31.wav', v_p_settings)
        print_effect(choose_warning, t_settings)
        time.sleep(4.5) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/d&d/32.wav', v_p_settings)
        print_effect(choose_warning, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None


# обработка озвучки чисел
def determination_second_number(v_a_settings, some_number):
    if some_number == '1':
        sound_effect('sound/voice_actions/d&d/point_1.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '2':
        sound_effect('sound/voice_actions/d&d/point_2.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '3':
        sound_effect('sound/voice_actions/d&d/point_3.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '4':
        sound_effect('sound/voice_actions/d&d/point_4.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '5':
        sound_effect('sound/voice_actions/d&d/point_5.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '6':
        sound_effect('sound/voice_actions/d&d/point_6.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '7':
        sound_effect('sound/voice_actions/d&d/point_7.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    elif some_number == '8':
        sound_effect('sound/voice_actions/d&d/point_8.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    else:
        sound_effect('sound/voice_actions/d&d/point_9.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
    return


def determination_first_number(v_a_settings, some_number):
    if some_number == '10':
        sound_effect('sound/voice_actions/d&d/point_10.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '11':
        sound_effect('sound/voice_actions/d&d/point_11.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '12':
        sound_effect('sound/voice_actions/d&d/point_12.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '13':
        sound_effect('sound/voice_actions/d&d/point_13.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '14':
        sound_effect('sound/voice_actions/d&d/point_14.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '15':
        sound_effect('sound/voice_actions/d&d/point_15.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '16':
        sound_effect('sound/voice_actions/d&d/point_16.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '17':
        sound_effect('sound/voice_actions/d&d/point_17.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '18':
        sound_effect('sound/voice_actions/d&d/point_18.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '19':
        sound_effect('sound/voice_actions/d&d/point_13.wav', v_a_settings)
        time.sleep(1) if v_a_settings else None
        return False
    else:
        if some_number[0] == '2':
            sound_effect('sound/voice_actions/d&d/point_20.wav', v_a_settings)
            time.sleep(1) if v_a_settings else None
            if some_number[1] == '0':
                return False
            else:
                return True
        elif some_number[0] == '3':
            sound_effect('sound/voice_actions/d&d/point_30.wav', v_a_settings)
            time.sleep(1) if v_a_settings else None
            if some_number[1] == '0':
                return False
            else:
                return True
        elif some_number[0] == '4':
            sound_effect('sound/voice_actions/d&d/point_40.wav', v_a_settings)
            time.sleep(1) if v_a_settings else None
            if some_number[1] == '0':
                return False
            else:
                return True
        else:
            sound_effect('sound/voice_actions/d&d/point_50.wav', v_a_settings)
            time.sleep(1) if v_a_settings else None
            return False


# озвучка количества очков решимости
def determination_announcement(v_a_settings, new_number):
    print(f'{next(set_generator_dnd(22))}: {new_number}')
    sound_effect('sound/voice_actions/d&d/22.wav', v_a_settings)
    time.sleep(2.5) if v_a_settings else None
    if len(str(new_number)) == 1:
        determination_second_number(v_a_settings, str(new_number))
    else:
        next_number = determination_first_number(v_a_settings, str(new_number))
        if next_number:
            determination_second_number(v_a_settings, str(new_number)[1])
    return


# функция, реагирующая на изменение количества очков решимости
def new_determination(t_settings, v_p_settings, v_a_settings, m_settings, s_settings, number, value, operation):
    if operation == '-':
        new_number = number - value

        sound_effect('sound/voice_actions/d&d/21.wav', v_a_settings)
        print(f'{next(set_generator_dnd(21))}: {value}')
        time.sleep(2) if v_a_settings else None
        if len(str(value)) == 1:
            determination_second_number(v_a_settings, str(value))
        else:
            next_num = determination_first_number(v_a_settings, str(value))
            if next_num:
                determination_second_number(v_a_settings, str(value)[1])

        # смерть персонажа из-за низкой решимости
        if new_number <= 0:
            pygame.mixer.stop() if m_settings else None
            random_death(t_settings, v_p_settings)
            sound_effect('sound/sound_effects/death.wav', s_settings)
            time.sleep(1) if s_settings else None
            dd_mp3.set_volume(0.2) if m_settings else None
            dd_mp3.play(-1) if m_settings else None
            g = set_generator_dnd(34)
            sound_effect('sound/voice_person/d&d/34.wav', v_p_settings)
            print_effect(next(g), t_settings)
            time.sleep(11) if not t_settings and v_p_settings else None
            time.sleep(1)
            sound_effect('sound/voice_person/d&d/35.wav', v_p_settings)
            print_effect(next(g), t_settings)
            print('')
            time.sleep(7) if not t_settings and v_p_settings else None
            time.sleep(1)
            g = set_generator_dnd(0)
            print(Fore.RED, f'{next(g)}')
            dd_mp3.fadeout(3) if m_settings else None
            time.sleep(3) if m_settings else None
            exit()
    else:
        new_number = number + value
        sound_effect('sound/voice_actions/d&d/20.wav', v_a_settings)
        print(f'{next(set_generator_dnd(20))}: {value}')
        time.sleep(2.2) if v_a_settings else None
        if len(str(value)) == 1:
            determination_second_number(v_a_settings, str(value))
        else:
            next_num = determination_first_number(v_a_settings, str(value))
            if next_num:
                determination_second_number(v_a_settings, str(value)[1])
    time.sleep(1) if v_a_settings else None

    determination_announcement(v_a_settings, new_number)
    random_revival(t_settings, v_p_settings)

    if new_number <= 10:
        random_warning(t_settings, v_p_settings)

    return new_number
