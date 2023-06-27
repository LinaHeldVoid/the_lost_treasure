import time
import random
import pygame.mixer
from colorama import Fore, Style

from sound_manager import room_1_mp3, room_2_mp3, dd_mp3
from scenario_generator import generate_base
from service_fuctions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n


def room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, book_found):

    """Перевод сценария в переменные"""
    # begin = r_1_2[177]
    # glass = r_1_2[182]
    # pouring_potion = r_1_2[185]
    # result_1 = r_1_2[187]
    # result_2 = r_1_2[188]
    # result_3 = r_1_2[189]
    # result_4 = r_1_2[190]
    # start_experiment = r_1_2[193]
    # paper_in_glass = r_1_2[197]
    # need_to_think = r_1_2[200]
    # no_effect = r_1_2[203]
    # of_course = r_1_2[206]
    # effect_1 = r_1_2[207]
    # effect_2 = r_1_2[208]
    # effect_3 = r_1_2[209]
    # coin_stuck = r_1_2[212]
    # bowl_effect = r_1_2[214]
    # bowl_destiny_1 = r_1_2[215]
    # bowl_destiny_2 = r_1_2[216]
    # read_paper = r_1_2[218]
    # paper_1 = r_1_2[220]
    # paper_2 = r_1_2[221]
    # paper_3 = r_1_2[222]
    # paper_4 = r_1_2[223]
    # paper_5 = r_1_2[224]
    # paper_6 = r_1_2[225]
    # paper_7 = r_1_2[227]
    # paper_8 = r_1_2[228]
    # so_cool = r_1_2[230]
    # lets_get_out = r_1_2[231]
    # rope = r_1_2[234]
    # sledgehammer = r_1_2[236]
    # get_out = r_1_2[239]
    #
    # to_room_2 = r_1_2[0]
    # open_chest = r_1_2[53]
    # close_chest = r_1_2[61]
    # no_use = r_1_2[73]
    # get_rope = r_1_2[179]
    # get_sledgehammer = r_1_2[180]
    # get_glass = r_1_2[181]
    # pour_potion = r_1_2[184]
    # burn_paper = r_1_2[192]
    # put_paper = r_1_2[196]
    # put_glass = r_1_2[199]
    # normal = r_1_2[202]
    # upside_down = r_1_2[205]
    # get_coin = r_1_2[211]

    """алгоритм"""
    book_found = book_found
    p_e(begin, t_settings)
    glass_taken = False
    while True:
        if glass_taken:
            break
        else:
            print(f'1) {open_chest}' + '\n')
            record = s_e('../sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            record.stop() if v_a_settings else None
            if option == '1':
                s_e('../sound/voice_actions/6_menu_1.wav', v_a_settings)
                time.sleep(13) if not t_settings and v_a_settings else None
                while True:
                    print(f'1) {get_glass}'
                          f'2) {get_rope}'
                          f'3) {get_sledgehammer}'
                          f'4) {close_chest}'
                          f'5) {to_room_2}' + '\n')
                    s_e('../sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '100':
                        q(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            s_e('../sound/voice_actions/6_menu_1.wav', v_a_settings)
                            time.sleep(13) if not t_settings else None
                            continue
                        else:
                            print('Озвучивание опций отключено')
                            continue
                    elif option == '1':
                        if book_found:
                            glass_taken = True
                            p_e(glass, t_settings)
                            time.sleep(1)
                            continue
                        else:
                            p_e(no_use, t_settings)
                            time.sleep(1)
                            continue
                    elif option == '2' or option == '3':
                        p_e(no_use, t_settings)
                        time.sleep(1)
                        continue
                    elif option == '4':
                        break
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
            else:
                print(w(t_settings, v_a_settings))
                continue

    """разбираемся с зельем"""
    while True:
        print(f'1) {pour_potion}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '100':
            q(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                s_e('../sound/voice_actions/6_menu_1.wav', v_a_settings)
                time.sleep(13) if not t_settings else None
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':
            p_e(pouring_potion, t_settings)
            time.sleep(2)
            p_e(result_1, t_settings)
            time.sleep(1)
            p_e(result_2, t_settings)
            time.sleep(1)
            p_e(result_3, t_settings)
            time.sleep(1)
            p_e(result_4, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {burn_paper}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            p_e(start_experiment, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {put_paper}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            p_e(paper_in_glass, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue
    bowl_ready = False
    mistake_made = False
    while True:
        if bowl_ready:
            break
        else:
            print(f'1) {put_glass}' + '\n')
            s_e('../sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                p_e(need_to_think, t_settings)
                time.sleep(1)
                while True:
                    print(f'1) {normal}'
                          f'2) {upside_down}' + '\n')
                    s_e('../sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '1':
                        mistake_made = True
                        p_e(no_effect, t_settings)
                        time.sleep(1)
                        continue
                    elif option == '2':
                        bowl_ready = True
                        if mistake_made:
                            p_e(of_course, t_settings)
                            time.sleep(1)
                        p_e(effect_1, t_settings)
                        time.sleep(1)
                        p_e(effect_2, t_settings)
                        time.sleep(1)
                        p_e(effect_3, t_settings)
                        time.sleep(1)
                        break
            else:
                print(w(t_settings, v_a_settings))
                continue
    while True:
        print(f'1) {get_coin}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            p_e(coin_stuck, t_settings)
            time.sleep(1)
            p_e(bowl_effect, t_settings)
            time.sleep(1)
            p_e(bowl_destiny_1, t_settings)
            time.sleep(1)
            p_e(bowl_destiny_2, t_settings)
            time.sleep(1)
            p_e(read_paper, t_settings)
            time.sleep(2)
            p_e(paper_1, t_settings)
            time.sleep(1)
            p_e(paper_2, t_settings)
            p_e(paper_3, t_settings)
            time.sleep(1)
            p_e(paper_4, t_settings)
            p_e(paper_5, t_settings)
            p_e(paper_6 + '\n', t_settings)
            time.sleep(2)
            p_e(paper_7, t_settings)
            time.sleep(1)
            p_e(paper_8 + '\n', t_settings)
            time.sleep(2)
            p_e(so_cool, t_settings)
            time.sleep(1)
            p_e(lets_get_out, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue

    """забираем всё из сундука"""
    rope_taken = False
    sledgehammer_taken = False
    print(f'1) {open_chest}' + '\n')
    s_e('../sound/voice_actions/option.wav', v_a_settings)
    time.sleep(2) if not t_settings and v_a_settings else None
    option = input('Введите цифру: ')
    while True:
        if option == '1':
            while True:
                if rope_taken and sledgehammer_taken:
                    break
                else:
                    print(f'1) {get_rope}'
                          f'2) {get_sledgehammer}' + '\n')
                    s_e('../sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '1':
                        rope_taken = True
                        p_e(rope, t_settings)
                        time.sleep(1)
                        continue
                    elif option == '2':
                        sledgehammer_taken = True
                        p_e(sledgehammer, t_settings)
                        time.sleep(1)
                        continue
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
        else:
            print(w(t_settings, v_a_settings))
            continue

        """уходим"""
        while True:
            print(f'1) {get_out}' + '\n')
            s_e('../sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                return
            else:
                print(w(t_settings, v_a_settings))
                continue
