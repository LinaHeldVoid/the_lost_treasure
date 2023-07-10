import time
import random
import pygame.mixer
from colorama import Fore, Style

from sound_manager import room_1_2
from scenario_generator import generate_base
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, numbers_check as n_c, determination_announcement as d_a, \
    new_determination, death_menu, print_help


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
    g = set_generator_1(145)
    while i < 5:
        no_use.append(next(g))
        i += 1
    return no_use


def room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, sack_found, determination):

    """переменные"""
    determination = determination
    sack_found = sack_found
    rope_taken = False
    glass_taken = False
    powder_used = False
    steroids_used = False
    steroids_eaten = False

    """алгоритм"""
    room_1_2.set_volume(0.2) if m_settings else None
    room_1_2.play(-1) if m_settings else None
    g = set_generator(0)
    print(next(g))
    print('')
    p_e(next(g), t_settings)
    time.sleep(1)
    while True:
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
