import time
import pygame
import random
import datetime
import _thread

from colorama import Fore, Style
from github import Github
from threading import Timer

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
    sound_effect('sound/voice_actions/wrong_input.ogg', v_a_settings, 1)
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
        time.sleep(1)
        return
    else:
        return True


# прерывание озвучки
def sound_interrupt():
    print('')
    answer = input('Введите Enter, чтобы продолжить')
    return

    # permission = 1
    # print(permission)
    # task1 = Thread(target=countdown(period, permission))
    # task2 = Thread(target=answer(permission))
    # task1.start()
    # print(permission)
    # task2.start()


# имитация чтения книги
def print_effect(text, t_settings):
    if t_settings == 'True':
        for i in text:
            time.sleep(0.07)
            print(i, end='', flush=True)
    else:
        print(text, end='')


# управление запуском звука
def sound_effect(sound_path, settings, category):
    try:
        if settings:
            record = pygame.mixer.Sound(sound_path)
            record.play()
            return record
        else:
            return
    except FileNotFoundError:
        sound_bug_report(category, sound_path)


# сообщения об ошибках
def sound_bug_report(category, path):

    # номер версии из GitHub
    with open('game_logs/git_access.txt', 'r', encoding='utf-8') as access:
        log = access.readline()
        password = access.readline()
    g = Github(log, password)
    repo = g.get_repo('LinaHeldVoid/the_lost_treasure')
    branch = repo.get_branch('master')
    version = branch.commit.sha

    # дата и время
    date_time = datetime.datetime.now()
    current_time = date_time.time()
    current_date = date_time.date()

    # характер ошибки
    error = 0
    if category == 1:
        error = 'отсутствует файл озвучки для игрового меню'
    elif category == 2:
        error = 'отсутствует файл озвучки для игровой реплики'
    elif category == 3:
        error = 'отсутствует файл звукового эффекта'

    # записываем отчёт в файл
    with open('game_logs/bug_log.txt', 'a', encoding='utf-8') as bug_report:
        bug_report.write(f'Дата: {current_date}' + '\n')
        bug_report.write(f'Время: {current_time}' + '\n')
        bug_report.write(f'Коммит: {version}' + '\n')
        bug_report.write(f'Описание ошибки: {error}' + '\n')
        bug_report.write(f'Адрес файла на устройстве: {path}' + '\n')
        bug_report.write('\n')
        bug_report.write('\n')
        print(Fore.CYAN, f'Ошибка воспроизведения: {error}' + '\n')
        print(Style.RESET_ALL)
    return


# меню выхода из игры
def quit_menu(t_settings, v_a_settings):
    sound_effect('sound/voice_actions/option.ogg', v_a_settings, 1)
    time.sleep(1) if v_a_settings else None
    print('Вы уверены, что хотите выйти из игры?' + '\n'
          '1) Да, выйти' + '\n'
          '2) Нет, остаться' + '\n')
    record = sound_effect('sound/voice_actions/quit_menu.ogg', v_a_settings, 1)
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


def print_help(v_a_settings):
    print('Цель игры: помогите герою найти в пещере артефакт и выбраться оттуда живым и (по возможности) здоровым.')
    print('В вашем путешествии вас поддерживает Решимость. Растеряв всю Решимость, вы обречёте героя на гибель.')
    print('В любой момент, когда программа ожидает вашего хода, вы можете воспользоваться служебными командами.')
    print('')
    print("Служебные команды в игре:" + '\n'
          "'100': выйти из игры" + '\n'
          "'200': узнать оставшееся количество очков решимости" + '\n'
          "'0': повторить озвучивание последнего меню" + '\n'
          "'помощь'/'help': вывести это сообщение ещё раз" + '\n')
    return


