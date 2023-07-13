import time
import random
import pygame.mixer
from colorama import Fore, Style

from sound_manager import room_1_2, dd_mp3
from scenario_generator import generate_base
from console_game.sights import poison_effect
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, determination_announcement as d_a, \
    new_determination, death_menu, print_help, random_revival


def set_generator(line):
    i = 0
    g = generate_base('text/5_back_to_room_1.txt')
    while i < line:
        next(g)
        i += 1
    return g


def set_generator_1(line):
    i = 0
    g = generate_base('text/2_room_1.txt')
    while i < line:
        next(g)
        i += 1
    return g


def no_use_generator():
    no_use = []
    i = 0
    g = set_generator(283)
    while i < 5:
        no_use.append(next(g))
        i += 1
    return no_use


def wont_eat_generator():
    wont_eat = []
    i = 0
    g = set_generator(164)
    while i < 3:
        wont_eat.append(next(g))
        i += 1
    return wont_eat


def random_wont_eat(wont_eat_list, t_settings):
    wont_eat = random.choice(wont_eat_list)
    return wont_eat


def taking_powder(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination, wont_eat,
                  used, refuses):
    d = {}
    while True:
        g = set_generator(125)
        print(f'1) {next(g)}'
              f'2) {next(g)}'
              f'3) {next(g)}' + '\n')
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

        # съесть
        elif option == '1':
            if wont_eat:
                random_wont_eat(refuses, t_settings)
                continue
            else:
                wont_eat = True
                g = set_generator(130)
                p_e(next(g), t_settings)
                time.sleep(1)
                next(g)
                time.sleep(1)
                p_e(next(g), t_settings)
                time.sleep(1)
                determination = new_determination(t_settings, v_p_settings,
                                                  v_a_settings, m_settings,
                                                  s_settings, determination, 2, '-')
                continue

        # высыпать
        elif option == '2':
            used = True
            g = set_generator(137)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            print(next(g))
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            break
        elif option == '3':
            break
        else:
            print(w(t_settings, v_a_settings))
            continue

    d['wont_eat'] = wont_eat
    d['used'] = used
    return d


def taking_steroids(t_settings, v_a_settings, determination, eaten, wont_eat, used, refuses):
    d = {}
    while True:
        g = set_generator(160)
        print(f'1) {next(g)}'
              f'2) {next(g)}'
              f'3) {next(g)}' + '\n')
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
            if wont_eat:
                random_wont_eat(refuses, t_settings)
                continue
            else:
                g = set_generator(165)
                p_e(next(g), t_settings)
                time.sleep(1)
                if determination > 42:
                    eaten = True
                    g = set_generator(168)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    break
                else:
                    wont_eat = True
                    g = set_generator(178)
                    p_e(next(g), t_settings)
                    time.sleep(1)
                    continue
        elif option == '2':
            used = True
            g = set_generator(186)
            p_e(next(g), t_settings)
            time.sleep(1)
            next(g)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            continue
        elif option == '3':
            break
        else:
            print(w(t_settings, v_a_settings))
            continue

    d['eaten'] = eaten
    d['wont_eat'] = wont_eat
    d['used'] = used
    return d


def experiment(t_settings, v_p_settings, v_a_settings, m_settings, s_settings, determination):
    while True:
        g = set_generator(199)
        p_e(next(g), t_settings)
        time.sleep(1)
        p_e(next(g), t_settings)
        time.sleep(1)
        while True:
            g = set_generator(201)
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
                g = set_generator(203)
                p_e(next(g), t_settings)
                time.sleep(1)
                while True:
                    g = set_generator(205)
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
                        g = set_generator(206)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        while True:
                            g = set_generator(208)
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
                                g = set_generator(209)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                while True:
                                    g = set_generator(211)
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
                                        g = set_generator(220)
                                        p_e(next(g), t_settings)
                                        time.sleep(1)
                                        p_e(next(g), t_settings)
                                        time.sleep(1)
                                        p_e(next(g), t_settings)
                                        time.sleep(1)
                                        return
                                    elif option == '2':
                                        g = set_generator(215)
                                        p_e(next(g), t_settings)
                                        time.sleep(1)
                                        determination = new_determination(t_settings, v_p_settings, v_a_settings,
                                                                          m_settings, s_settings, determination, 1, '-')
                                        continue
                            else:
                                print(w(t_settings, v_a_settings))
                                continue
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
            else:
                print(w(t_settings, v_a_settings))
                continue


