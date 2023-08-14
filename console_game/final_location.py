import pygame
import time
from colorama import Fore

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
    if determination <= 5:

        # смерть от потери решимости
        pygame.mixer.stop() if m_settings == 'True' else None
        random_death(t_settings, v_p_settings)
        s_e('sound/sound_effects/death.ogg', s_settings, 3)
        time.sleep(1) if s_settings else None
        dd_mp3.set_volume(0.2) if m_settings == 'True' else None
        dd_mp3.play(-1) if m_settings == 'True' else None
        g = set_generator_dnd(34)
        s_e('sound/voice_person/d&d/34.ogg', v_p_settings, 2)
        p_e(next(g), t_settings)
        time.sleep(11) if not t_settings and v_p_settings else None
        s_e('sound/voice_person/d&d/35.ogg', v_p_settings, 2)
        p_e(next(g), t_settings)
        print('')
        time.sleep(7) if not t_settings and v_p_settings else None
        g = set_generator_dnd(0)
        print(Fore.RED, f'{next(g)}')
        dd_mp3.fadeout(3) if m_settings == 'True' else None
        time.sleep(3) if m_settings == 'True' else None
        exit()
    else:
        # выходим из пещеры
        g = set_generator(42)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
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
                p_e(next(g), t_settings)
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
                else:
                    g = set_generator(56)
                    p_e(next(g), t_settings)
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
    print('')
    while True:
        if asked_stone and stone_examined:
            g = set_generator(21)
            print(next(g))
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
                print(next(g))
                s_e('sound/sound_effects/stones.ogg', s_settings, 3)
                time.sleep(1) if s_settings else None
                s_e('sound/sound_effects/giant_stone.ogg', s_settings, 3)
                time.sleep(7) if s_settings else None
                pygame.mixer.stop() if m_settings == 'True' else None
                s_e('sound/sound_effects/death.ogg', s_settings, 3)
                time.sleep(1) if s_settings else None
                dd_mp3.set_volume(0.2) if m_settings == 'True' else None
                dd_mp3.play(-1) if m_settings == 'True' else None
                p_e(next(g), t_settings)
                p_e(next(g), t_settings)
                print('')
                death_menu(t_settings, v_a_settings, m_settings)
                room_1_2.set_volume(0.2)
                room_1_2.play(-1) if m_settings == 'True' else None
                determination = new_determination(t_settings, v_p_settings,
                                                  v_a_settings, m_settings,
                                                  s_settings, determination, 7, '-')
                random_revival(t_settings, v_p_settings, s_settings)

            else:
                stone_examined = True
                g = set_generator(18)
                p_e(next(g), t_settings)
                p_e(next(g), t_settings)
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
                    p_e(next(g), t_settings)
                    p_e(next(g), t_settings)
                elif ending == 2 or ending == 3:
                    g = set_generator(35)
                    p_e(next(g), t_settings)
                    p_e(next(g), t_settings)
                    p_e(next(g), t_settings)
                else:
                    g = set_generator(39)
                    p_e(next(g), t_settings)
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
    print('')
    if ending == 1:
        best_final.set_volume(0.2) if m_settings == 'True' else None
        best_final.play(-1) if m_settings == 'True' else None
        g = set_generator_epilogue(3)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        s_e('sound/voice_person/epilogue/Ep_1.ogg', v_p_settings, 2)
        time.sleep(61) if not t_settings and v_p_settings else None

    elif ending == 2:
        neutral_1_final.set_volume(0.2) if m_settings == 'True' else None
        neutral_1_final.play(-1) if m_settings == 'True' else None
        g = set_generator_epilogue(10)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        s_e('sound/voice_person/epilogue/Ep_2.ogg', v_p_settings, 2)
        time.sleep(109) if not t_settings and v_p_settings else None

    elif ending == 3:
        neutral_2_final.set_volume(0.2) if m_settings == 'True' else None
        neutral_2_final.play(-1) if m_settings == 'True' else None
        g = set_generator_epilogue(21)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        s_e('sound/voice_person/epilogue/Ep_3.ogg', v_p_settings, 2)
        time.sleep(106) if not t_settings and v_p_settings else None

    elif ending == 4:
        neutral_3_final.set_volume(0.2) if m_settings == 'True' else None
        neutral_3_final.play(-1) if m_settings == 'True' else None
        g = set_generator_epilogue(32)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        s_e('sound/voice_person/epilogue/Ep_4.ogg', v_p_settings, 2)
        time.sleep(123) if not t_settings and v_p_settings else None

    else:
        worst_final.set_volume(0.2) if m_settings == 'True' else None
        worst_final.play(-1) if m_settings == 'True' else None
        g = set_generator_epilogue(44)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        print('')
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        p_e(next(g), t_settings)
        s_e('sound/voice_person/epilogue/Ep_5.ogg', v_p_settings, 2)
        time.sleep(119) if not t_settings and v_p_settings else None

    g = set_generator_epilogue(55)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)

    # титры
    g = set_generator_epilogue(58)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
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
    input('Нажмите Enter, чтобы завершить игру: ')
    print('')
    p_e(next(g), t_settings)
    pygame.mixer.fadeout(3) if m_settings == 'True' else None
    time.sleep(3) if m_settings == 'True' else None
