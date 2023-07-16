import time

from console_game.introduction import start_game
from console_game.location_1 import room_1
from console_game.location_2 import room_2
from console_game.location_3 import room_1_again
from console_game.service_functions import print_help
from console_game.final_location import final_location
from sound_manager import room_1_mp3, room_2_mp3, dd_mp3
# from read_scenario import prologue as p, room_1 as r_1, room_2 as r_2, \
#     riddle, room_1_again as r_1_2, escape as e, epilogue as ep


# запуск игры в консоли
def run_game_console(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):
    print('')
    print_help(v_a_settings)
    input('Нажмите Enter, чтобы продолжить: ')
    room_1_mp3.set_volume(0.2) if m_settings else None
    room_1_mp3.play(-1) if m_settings else None
    start_game(t_settings, v_a_settings, v_p_settings)
    points_1 = room_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    game_data = room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, points_1)
    points_2 = game_data['determination']
    sack_found = game_data['sack_took']
    final_report = room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, sack_found, points_2)
    determination = final_report['determination']
    ending = final_report['ending']
    final_location(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination, ending)
