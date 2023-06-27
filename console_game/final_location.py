import time
import random
import pygame.mixer
from colorama import Fore, Style

from sound_manager import room_1_mp3, room_2_mp3, dd_mp3
from scenario_generator import generate_escape as e, generate_epilogue as ep
from service_fuctions import print_effect as p_e, sound_effect as s_e, wrong_input as w


def final_location(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    """Перевод сценария в переменные"""
    need_to_think = e[242]
    cant_smash = e[248]
    lets_pray = e[249]
    prayer_1 = e[252]
    prayer_2 = e[253]
    hole = e[257]
    lets_go = e[258]
    final = e[262]
    epilogue_1 = ep[265]
    epilogue_2 = ep[266]
    epilogue_3 = ep[267]
    epilogue_4 = ep[268]
    epilogue_5 = ep[269]
    thanks = e[271]
    good_luck = e[272]
    end_game = e[274]

    cave_entrance = e[241]
    smash_wall = e[244]
    pray = e[245]
    through_sledgehammer = e[255]
    escape = e[260]
    dots = e[261]
    epilogue = e[264]

    """алгоритм"""
    print(cave_entrance)
    time.sleep(1)
    p_e(need_to_think, t_settings)
    time.sleep(1)
    while True:
        print(f'1) {smash_wall}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            p_e(cant_smash, t_settings)
            time.sleep(2)
            p_e(lets_pray, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue

    """молитва и побег"""
    while True:
        print(f'1) {pray}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            p_e(prayer_1, t_settings)
            time.sleep(2)
            p_e(prayer_2, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {through_sledgehammer}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            time.sleep(1)
            p_e(hole, t_settings)
            time.sleep(2)
            p_e(lets_go, t_settings)
            time.sleep(1)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {escape}' + '\n')
        s_e('../sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            time.sleep(1)
            p_e(dots, t_settings)
            time.sleep(1)
            p_e(final, t_settings)
            room_1_mp3.fadeout(2000) if m_settings else None
            time.sleep(1)
            time.sleep(2)
            break
        else:
            print(w(t_settings, v_a_settings))
            continue
    
    """ЭПИЛОГ"""
    room_2_mp3.play() if m_settings else None
    print(epilogue)
    time.sleep(2)
    p_e(epilogue_1, t_settings)
    time.sleep(2)
    p_e(epilogue_2, t_settings)
    time.sleep(2)
    p_e(epilogue_3, t_settings)
    time.sleep(2)
    p_e(epilogue_4 + '\n', t_settings)
    time.sleep(2)
    p_e(epilogue_5 + '\n', t_settings)
    time.sleep(2)
    room_2_mp3.fadeout(3000) if m_settings else None
    p_e(thanks, t_settings)
    time.sleep(1)
    p_e(good_luck, t_settings)
    time.sleep(1)
    print(Fore.GREEN, end_game)
    print(Style.RESET_ALL)
    time.sleep(2)
    return