def death_menu(t_settings, v_a_settings, m_settings):
    while True:
        g = set_generator_dnd(1)
        print(next(g))
        next(g)
        print(f'1) {next(g)}'
              f'2) {next(g)}' + '\n')
        record = sound_effect('sound/voice_actions/room_1/10_death_menu.ogg', v_a_settings, 1)
        option = input(f'Введите цифру: ')
        record.stop() if v_a_settings else None
        if option == '1':
            pygame.mixer.fadeout(2) if m_settings else None
            sound_effect('sound/voice_actions/room_1/11_game_resume.ogg', v_a_settings, 1)
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
    if choose_no_use == next(set_generator_2(275)):
        sound_effect('sound/voice_person/no_use.ogg', v_p_settings, 2)
        print_effect(choose_no_use, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_no_use == next(set_generator_2(276)):
        sound_effect('sound/voice_person/no_use_2.ogg', v_p_settings, 2)
        print_effect(choose_no_use, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    elif choose_no_use == next(set_generator_2(277)):
        sound_effect('sound/voice_person/no_use_3.ogg', v_p_settings, 2)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    elif choose_no_use == next(set_generator_2(278)):
        sound_effect('sound/voice_person/no_use_4.ogg', v_p_settings, 2)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/no_use_5.ogg', v_p_settings, 2)
        print_effect(choose_no_use, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    return


# случайная реакция на воскрешение
def random_revival(t_settings, v_p_settings, s_settings):
    sound_effect('sound/sound_effects/revival.ogg', s_settings, 3)
    time.sleep(2) if s_settings else None
    choose_revival = random.choice(revival_generator())
    if choose_revival == next(set_generator_dnd(11)):
        sound_effect('sound/voice_person/d&d/11.ogg', v_p_settings, 2)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(12)):
        sound_effect('sound/voice_person/d&d/12.ogg', v_p_settings, 2)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(13)):
        sound_effect('sound/voice_person/d&d/13.ogg', v_p_settings, 2)
        print_effect(choose_revival, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(14)):
        sound_effect('sound/voice_person/d&d/14.ogg', v_p_settings, 2)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_revival == next(set_generator_dnd(15)):
        sound_effect('sound/voice_person/d&d/15.ogg', v_p_settings, 2)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/d&d/16.ogg', v_p_settings, 2)
        print_effect(choose_revival, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None


# случайное предупреждение о низкой решимости
def random_warning(t_settings, v_p_settings):
    choose_warning = random.choice(warning_generator())
    if choose_warning == next(set_generator_dnd(24)):
        sound_effect('sound/voice_person/d&d/24.ogg', v_p_settings, 2)
        print_effect(choose_warning, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_warning == next(set_generator_2(25)):
        sound_effect('sound/voice_person/d&d/25.ogg', v_p_settings, 2)
        print_effect(choose_warning, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/d&d/26.ogg', v_p_settings, 2)
        print_effect(choose_warning, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None


# случайное уведомление об окончательной смерти персонажа
def random_death(t_settings, v_p_settings):
    choose_warning = random.choice(death_generator())
    if choose_warning == next(set_generator_dnd(30)):
        sound_effect('sound/voice_person/d&d/30.ogg', v_p_settings, 2)
        print_effect(choose_warning, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    elif choose_warning == next(set_generator_2(31)):
        sound_effect('sound/voice_person/d&d/31.ogg', v_p_settings, 2)
        print_effect(choose_warning, t_settings)
        time.sleep(4.5) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/d&d/32.ogg', v_p_settings, 2)
        print_effect(choose_warning, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None


# обработка озвучки чисел
def determination_second_number(v_a_settings, some_number):
    if some_number == '1':
        sound_effect('sound/voice_actions/d&d/point_1.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '2':
        sound_effect('sound/voice_actions/d&d/point_2.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '3':
        sound_effect('sound/voice_actions/d&d/point_3.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '4':
        sound_effect('sound/voice_actions/d&d/point_4.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '5':
        sound_effect('sound/voice_actions/d&d/point_5.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '6':
        sound_effect('sound/voice_actions/d&d/point_6.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '7':
        sound_effect('sound/voice_actions/d&d/point_7.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    elif some_number == '8':
        sound_effect('sound/voice_actions/d&d/point_8.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    else:
        sound_effect('sound/voice_actions/d&d/point_9.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
    return


def determination_first_number(v_a_settings, some_number):
    if some_number == '10':
        sound_effect('sound/voice_actions/d&d/point_10.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '11':
        sound_effect('sound/voice_actions/d&d/point_11.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '12':
        sound_effect('sound/voice_actions/d&d/point_12.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '13':
        sound_effect('sound/voice_actions/d&d/point_13.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '14':
        sound_effect('sound/voice_actions/d&d/point_14.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '15':
        sound_effect('sound/voice_actions/d&d/point_15.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '16':
        sound_effect('sound/voice_actions/d&d/point_16.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '17':
        sound_effect('sound/voice_actions/d&d/point_17.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '18':
        sound_effect('sound/voice_actions/d&d/point_18.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    elif some_number == '19':
        sound_effect('sound/voice_actions/d&d/point_13.ogg', v_a_settings, 1)
        time.sleep(1) if v_a_settings else None
        return False
    else:
        if some_number[0] == '2':
            sound_effect('sound/voice_actions/d&d/point_20.ogg', v_a_settings, 1)
            time.sleep(1) if v_a_settings else None
            if some_number[1] == '0':
                return False
            else:
                return True
        elif some_number[0] == '3':
            sound_effect('sound/voice_actions/d&d/point_30.ogg', v_a_settings, 1)
            time.sleep(1) if v_a_settings else None
            if some_number[1] == '0':
                return False
            else:
                return True
        elif some_number[0] == '4':
            sound_effect('sound/voice_actions/d&d/point_40.ogg', v_a_settings, 1)
            time.sleep(1) if v_a_settings else None
            if some_number[1] == '0':
                return False
            else:
                return True
        else:
            sound_effect('sound/voice_actions/d&d/point_50.ogg', v_a_settings, 1)
            time.sleep(1) if v_a_settings else None
            return False


# озвучка количества очков решимости
def determination_announcement(v_a_settings, new_number):
    print(f'{next(set_generator_dnd(22))}: {new_number}')
    sound_effect('sound/voice_actions/d&d/22.ogg', v_a_settings, 1)
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

        sound_effect('sound/voice_actions/d&d/21.ogg', v_a_settings, 1)
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
            sound_effect('sound/sound_effects/death.ogg', s_settings, 3)
            time.sleep(1) if s_settings else None
            dd_mp3.set_volume(0.2) if m_settings else None
            dd_mp3.play(-1) if m_settings else None
            g = set_generator_dnd(34)
            sound_effect('sound/voice_person/d&d/34.ogg', v_p_settings, 2)
            print_effect(next(g), t_settings)
            time.sleep(11) if not t_settings and v_p_settings else None
            time.sleep(1)
            sound_effect('sound/voice_person/d&d/35.ogg', v_p_settings, 2)
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
        sound_effect('sound/voice_actions/d&d/20.ogg', v_a_settings, 1)
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

    if new_number <= 10:
        random_warning(t_settings, v_p_settings)

    return new_number
