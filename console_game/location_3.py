import time
import random
import pygame.mixer
from colorama import Fore, Style

from sound_manager import room_1_2, dd_mp3
from scenario_generator import generate_base
from console_game.sights import poison_effect
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, determination_announcement as d_a, new_determination, death_menu, print_help


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
    g = set_generator(247)
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


def room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, sack_found, determination):

    """переменные"""
    determination = determination
    sack_found = sack_found
    no_use = no_use_generator()
    wont_eat = wont_eat_generator()

    rope_taken = False
    glass_taken = False
    powder_used = False
    powder_eaten = False
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
    print('')
    p_e(next(g), t_settings)
    time.sleep(1)
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
                            g = set_generator(38)
                            print(f'1) {next(g)}'
                                  f'2) {next(g)}'
                                  f'3) {next(g)}'
                                  f'4) {next(g)}'
                                  f'5) {next(g)}'
                                  f'6) {next(g)}' + '\n')
                        else:
                            g = set_generator(25)
                            print(f'1) {next(g)}'
                                  f'2) {next(g)}'
                                  f'3) {next(g)}'
                                  f'4) {next(g)}'
                                  f'5) {next(g)}'
                                  f'6) {next(g)}' + '\n')
                    else:
                        g = set_generator(25)
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
                            g = set_generator(46)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        time.sleep(1)
                        next(g)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/226.wav', v_p_settings)
                        time.sleep(33) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings)
                        time.sleep(2) if s_settings else None
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/231.wav', v_p_settings)
                        time.sleep(24) if not t_settings and v_p_settings else None
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
                            g = set_generator(46)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                        g = set_generator(67)
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
                            g = set_generator(81)
                            p_e(next(g), t_settings)
                            time.sleep(1)

                        g = set_generator(83)
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
                                g = set_generator(88)
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
                                    g = set_generator(96)
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                continue
                        elif option == '2':
                            g = set_generator(175)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            if powder_used:

                                # начало видений
                                break_out_flag = True
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                p_e(next(g), t_settings)
                                time.sleep(1)
                                poison_effect(t_settings, v_a_settings, v_p_settings, m_settings,
                                              s_settings, determination)
                            else:

                                # смерть от кислоты
                                g = set_generator(99)
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
                            continue
                        elif option == '3':
                            break
                        else:
                            print(w(t_settings, v_a_settings))
                            continue

                    # опции для порошка
                    elif option == '4':
                        powder_count += 1
                        if powder_count == 1:
                            g = set_generator(106)
                            p_e(next(g), t_settings)
                            time.sleep(1)

                    # опции для огнива
                    elif option == '5':
                        flint_count += 1
                        if flint_count == 1:
                            g = set_generator(126)
                            p_e(next(g), t_settings)
                            time.sleep(1)

                    # используем кубы или проводим эксперимент (если это возможно)
                    elif option == '6':
                        if break_out_flag:
                            break

                        if sack_found:
                            if steroids_eaten:
                                pass
                            elif steroids_used:
                                print(w(t_settings, v_a_settings))
                                continue
                            else:
                                pass
                        else:
                            print(w(t_settings, v_a_settings))
                            continue
    # book_found = book_found
    # p_e(begin, t_settings)
    # glass_taken = False
    # while True:
    #     if glass_taken:
    #         break
    #     else:
    #         print(f'1) {open_chest}' + '\n')
    #         record = s_e('../sound/voice_actions/option.wav', v_a_settings)
    #         time.sleep(2) if not t_settings and v_a_settings else None
    #         option = input('Введите цифру: ')
    #         record.stop() if v_a_settings else None
    #         if option == '1':
    #             s_e('../sound/voice_actions/6_menu_1.wav', v_a_settings)
    #             time.sleep(13) if not t_settings and v_a_settings else None
    #             while True:
    #                 print(f'1) {get_glass}'
    #                       f'2) {get_rope}'
    #                       f'3) {get_sledgehammer}'
    #                       f'4) {close_chest}'
    #                       f'5) {to_room_2}' + '\n')
    #                 s_e('../sound/voice_actions/option.wav', v_a_settings)
    #                 time.sleep(2) if not t_settings and v_a_settings else None
    #                 option = input('Введите цифру: ')
    #                 if option == '100':
    #                     q(t_settings, v_a_settings)
    #                     continue
    #                 elif option == '0':
    #                     if v_a_settings:
    #                         s_e('../sound/voice_actions/6_menu_1.wav', v_a_settings)
    #                         time.sleep(13) if not t_settings else None
    #                         continue
    #                     else:
    #                         print('Озвучивание опций отключено')
    #                         continue
    #                 elif option == '1':
    #                     if book_found:
    #                         glass_taken = True
    #                         p_e(glass, t_settings)
    #                         time.sleep(1)
    #                         continue
    #                     else:
    #                         p_e(no_use, t_settings)
    #                         time.sleep(1)
    #                         continue
    #                 elif option == '2' or option == '3':
    #                     p_e(no_use, t_settings)
    #                     time.sleep(1)
    #                     continue
    #                 elif option == '4':
    #                     break
    #                 else:
    #                     print(w(t_settings, v_a_settings))
    #                     continue
    #         else:
    #             print(w(t_settings, v_a_settings))
    #             continue
    #
    # """разбираемся с зельем"""
    # while True:
    #     print(f'1) {pour_potion}' + '\n')
    #     s_e('../sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '100':
    #         q(t_settings, v_a_settings)
    #         continue
    #     elif option == '0':
    #         if v_a_settings:
    #             s_e('../sound/voice_actions/6_menu_1.wav', v_a_settings)
    #             time.sleep(13) if not t_settings else None
    #             continue
    #         else:
    #             print('Озвучивание опций отключено')
    #             continue
    #     elif option == '1':
    #         p_e(pouring_potion, t_settings)
    #         time.sleep(2)
    #         p_e(result_1, t_settings)
    #         time.sleep(1)
    #         p_e(result_2, t_settings)
    #         time.sleep(1)
    #         p_e(result_3, t_settings)
    #         time.sleep(1)
    #         p_e(result_4, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(w(t_settings, v_a_settings))
    #         continue
    # while True:
    #     print(f'1) {burn_paper}' + '\n')
    #     s_e('../sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         p_e(start_experiment, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(w(t_settings, v_a_settings))
    #         continue
    # while True:
    #     print(f'1) {put_paper}' + '\n')
    #     s_e('../sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         p_e(paper_in_glass, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(w(t_settings, v_a_settings))
    #         continue
    # bowl_ready = False
    # mistake_made = False
    # while True:
    #     if bowl_ready:
    #         break
    #     else:
    #         print(f'1) {put_glass}' + '\n')
    #         s_e('../sound/voice_actions/option.wav', v_a_settings)
    #         time.sleep(2) if not t_settings and v_a_settings else None
    #         option = input('Введите цифру: ')
    #         if option == '1':
    #             p_e(need_to_think, t_settings)
    #             time.sleep(1)
    #             while True:
    #                 print(f'1) {normal}'
    #                       f'2) {upside_down}' + '\n')
    #                 s_e('../sound/voice_actions/option.wav', v_a_settings)
    #                 time.sleep(2) if not t_settings and v_a_settings else None
    #                 option = input('Введите цифру: ')
    #                 if option == '1':
    #                     mistake_made = True
    #                     p_e(no_effect, t_settings)
    #                     time.sleep(1)
    #                     continue
    #                 elif option == '2':
    #                     bowl_ready = True
    #                     if mistake_made:
    #                         p_e(of_course, t_settings)
    #                         time.sleep(1)
    #                     p_e(effect_1, t_settings)
    #                     time.sleep(1)
    #                     p_e(effect_2, t_settings)
    #                     time.sleep(1)
    #                     p_e(effect_3, t_settings)
    #                     time.sleep(1)
    #                     break
    #         else:
    #             print(w(t_settings, v_a_settings))
    #             continue
    # while True:
    #     print(f'1) {get_coin}' + '\n')
    #     s_e('../sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         p_e(coin_stuck, t_settings)
    #         time.sleep(1)
    #         p_e(bowl_effect, t_settings)
    #         time.sleep(1)
    #         p_e(bowl_destiny_1, t_settings)
    #         time.sleep(1)
    #         p_e(bowl_destiny_2, t_settings)
    #         time.sleep(1)
    #         p_e(read_paper, t_settings)
    #         time.sleep(2)
    #         p_e(paper_1, t_settings)
    #         time.sleep(1)
    #         p_e(paper_2, t_settings)
    #         p_e(paper_3, t_settings)
    #         time.sleep(1)
    #         p_e(paper_4, t_settings)
    #         p_e(paper_5, t_settings)
    #         p_e(paper_6 + '\n', t_settings)
    #         time.sleep(2)
    #         p_e(paper_7, t_settings)
    #         time.sleep(1)
    #         p_e(paper_8 + '\n', t_settings)
    #         time.sleep(2)
    #         p_e(so_cool, t_settings)
    #         time.sleep(1)
    #         p_e(lets_get_out, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(w(t_settings, v_a_settings))
    #         continue
    #
    # """забираем всё из сундука"""
    # rope_taken = False
    # sledgehammer_taken = False
    # print(f'1) {open_chest}' + '\n')
    # s_e('../sound/voice_actions/option.wav', v_a_settings)
    # time.sleep(2) if not t_settings and v_a_settings else None
    # option = input('Введите цифру: ')
    # while True:
    #     if option == '1':
    #         while True:
    #             if rope_taken and sledgehammer_taken:
    #                 break
    #             else:
    #                 print(f'1) {get_rope}'
    #                       f'2) {get_sledgehammer}' + '\n')
    #                 s_e('../sound/voice_actions/option.wav', v_a_settings)
    #                 time.sleep(2) if not t_settings and v_a_settings else None
    #                 option = input('Введите цифру: ')
    #                 if option == '1':
    #                     rope_taken = True
    #                     p_e(rope, t_settings)
    #                     time.sleep(1)
    #                     continue
    #                 elif option == '2':
    #                     sledgehammer_taken = True
    #                     p_e(sledgehammer, t_settings)
    #                     time.sleep(1)
    #                     continue
    #                 else:
    #                     print(w(t_settings, v_a_settings))
    #                     continue
    #     else:
    #         print(w(t_settings, v_a_settings))
    #         continue
    #
    #     """уходим"""
    #     while True:
    #         print(f'1) {get_out}' + '\n')
    #         s_e('../sound/voice_actions/option.wav', v_a_settings)
    #         time.sleep(2) if not t_settings and v_a_settings else None
    #         option = input('Введите цифру: ')
    #         if option == '1':
    #             return
    #         else:
    #             print(w(t_settings, v_a_settings))
    #             continue