def room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, sack_found, determination):

    """переменные"""
    v_a_settings = False
    v_p_settings = False
    determination = determination
    sack_found = sack_found
    no_use = no_use_generator()
    wont_eat = wont_eat_generator()
    final_report = {}
    ending = 0

    rope_taken = False
    glass_taken = False
    powder_used = False
    wont_eat_powder = False
    steroids_used = False
    steroids_eaten = False
    wont_eat_steroids = False
    break_out_flag = False
    poison_poured = False
    read_count = 0
    glass_count = 0
    powder_count = 0
    steroids_count = 0
    flint_count = 0

    """алгоритм"""
    room_1_2.set_volume(0.2) if m_settings else None
    room_1_2.play(-1) if m_settings else None
    g = set_generator(0)
    print(next(g))
    next(g)
    p_e(next(g), t_settings)
    time.sleep(1)
    print('')
    while True:
        if break_out_flag:
            break

        g = set_generator(4)
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
            s_e('sound/sound_effects/open_chest.wav', s_settings)
            time.sleep(1.5) if s_settings else None
            while True:
                if break_out_flag:
                    break

                if glass_taken:
                    g = set_generator(14)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}' + '\n')
                else:
                    g = set_generator(10)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' + '\n')
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
                    r_n(t_settings, v_p_settings, no_use)
                    continue
                elif option == '2':
                    if glass_taken:
                        s_e('sound/sound_effects/close_chest.wav', s_settings)
                        time.sleep(1.5) if s_settings else None
                        break
                    else:
                        glass_taken = True
                        g = set_generator(18)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        continue
                elif option == '3':
                    if glass_taken:
                        print(w(t_settings, v_a_settings))
                        continue
                    else:
                        s_e('sound/sound_effects/close_chest.wav', s_settings)
                        time.sleep(1.5) if s_settings else None
                        break
        elif option == '2':
            if not glass_taken:
                g = set_generator(21)
                p_e(next(g), t_settings)
                time.sleep(1)
                continue
            else:
                while True:
                    if break_out_flag:
                        break

                    if sack_found:
                        if steroids_eaten:
                            if powder_used:
                                g = set_generator(51)
                                print(f'1) {next(g)}'
                                      f'2) {next(g)}'
                                      f'3) {next(g)}'
                                      f'4) {next(g)}'
                                      f'5) {next(g)}' + '\n')
                            else:
                                g = set_generator(44)
                                print(f'1) {next(g)}'
                                      f'2) {next(g)}'
                                      f'3) {next(g)}'
                                      f'4) {next(g)}'
                                      f'5) {next(g)}'
                                      f'6) {next(g)}' + '\n')
                        else:
                            if powder_used:
                                g = set_generator(38)
                                print(f'1) {next(g)}'
                                      f'2) {next(g)}'
                                      f'3) {next(g)}'
                                      f'4) {next(g)}'
                                      f'5) {next(g)}' + '\n')
                            else:
                                g = set_generator(25)
                                print(f'1) {next(g)}'
                                      f'2) {next(g)}'
                                      f'3) {next(g)}'
                                      f'4) {next(g)}'
                                      f'5) {next(g)}'
                                      f'6) {next(g)}' + '\n')
                    else:
                        if powder_used:
                            g = set_generator(57)
                            print(f'1) {next(g)}'
                                  f'2) {next(g)}'
                                  f'3) {next(g)}'
                                  f'4) {next(g)}' + '\n')
                        else:
                            g = set_generator(32)
                            print(f'1) {next(g)}'
                                  f'2) {next(g)}'
                                  f'3) {next(g)}'
                                  f'4) {next(g)}'
                                  f'5) {next(g)}' + '\n')
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

                    # перечитываем запись в дневнике
                    elif option == '1':
                        read_count += 1
                        if read_count == 1:
                            g = set_generator(63)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        time.sleep(1)
                        next(g)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/222.wav', v_p_settings)
                        time.sleep(23) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/226.wav', v_p_settings)
                        time.sleep(33) if not t_settings and v_p_settings else None
                        time.sleep(2)
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        s_e('sound/voice_person/room_2/231.wav', v_p_settings)
                        time.sleep(24) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/235.wav', v_p_settings)
                        time.sleep(24) if not t_settings and v_p_settings else None
                        s_e('sound/sound_effects/papers_close.mp3', s_settings)
                        time.sleep(15) if s_settings else None
                        next(g)
                        time.sleep(2)
                        continue

                    # перечитываем журнал испытаний
                    elif option == '2':
                        read_count += 1
                        if read_count == 1:
                            g = set_generator(63)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                        g = set_generator(84)
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
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
                        s_e('sound/voice_person/room_2/245.wav', v_p_settings)
                        time.sleep(60) if not t_settings and v_p_settings else None
                        s_e('sound/sound_effects/papers_close.mp3', s_settings)
                        time.sleep(2) if s_settings else None

                    # опции для стакана
                    elif option == '3':
                        if break_out_flag:
                            break

                        glass_count += 1
                        if glass_count == 1:
                            g = set_generator(98)
                            p_e(next(g), t_settings)
                            time.sleep(1)

                        g = set_generator(100)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}' + '\n')
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
                            if poison_poured:
                                r_n(t_settings, v_p_settings, no_use)
                                continue
                            else:
                                poison_poured = True
                                g = set_generator(105)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                print(next(g))
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                if steroids_eaten:
                                    next(g)
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                else:
                                    g = set_generator(113)
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                continue
                        elif option == '2':
                            g = set_generator(192)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            if powder_used:

                                # начало видений
                                break_out_flag = True
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                room_1_2.fadeout(2) if m_settings else None
                                time.sleep(2) if m_settings else None
                                final_report = poison_effect(t_settings, v_a_settings, v_p_settings,
                                                             m_settings, s_settings, determination)
                                determination = final_report['determination']
                                g = set_generator(225)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                continue
                            else:

                                # смерть от кислоты
                                g = set_generator(116)
                                room_1_2.stop() if m_settings else None
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
                            continue
                        elif option == '3':
                            break
                        else:
                            print(w(t_settings, v_a_settings))
                            continue

                    # опции для огнива
                    elif option == '4':
                        flint_count += 1
                        if flint_count == 1:
                            g = set_generator(143)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                        while True:
                            g = set_generator(145)
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

                                # смерть от взрыва
                                g = set_generator(149)
                                room_1_2.stop() if m_settings else None
                                s_e('sound/sound_effects/death.wav', s_settings)
                                time.sleep(1) if s_settings else None
                                dd_mp3.set_volume(0.2) if m_settings else None
                                dd_mp3.play(-1) if m_settings else None
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                print(next(g))
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                death_menu(t_settings, v_a_settings, m_settings)
                                room_1_2.set_volume(0.2)
                                room_1_2.play(-1) if m_settings else None
                                determination = new_determination(t_settings, v_p_settings,
                                                                  v_a_settings, m_settings,
                                                                  s_settings, determination, 7, '-')
                                random_revival(t_settings, v_p_settings)

                    else:
                        if option == '5':
                            powder_count += 1
                            if not powder_used:

                                # опции для порошка
                                if powder_count == 1:
                                    g = set_generator(123)
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                result = taking_powder(t_settings, v_a_settings, v_p_settings, m_settings,
                                                       s_settings,
                                                       determination, wont_eat_powder, powder_used, wont_eat)
                                wont_eat_powder = result['wont_eat']
                                powder_used = result['used']
                                continue
                            else:
                                if sack_found:

                                    # эксперимент
                                    if steroids_eaten:
                                        break_out_flag = True
                                        experiment(t_settings, v_p_settings, v_a_settings, m_settings,
                                                   s_settings, determination)
                                        final_report['fails'] = '+++'
                                        continue

                                    # опции для кубика
                                    steroids_count += 1
                                    if steroids_count == 1:
                                        g = set_generator(158)
                                        p_e(next(g), t_settings)
                                        time.sleep(1)
                                        continue
                                    else:
                                        result = taking_steroids(t_settings, v_a_settings, determination,
                                                                 steroids_eaten, wont_eat_steroids, steroids_used,
                                                                 wont_eat)
                                        steroids_eaten = result['eaten']
                                        wont_eat_steroids = result['wont_eat']
                                        steroids_used = result['used']
                                        continue
                                else:
                                    print(w(t_settings, v_a_settings))
                                    continue

                        # используем кубы или проводим эксперимент (если это возможно)
                        elif option == '6':
                            if sack_found and not powder_used:

                                # эксперимент
                                if steroids_eaten:
                                    break_out_flag = True
                                    experiment(t_settings, v_p_settings, v_a_settings, m_settings,
                                               s_settings, determination)
                                    final_report['fails'] = '+++'
                                    continue

                                elif steroids_used:
                                    print(w(t_settings, v_a_settings))
                                    continue
                                else:

                                    # опции для кубика
                                    steroids_count += 1
                                    if steroids_count == 1:
                                        g = set_generator(158)
                                        p_e(next(g), t_settings)
                                        time.sleep(1)
                                    result = taking_steroids(t_settings, v_a_settings, determination,
                                                             steroids_eaten, wont_eat_steroids, steroids_used, wont_eat)
                                    steroids_eaten = result['eaten']
                                    wont_eat_steroids = result['wont_eat']
                                    steroids_used = result['used']
                                    continue
                            else:
                                print(w(t_settings, v_a_settings))
                                continue

    # определяем концовку
    if final_report['fails'] == '+++':
        ending = 1
    elif final_report['fails'] == 0:
        ending = 2
    elif final_report['fails'] == 1:
        ending = 3
    elif final_report['fails'] == 2:
        ending = 4
    else:
        ending = 5

    # поднимаем монетку
    letter_read = False
    g = set_generator(227)
    p_e(next(g), t_settings)
    time.sleep(1)
    while True:
        if letter_read:
            break

        g = set_generator(229)
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
            g = set_generator(230)
            p_e(next(g), t_settings)
            time.sleep(1)
            print(next(g))
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            print(next(g))
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)

            # читаем послание колдуна
            letter_read = True
            s_e('sound/sound_effects/papers_open.mp3', s_settings)
            time.sleep(2) if s_settings else None
            p_e(next(g), t_settings)
            time.sleep(1)
            print('')
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            p_e(next(g), t_settings)
            time.sleep(1)
            print('')
            p_e(next(g), t_settings)
            time.sleep(1)
            p_e(next(g), t_settings)
            time.sleep(1)
            s_e('sound/sound_effects/papers_close.mp3', s_settings)
            time.sleep(2) if s_settings else None

            # реакция героя в зависимости от концовки
            if ending == 1:
                g = set_generator(252)
                p_e(next(g), t_settings)
                time.sleep(1)
            elif ending == 2 or ending == 3:
                g = set_generator(255)
                p_e(next(g), t_settings)
                time.sleep(1)
                p_e(next(g), t_settings)
                time.sleep(1)
            else:
                g = set_generator(259)
                p_e(next(g), t_settings)
                time.sleep(1)
                p_e(next(g), t_settings)
                time.sleep(1)
                print('')
                p_e(next(g), t_settings)
                p_e(next(g), t_settings)
                time.sleep(1)
        else:
            print(w(t_settings, v_a_settings))
            continue

    # уходим
    g = set_generator(264)
    p_e(next(g), t_settings)
    time.sleep(1)
    p_e(next(g), t_settings)
    time.sleep(1)
    while True:
        if rope_taken:
            g = set_generator(279)
            print(f'1) {next(g)}' + '\n')
        else:
            g = set_generator(272)
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
            if rope_taken:
                p_e(next(g), t_settings)
                time.sleep(1)
                final_report['determination'] = determination
                final_report['ending'] = ending
                return final_report
            else:
                s_e('sound/sound_effects/open_chest.wav', s_settings)
                time.sleep(1.5) if s_settings else None
                while True:
                    g = set_generator(267)
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
                        rope_taken = True
                        s_e('sound/sound_effects/close_chest.wav', s_settings)
                        time.sleep(1.5) if s_settings else None
                        g = set_generator(276)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        break
                    elif option == '2':
                        s_e('sound/sound_effects/close_chest.wav', s_settings)
                        time.sleep(1.5) if s_settings else None
                        break
        elif option == '2':
            if rope_taken:
                print(w(t_settings, v_a_settings))
                continue
            else:
                g = set_generator(290)
                p_e(next(g), t_settings)
                time.sleep(1)
                continue
        else:
            print(w(t_settings, v_a_settings))
            continue
