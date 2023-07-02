import time

from scenario_generator import generate_base
from colorama import Fore, Style
from console_game.service_fuctions import print_effect as p_e, sound_effect as s_e


# начало, вход
def start_game(t_settings, v_a_settings, v_p_settings):

    g = generate_base('text/1_prologue.txt')
    s_e('sound/voice_actions/room_1/1_start.wav', v_a_settings)
    print(Fore.GREEN, f'{next(g)}')
    print(Style.RESET_ALL)
    time.sleep(2) if v_a_settings else None
    s_e('sound/voice_actions/room_1/2_prologue.wav', v_a_settings)
    next(g)
    print(next(g))
    time.sleep(2)
    s_e('sound/voice_person/room_1/1_intro_1.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    time.sleep(2)
    s_e('sound/voice_person/room_1/2_intro_2.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(11) if not t_settings and v_p_settings else None
    time.sleep(2)
    s_e('sound/voice_person/room_1/3_intro_3.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(8) if not t_settings and v_p_settings else None
    time.sleep(2)
    s_e('sound/voice_person/room_1/4_intro_4.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(5) if not t_settings and v_p_settings else None
    time.sleep(2)
    s_e('sound/voice_person/room_1/5_intro_5.wav', v_p_settings)
    p_e(next(g) + '\n', t_settings)
    time.sleep(6) if not t_settings and v_p_settings else None
    time.sleep(2)
    next(g)
    next(g)
    s_e('sound/voice_person/room_1/6_begin.wav', v_p_settings)
    p_e(next(g) + '\n', t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    time.sleep(2)
    next(g)
    print(next(g))
    s_e('sound/voice_actions/room_1/3_cave_entrance.wav', v_a_settings)
    time.sleep(2) if v_a_settings else None
    s_e('sound/voice_person/room_1/7_entrance.wav', v_p_settings)
    p_e(next(g) + '\n', t_settings)
    time.sleep(7) if not t_settings and v_p_settings else None
    time.sleep(2)
