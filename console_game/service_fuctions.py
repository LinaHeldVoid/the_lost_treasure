import time
import pygame
import random

from scenario_generator import generate_base


# неверный ввод
def wrong_input(t_settings, v_a_settings):
    sound_effect('../sound/voice_actions/wrong_input.wav', v_a_settings)
    time.sleep(5) if not t_settings and v_a_settings else None
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


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


def quit_menu(t_settings, v_a_settings):
    sound_effect('../sound/voice_actions/option.wav', v_a_settings)
    time.sleep(2) if not t_settings and v_a_settings else None
    print('Вы уверены, что хотите выйти из игры?' + '\n'
          '1) Да, выйти' + '\n'
          '2) Нет, остаться' + '\n')
    record = sound_effect('../sound/voice_actions/quit_menu.wav', v_a_settings)
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


def random_no(t_settings, v_p_settings, no_use):
    choose_no_use = random.choice(no_use)
    if choose_no_use == r_1[119]:
        sound_effect('../sound/voice_person/no_use.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_no_use == r_1[120]:
        sound_effect('../sound/voice_person/no_use_2.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    elif choose_no_use == r_1[121]:
        sound_effect('../sound/voice_person/no_use_3.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    elif choose_no_use == r_1[122]:
        sound_effect('../sound/voice_person/no_use_4.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    else:
        sound_effect('../sound/voice_person/no_use_5.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    return


def random_wont_open(t_settings, v_p_settings, wont_open_list):
    choice = random.choice(wont_open_list)
    if choice == r_2[226]:
        print_effect(choice, t_settings)
    elif choice == r_2[227]:
        print_effect(choice, t_settings)
    else:
        print_effect(choice, t_settings)
    return


def random_try(t_settings, v_p_settings, tries):
    choice = random.choice(tries)
    if choice == r_2[107]:
        print_effect(choice, t_settings)
    elif choice == r_2[108]:
        print_effect(choice, t_settings)
    elif choice == r_2[109]:
        print_effect(choice, t_settings)
    else:
        print_effect(choice, t_settings)
    return


def random_failure(t_settings, v_p_settings, failures):
    choice = random.choice(failures)
    if choice == r_2[116]:
        print_effect(choice, t_settings)
    elif choice == r_2[117]:
        print_effect(choice, t_settings)
    elif choice == r_2[118]:
        print_effect(choice, t_settings)
    else:
        print_effect(choice, t_settings)
    return


def random_open_shelf(t_settings, v_p_settings, open_shelf_again):
    choose_reaction = random.choice(open_shelf_again)
    print_effect(choose_reaction, t_settings)
    return
