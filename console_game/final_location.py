import pygame
import time
from colorama import Fore
import random

from sound_manager import best_final, neutral_1_final, neutral_2_final, neutral_3_final, worst_final, dd_mp3, room_1_2
from scenario_generator import generate_base
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, determination_announcement as d_a, \
    new_determination, death_menu, print_help, random_death, random_revival


def set_generator(line):
    i = 0
    g = generate_base('text/6_escape.txt')
    while i < line:
        next(g)
        i += 1
    return g


def set_generator_epilogue(line):
    i = 0
    g = generate_base('text/7_epilogue.txt')
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


def escaping(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination, ending):
    if determination <= 10:

        # смерть от потери решимости
        pygame.mixer.stop() if m_settings else None
        random_death(t_settings, v_p_settings)
        s_e('sound/sound_effects/death.wav', s_settings)
        time.sleep(1) if s_settings else None
        dd_mp3.set_volume(0.2) if m_settings else None
        dd_mp3.play(-1) if m_settings else None
        g = set_generator_dnd(34)
        s_e('sound/voice_person/d&d/34.wav', v_p_settings)
        p_e(next(g), t_settings)
        time.sleep(11) if not t_settings and v_p_settings else None
        time.sleep(1)
        s_e('sound/voice_person/d&d/35.wav', v_p_settings)
        p_e(next(g), t_settings)
        print('')
        time.sleep(7) if not t_settings and v_p_settings else None
        time.sleep(1)
        g = set_generator_dnd(0)
        print(Fore.RED, f'{next(g)}')
        dd_mp3.fadeout(3) if m_settings else None
        time.sleep(3) if m_settings else None
        exit()
    else:
        # выходим из пещеры
        g = set_generator(42)
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        time.sleep(1)
        while True:
            g = set_generator(48)
            print(f'1) {next(g)}' + '\n')
            option = input('Введите цифру: ')
            if option == '100':
                q(t_settings, v_a_settings)
                continue
            elif option == '200':
                d_a(v_a_settings, determination)
                continue
            elif option == '0':
                if v_a_settings:
                    continue
                else:
                    print('Озвучивание опций отключено')
                    continue
            elif option.lower() == 'помощь' or option.lower() == 'help':
                print_help(v_a_settings)
                continue
            elif option == '1':
                g = set_generator(49)
                p_e(next(g), t_settings)
                time.sleep(1)
                p_e(next(g), t_settings)
                time.sleep(1)
                break
            else:
                print(w(t_settings, v_a_settings))
                continue

        while True:
            g = set_generator(53)
            print(f'1) {next(g)}' + '\n')
            option = input('Введите цифру: ')
            if option == '100':
                q(t_settings, v_a_settings)
                continue
            elif option == '200':
                d_a(v_a_settings, determination)
                continue
            elif option == '0':
                if v_a_settings:
                    continue
                else:
                    print('Озвучивание опций отключено')
                    continue
            elif option.lower() == 'помощь' or option.lower() == 'help':
                print_help(v_a_settings)
                continue
            elif option == '1':
                if ending == 4 or ending == 5:
                    g = set_generator(58)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                else:
                    g = set_generator(56)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                return
            else:
                print(w(t_settings, v_a_settings))
                continue


def final_location(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination, ending):

    v_a_settings = False
    v_p_settings = False
    asked_stone = False
    stone_examined = False

    g = set_generator(0)
    print('')
    print(next(g))
    time.sleep(1)
    print('')
    while True:
        if asked_stone and stone_examined:
            g = set_generator(21)
            print(next(g))
            time.sleep(1)
            print('')

        if not stone_examined:
            if not asked_stone:
                g = set_generator(3)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
            else:
                g = set_generator(14)
                print(f'1) {next(g)}'
                      f'2) {next(g)}' + '\n')
        else:
            if not asked_stone:
                g = set_generator(7)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
            else:
                g = set_generator(11)
                print(f'1) {next(g)}'
                      f'2) {next(g)}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            q(t_settings, v_a_settings)
            continue
        elif option == '200':
            d_a(v_a_settings, determination)
            continue
        elif option == '0':
            if v_a_settings:
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option.lower() == 'помощь' or option.lower() == 'help':
            print_help(v_a_settings)
            continue
        elif option == '1':
            if stone_examined:

                # смерть от обвала
                g = set_generator(24)
                p_e(next(g), t_settings)
                time.sleep(1)
                print(next(g))
                time.sleep(1)
                s_e('sound/sound_effects/stones.wav', s_settings)
                time.sleep(1) if s_settings else None
                s_e('sound/sound_effects/giant_stone.wav', s_settings)
                time.sleep(7) if s_settings else None
                pygame.mixer.stop() if m_settings else None
                s_e('sound/sound_effects/death.wav', s_settings)
                time.sleep(1) if s_settings else None
                dd_mp3.set_volume(0.2) if m_settings else None
                dd_mp3.play(-1) if m_settings else None
                p_e(next(g), t_settings)
                p_e(next(g), t_settings)
                time.sleep(1)
                print('')
                death_menu(t_settings, v_a_settings, m_settings)
                room_1_2.set_volume(0.2)
                room_1_2.play(-1) if m_settings else None
                determination = new_determination(t_settings, v_p_settings,
                                                  v_a_settings, m_settings,
                                                  s_settings, determination, 7, '-')
                random_revival(t_settings, v_p_settings)

            else:
                stone_examined = True
                g = set_generator(18)
                p_e(next(g), t_settings)
                time.sleep(1)
                p_e(next(g), t_settings)
                time.sleep(1)
                print('')
                continue
        elif option == '2':
            if asked_stone:
                escaping(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination, ending)
                break
            else:
                asked_stone = True
                if ending == 1:
                    g = set_generator(31)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                elif ending == 2 or ending == 3:
                    g = set_generator(35)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                else:
                    g = set_generator(39)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                continue
        elif option == '3':
            if asked_stone:
                print(w(t_settings, v_a_settings))
                continue
            else:
                escaping(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination, ending)
                break

    # ЭПИЛОГ
    pygame.mixer.stop()
    g = set_generator_epilogue(0)
    p_e(next(g), t_settings)
    time.sleep(1)
    print('')
    if ending == 1:
        best_final.set_volume(0.2)
        best_final.play(-1)
        g = set_generator(3)
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        time.sleep(1)
    elif ending == 2:
        neutral_1_final.set_volume(0.2)
        neutral_1_final.play(-1)
        g = set_generator(10)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        time.sleep(1)
    elif ending == 3:
        neutral_2_final.set_volume(0.2)
        neutral_2_final.play(-1)
        g = set_generator(21)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
    elif ending == 4:
        neutral_2_final.set_volume(0.2)
        neutral_2_final.play(-1)
        g = set_generator(32)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
    else:
        worst_final.set_volume(0.2)
        worst_final.play(-1)
        g = set_generator(44)
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        time.sleep(1)
    g = set_generator(55)
    p_e(next(g), t_settings)
    time.sleep(1)
    p_e(next(g), t_settings)
    time.sleep(1)

    # титры
    g = set_generator_epilogue(58)
    p_e(next(g), t_settings)
    time.sleep(1)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    time.sleep(1)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')
    next(g)
    p_e(next(g), t_settings)
    input('Нажмите Enter, чтобы завершить игру: ')
