import time
import random
import pygame.mixer
from colorama import Fore, Style

from sound_manager import room_1_mp3, room_2_mp3, dd_mp3
from scenario_generator import generate_room_2 as r_2, generate_riddle as g_r, generate_room_1 as r_1
from service_fuctions import print_effect as p_e, sound_effect as s_e, wrong_input as w


# рабочий кабинет
def room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    """Перевод сценария в переменные"""
    look_around_1 = r_2[1]
    look_around_2 = r_2[2]
    table_examined_1 = r_2[8]
    table_examined_2 = r_2[9]
    shelf_1 = r_2[16]
    shelf_2_1 = r_2[19]
    shelf_2_2 = r_2[20]
    shelf_3 = r_2[23]
    shelves_examined = r_2[24]
    open_shelf_again = [r_2[27], r_2[28], r_2[29]]
    candle_lightened = r_2[38]
    no_light = r_2[42]
    mechanism_examined_1 = r_2[45]
    mechanism_examined_2 = r_2[46]
    string_1 = riddle[1]
    string_2 = riddle[2]
    string_3 = riddle[5]
    string_4 = riddle[6]
    string_5 = riddle[9]
    string_6 = riddle[10]
    reactions = [r_2[49], r_2[51], r_2[52], r_2[55], r_2[56], r_2[57], r_2[59],
                 r_2[62], r_2[63], r_2[64], r_2[66], r_2[69], r_2[70], r_2[73]]
    riddle_strings = [riddle[12], riddle[13], riddle[14], riddle[15],
                      riddle[17], riddle[18], riddle[19], riddle[20],
                      riddle[22], riddle[23], riddle[24], riddle[25],
                      riddle[27], riddle[28], riddle[29], riddle[30]]
    four_candles_1 = r_2[78]
    four_candles_2 = r_2[79]
    chest_closed_1 = r_2[82]
    chest_closed_2 = r_2[83]
    candles_1 = r_2[91]
    candles_2 = r_2[92]
    need_to_read = r_2[95]
    candles_examined_1 = r_2[97]
    candles_examined_2 = r_2[98]
    candles_examined_3 = r_2[99]
    tries = [r_2[107], r_2[108], r_2[109], r_2[110]]
    first_failure = r_2[113]
    failures = [r_2[116], r_2[117], r_2[118], r_2[119]]
    death_1 = r_2[123]
    death_2 = r_2[124]
    riddle_solved_1 = r_2[128]
    riddle_solved_2 = r_2[129]
    chest_opened = r_2[132]
    begin_reading = r_2[138]
    line_1 = r_2[140]
    line_2 = r_2[141]
    line_3 = r_2[143]
    line_4 = r_2[144]
    need_to_think = r_2[146]
    why_religion = r_2[147]
    back_to_business = r_2[148]
    sack_1 = r_2[151]
    sack_2 = r_2[152]
    sack_3 = r_2[153]
    cant_close = r_2[234]
    mechanism_again = r_2[237]
    stone_inserted = r_2[156]
    diamond_correct = r_2[158]
    great_diamond = r_2[159]
    follow_the_light = r_2[160]
    storage_found = r_2[163]
    storage_opened = r_2[166]
    read_1 = r_2[167]
    read_2 = r_2[168]
    read_3 = r_2[175]
    book_1 = r_2[177]
    book_2 = r_2[178]
    book_3 = r_2[179]
    book_4 = r_2[181]
    book_5 = r_2[182]
    book_6 = r_2[183]
    book_7 = r_2[184]
    book_8 = r_2[186]
    book_9 = r_2[187]
    book_10 = r_2[189]
    book_11 = r_2[190]
    book_12 = r_2[191]
    conclusion = r_2[193]
    read_log_1 = r_2[196]
    read_log_2 = r_2[197]
    log_1 = r_2[199]
    log_2 = r_2[200]
    log_3 = r_2[201]
    log_4 = r_2[202]
    log_5 = r_2[203]
    log_6 = r_2[204]
    log_7 = r_2[205]
    log_8 = r_2[206]
    log_9 = r_2[207]
    log_10 = r_2[208]
    log_11 = r_2[209]
    log_12 = r_2[210]
    much_information = r_2[212]
    get_steroids_1 = r_2[215]
    get_steroids_2 = r_2[216]
    get_steroids_3 = r_2[217]
    get_tools = r_2[219]
    get_away = r_2[220]
    no_use = [r_1[119], r_1[120], r_1[121], r_1[122], r_1[123]]

    room_2_location = r_2[0]
    examine_the_table = r_2[4]
    examine_altar = r_2[5]
    open_shelf_1 = r_2[11]
    open_shelf_2 = r_2[12]
    open_shelf_3 = r_2[13]
    light_candle = r_2[34]
    examine_mechanism = r_2[44]
    read_paper_1 = r_2[31]
    read_paper_2 = r_2[32]
    read_paper_3 = r_2[33]
    papers_away = r_2[246]
    combine_papers = r_2[68]
    leave_table = r_2[75]
    examine_chest = r_2[81]
    read_riddle = r_2[85]
    open_chest = r_2[86]
    look_at_candles = r_2[87]
    leave_altar = r_2[88]
    light_angel = r_2[101]
    light_crow = r_2[102]
    light_censer = r_2[103]
    light_hood = r_2[104]
    dart_whoosh = r_2[122]
    chest_unlocked = r_2[127]
    read_papers = r_2[134]
    take_sack = r_2[135]
    close_chest = r_2[231]
    insert_stone = r_2[155]
    click = r_2[157]
    knock_the_wall = r_2[162]
    hit_the_wall = r_2[165]
    read_book = r_2[170]
    read_log = r_2[171]
    take_bundle = r_2[172]
    leave_location = r_2[222]
    chest_wont_open = [r_2[226], r_2[227], r_2[228]]
    leave_candles = r_2[230]
    leave_storage = r_2[239]
    cant_go = r_2[244]
    examine_storage = r_2[241]
    game_over = r_1[24]
    death_menu = r_1[25]
    load_game = r_1[27]
    exit_game = r_1[28]
    game_resume = r_1[31]

    """алгоритм"""
    break_out_flag = False
    altar_examined = False
    open_1 = False
    open_2 = False
    open_3 = False
    table_is_examined = False
    mechanism_is_examined = False
    light_on = False
    paper_1_read = False
    paper_2_read = False
    paper_3_read = False
    papers_combined = False
    сhest_opened = False
    tries_number = 0
    room_2_mp3.play(-1) if m_settings else None
    print(room_2_location)
    time.sleep(1)
    print_effect(look_around_1, t_settings)
    time.sleep(1)
    print_effect(look_around_2, t_settings)
    time.sleep(1)

    """главное меню"""
    while True:
        if break_out_flag:
            break

        if open_1 and open_2 and open_3:
            if papers_combined:
                print(f'1) {examine_the_table}'
                      f'2) {examine_altar}' + '\n')
            else:
                print(f'1) {examine_the_table}'
                      f'2) {examine_altar}'
                      f'3) {read_papers}' + '\n')
        else:
            print(f'1) {examine_the_table}'
                  f'2) {examine_altar}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            quit_menu(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':

            """осматриваем стол"""
            if not table_is_examined:
                table_is_examined = True
                print_effect(table_examined_1, t_settings)
                time.sleep(1)
                print_effect(table_examined_2, t_settings)
                time.sleep(1)
            while True:

                """проверяем полки"""
                if open_1 and open_2 and open_3 and mechanism_is_examined:
                    print_effect(shelves_examined, t_settings)
                    break
                else:
                    if light_on:
                        print(f'1) {open_shelf_1}'
                              f'2) {open_shelf_2}'
                              f'3) {open_shelf_3}'
                              f'4) {examine_mechanism}'
                              f'5) {leave_table}' + '\n')
                    else:
                        print(f'1) {open_shelf_1}'
                              f'2) {open_shelf_2}'
                              f'3) {open_shelf_3}'
                              f'4) {examine_mechanism}'
                              f'5) {light_candle}'
                              f'6) {leave_table}' + '\n')
                    option = input('Введите цифру: ')
                    if option == '100':
                        quit_menu(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            continue
                        else:
                            print('Озвучивание опций отключено')
                            continue
                    elif option == '1':
                        if open_1:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            time.sleep(1)
                            continue
                        else:
                            open_1 = True
                            print_effect(shelf_1, t_settings)
                            time.sleep(1)
                            continue
                    elif option == '2':
                        if open_2:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            time.sleep(1)
                            continue
                        else:
                            open_2 = True
                            print_effect(shelf_2_1, t_settings)
                            time.sleep(1)
                            print_effect(shelf_2_2, t_settings)
                            time.sleep(1)
                            continue
                    elif option == '3':
                        if open_3:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            time.sleep(1)
                            continue
                        else:
                            open_3 = True
                            print_effect(shelf_3, t_settings)
                            time.sleep(1)
                            continue
                    elif option == '4':
                        if mechanism_is_examined:
                            random_no(t_settings, v_p_settings, no_use)
                            time.sleep(1)
                            continue
                        else:
                            if light_on is True:
                                mechanism_is_examined = True
                                print_effect(mechanism_examined_1, t_settings)
                                time.sleep(1)
                                print_effect(mechanism_examined_2, t_settings)
                                time.sleep(1)
                                continue
                            else:
                                print_effect(no_light, t_settings)
                                time.sleep(1)
                                continue
                    elif option == '5':
                        if light_on:
                            break
                        else:
                            light_on = True
                            print_effect(candle_lightened, t_settings)
                            time.sleep(1)
                    elif option == '6':
                        if not light_on:
                            break
                        else:
                            print(wrong_input(t_settings, v_a_settings))
                            continue
                    else:
                        print(wrong_input(t_settings, v_a_settings))
                        continue
        elif option == '2':
            if break_out_flag:
                break

            chest_is_examined = False
            candles_examined = False
            if not altar_examined:
                altar_examined = True
                print_effect(four_candles_1, t_settings)
                time.sleep(1)
                print_effect(four_candles_2, t_settings)
                time.sleep(1)
            while True:
                if break_out_flag:
                    break
                if chest_is_examined:
                    print(f'1) {open_chest}'
                          f'2) {look_at_candles}'
                          f'3) {leave_altar}' + '\n')
                else:
                    print(f'1) {examine_chest}'
                          f'2) {look_at_candles}'
                          f'3) {leave_altar}' + '\n')
                option = input('Введите цифру: ')
                if option == '1':
                    if chest_is_examined:
                        random_wont_open(t_settings, v_p_settings, chest_wont_open)
                        continue
                    else:
                        chest_is_examined = True
                        print_effect(chest_closed_1, t_settings)
                        time.sleep(1)
                        print_effect(chest_closed_2, t_settings)
                        time.sleep(1)
                        continue
                elif option == '2':
                    if papers_combined:
                        if not candles_examined:
                            candles_examined = True
                            print_effect(candles_1, t_settings)
                            time.sleep(1)
                            print_effect(candles_2, t_settings)
                            time.sleep(1)
                            print_effect(candles_examined_1, t_settings)
                            time.sleep(1)
                            print_effect(candles_examined_2, t_settings)
                            time.sleep(1)
                            print_effect(candles_examined_3, t_settings)
                            time.sleep(1)
                        while True:
                            if break_out_flag:
                                break
                            print(f'1) {light_angel}'
                                  f'2) {light_crow}'
                                  f'3) {light_censer}'
                                  f'4) {light_hood}'
                                  f'5) {read_riddle}'
                                  f'6) {leave_candles}' + '\n')
                            option = input('Введите цифру или комбинацию цифр: ')
                            if option == '100':
                                quit_menu(t_settings, v_a_settings)
                                continue
                            elif option == '0':
                                if v_a_settings:
                                    continue
                                else:
                                    print('Озвучивание опций отключено')
                                    continue
                            elif option == '5':
                                print_effect(riddle_strings[0], t_settings)
                                print_effect(riddle_strings[1], t_settings)
                                print_effect(riddle_strings[2], t_settings)
                                print_effect(riddle_strings[3], t_settings)
                                print('')
                                print_effect(riddle_strings[4], t_settings)
                                print_effect(riddle_strings[5], t_settings)
                                print_effect(riddle_strings[6], t_settings)
                                print_effect(riddle_strings[7], t_settings)
                                print('')
                                print_effect(riddle_strings[8], t_settings)
                                print_effect(riddle_strings[9], t_settings)
                                print_effect(riddle_strings[10], t_settings)
                                print_effect(riddle_strings[11], t_settings)
                                print('')
                                print_effect(riddle_strings[12], t_settings)
                                print_effect(riddle_strings[13], t_settings)
                                print_effect(riddle_strings[14], t_settings)
                                print_effect(riddle_strings[15], t_settings)
                                print('')
                                time.sleep(1)
                                continue
                            elif option == '6':
                                break
                            elif option == '3241':
                                break_out_flag = True
                                print(chest_unlocked)
                                print_effect(riddle_solved_1, t_settings)
                                time.sleep(1)
                                print_effect(riddle_solved_2, t_settings)
                                time.sleep(1)
                            else:
                                if numbers_check(option):
                                    tries_number += 1
                                    if tries_number == 1:
                                        print_effect(first_failure, t_settings)
                                        time.sleep(1)
                                        continue
                                    else:
                                        if tries_number < 3:
                                            random_failure(t_settings, v_p_settings, failures)
                                            continue
                                        else:

                                            """смерть от дротика"""
                                            while True:
                                                print(dart_whoosh)
                                                # room_1_mp3.stop() if m_settings else None
                                                # sound_effect('sound/sound_effects/death.wav', s_settings)
                                                # time.sleep(1) if s_settings else None
                                                # dd_mp3.set_volume(0.2) if m_settings else None
                                                # dd_mp3.play(-1) if m_settings else None
                                                # sound_effect('sound/voice_person/room_1/14_painful_death.wav',
                                                #              v_p_settings)
                                                print_effect(death_1, t_settings)
                                                # time.sleep(10) if not t_settings and v_p_settings else None
                                                time.sleep(1)
                                                # sound_effect('sound/voice_person/room_1/15_the_end.wav', v_p_settings)
                                                print_effect(death_2, t_settings)
                                                print('')
                                                # time.sleep(9) if not t_settings and v_p_settings else None
                                                # time.sleep(1)
                                                print(Fore.RED, f'{game_over}')
                                                print(Style.RESET_ALL)
                                                print(death_menu)
                                                print(f'1) {load_game}'
                                                      f'2) {exit_game}' + '\n')
                                                # record = sound_effect('sound/voice_actions/10_death_menu.wav',
                                                #                       v_a_settings)
                                                option = input(f'Введите цифру: ')
                                                # record.stop() if v_a_settings else None
                                                if option == '1':
                                                    # dd_mp3.stop() if m_settings else None
                                                    # room_1_mp3.play(-1) if m_settings else None
                                                    # sound_effect('sound/voice_actions/11_game_resume.wav',
                                                    # v_a_settings)
                                                    print('')
                                                    print(Fore.YELLOW, f'{game_resume}')
                                                    print(Style.RESET_ALL)
                                                    # time.sleep(2.5) if not t_settings and v_a_settings else None
                                                    tries_number = 0
                                                    break
                                                elif option == '2':

                                                    """конец игры"""
                                                    exit()
                                                else:
                                                    print(wrong_input(t_settings, v_a_settings))
                                                    continue
                                else:
                                    continue
                    else:
                        if candles_examined:
                            print_effect(need_to_read, t_settings)
                            time.sleep(1)
                            continue
                        else:
                            candles_examined = True
                            print_effect(candles_1, t_settings)
                            time.sleep(1)
                            print_effect(candles_2, t_settings)
                            time.sleep(1)
                            print_effect(need_to_read, t_settings)
                            time.sleep(1)
                            continue
                elif option == '3':
                    break
                else:
                    print(wrong_input(t_settings, v_a_settings))
                    continue
        elif option == '3':

            """читаем отрывки загадки"""
            language_found = 0
            read_count = 0
            while True:
                if papers_combined:
                    break
                if paper_1_read and paper_2_read and paper_3_read:
                    print(f'1) {read_paper_1}'
                          f'2) {read_paper_2}'
                          f'3) {read_paper_3}'
                          f'4) {combine_papers}'
                          f'5) {papers_away}' + '\n')
                else:
                    print(f'1) {read_paper_1}'
                          f'2) {read_paper_2}'
                          f'3) {read_paper_3}'
                          f'4) {papers_away}' + '\n')
                option = input('Введите цифру: ')
                print_effect(reactions[0], t_settings) if \
                    read_count == 0 and option != '4' and option != '5' else None
                if option == '100':
                    quit_menu(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                elif option == '1':
                    if paper_1_read:
                        random_no(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            read_count += 1
                            paper_1_read = True
                            print_effect(string_1, t_settings)
                            print_effect(string_2, t_settings)
                            time.sleep(1)
                            print_effect(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(1) if read_count == 1 else None
                            print_effect(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(1) if read_count == 2 else None
                            print_effect(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(1) if read_count == 3 else None
                            continue
                        else:
                            print_effect(no_light, t_settings)
                            time.sleep(1)
                    continue
                elif option == '2':
                    if paper_2_read:
                        random_no(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            language_found += 1
                            read_count += 1
                            paper_2_read = True
                            print_effect(reactions[7], t_settings) if language_found == 2 else None
                            time.sleep(1) if language_found == 2 else None
                            print_effect(reactions[3], t_settings)
                            time.sleep(1)
                            print_effect(reactions[4], t_settings)
                            time.sleep(1)
                            print_effect(reactions[5], t_settings)
                            time.sleep(1)
                            print_effect(string_3, t_settings)
                            print_effect(string_4, t_settings)
                            time.sleep(1)
                            print_effect(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(1) if read_count == 1 else None
                            print_effect(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(1) if read_count == 2 else None
                            print_effect(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(1) if read_count == 3 else None
                            continue
                        else:
                            print_effect(no_light, t_settings)
                            time.sleep(1)
                elif option == '3':
                    if paper_3_read:
                        random_no(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            language_found += 1
                            read_count += 1
                            paper_3_read = True
                            print_effect(reactions[7], t_settings) if language_found == 2 else None
                            time.sleep(1) if language_found == 2 else None
                            print_effect(reactions[8], t_settings)
                            time.sleep(1)
                            print_effect(reactions[9], t_settings)
                            time.sleep(1)
                            time.sleep(1)
                            print_effect(string_5, t_settings)
                            print_effect(string_6, t_settings)
                            time.sleep(1)
                            print_effect(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(1) if read_count == 1 else None
                            print_effect(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(1) if read_count == 2 else None
                            print_effect(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(1) if read_count == 3 else None
                            continue
                        else:
                            print_effect(no_light, t_settings)
                            time.sleep(1)
                elif option == '4':
                    if paper_1_read and paper_2_read and paper_3_read:
                        papers_combined = True
                        print_effect(reactions[11], t_settings)
                        time.sleep(1)
                        print_effect(reactions[12], t_settings)
                        time.sleep(1)
                        print_effect(riddle_strings[0], t_settings)
                        print_effect(riddle_strings[1], t_settings)
                        print_effect(riddle_strings[2], t_settings)
                        print_effect(riddle_strings[3], t_settings)
                        print('')
                        print_effect(riddle_strings[4], t_settings)
                        print_effect(riddle_strings[5], t_settings)
                        print_effect(riddle_strings[6], t_settings)
                        print_effect(riddle_strings[7], t_settings)
                        print('')
                        print_effect(riddle_strings[8], t_settings)
                        print_effect(riddle_strings[9], t_settings)
                        print_effect(riddle_strings[10], t_settings)
                        print_effect(riddle_strings[11], t_settings)
                        print('')
                        print_effect(riddle_strings[12], t_settings)
                        print_effect(riddle_strings[13], t_settings)
                        print_effect(riddle_strings[14], t_settings)
                        print_effect(riddle_strings[15], t_settings)
                        print('')
                        print_effect(reactions[13], t_settings)
                        time.sleep(1)
                        continue
                    else:
                        break
                elif option == '5':
                    if paper_1_read and paper_2_read and paper_3_read:
                        break
                    else:
                        print(wrong_input(t_settings, v_a_settings))
                        continue
                else:
                    print(wrong_input(t_settings, v_a_settings))
                    continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    papers_read = False
    sack_took = False
    while True:
        if papers_read and sack_took:
            break
        if not chest_opened:
            chest_opened = True
            print_effect(chest_opened, t_settings)
            time.sleep(1)
        print(f'1) {read_papers}'
              f'2) {take_sack}'
              f'3) {close_chest}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            quit_menu(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':
            if papers_read:
                random_no(t_settings, v_p_settings, no_use)
                continue
            else:
                papers_read = True
                print_effect(begin_reading, t_settings)
                print_effect(line_1, t_settings)
                print_effect(line_2 + '\n', t_settings)
                time.sleep(2)
                print_effect(line_3, t_settings)
                print_effect(line_4 + '\n', t_settings)
                time.sleep(2)
                print_effect(need_to_think, t_settings)
                time.sleep(1)
                print_effect(why_religion, t_settings)
                time.sleep(2)
                print_effect(back_to_business, t_settings)
                time.sleep(1)
                continue
        elif option == '2':
            if sack_took:
                random_no(t_settings, v_p_settings, no_use)
                continue
            else:
                sack_took = True
                print_effect(sack_1, t_settings)
                time.sleep(1)
                print_effect(sack_2, t_settings)
                time.sleep(1)
                print_effect(sack_3, t_settings)
                time.sleep(1)
        elif option == '3':
            if papers_read:
                break
            else:
                print_effect(cant_close, t_settings)
                continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    """обнаруживаем тайник"""
    break_indicator = False
    while True:
        if break_indicator:
            break
        print(f'1) {examine_the_table}'
              f'2) {examine_altar}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            quit_menu(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':
            while True:
                if break_indicator:
                    break
                print_effect(mechanism_again, t_settings)
                time.sleep(1)
                print(f'1) {insert_stone}'
                      f'2) {leave_table}' + '\n')
                option = input('Введите цифру: ')
                if option == '100':
                    quit_menu(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                elif option == '1':
                    print_effect(stone_inserted, t_settings)
                    time.sleep(1)
                    print(click)
                    time.sleep(1)
                    print_effect(diamond_correct, t_settings)
                    time.sleep(1)
                    print_effect(great_diamond, t_settings)
                    time.sleep(1)
                    print_effect(follow_the_light, t_settings)
                    time.sleep(1)
                    while True:
                        if break_indicator:
                            break
                        print(f'1) {knock_the_wall}' + '\n')
                        option = input('Введите цифру: ')
                        if option == '100':
                            quit_menu(t_settings, v_a_settings)
                            continue
                        elif option == '0':
                            if v_a_settings:
                                continue
                            else:
                                print('Озвучивание опций отключено')
                                continue
                        elif option == '1':
                            print_effect(storage_found, t_settings)
                            time.sleep(1)
                            while True:
                                print(f'1) {hit_the_wall}' + '\n')
                                option = input('Введите цифру: ')
                                if option == '100':
                                    quit_menu(t_settings, v_a_settings)
                                    continue
                                elif option == '0':
                                    if v_a_settings:
                                        continue
                                    else:
                                        print('Озвучивание опций отключено')
                                        continue
                                elif option == '1':
                                    break_indicator = True
                                    print_effect(storage_opened, t_settings)
                                    time.sleep(1)
                                    print_effect(read_1, t_settings)
                                    time.sleep(1)
                                    print_effect(read_2, t_settings)
                                    time.sleep(1)
                                    break
                        else:
                            print(wrong_input(t_settings, v_a_settings))
                            continue
                elif option == '2':
                    break
                else:
                    print(wrong_input(t_settings, v_a_settings))
                    continue
        elif option == '2':
            random_no(t_settings, v_p_settings, no_use)
            continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    """осматриваем тайник и уходим"""
    book_read = False
    log_read = False
    steroids_taken = False
    leave_point = False
    while True:
        if book_read and log_read:
            leave_point = True
        print(f'1) {examine_storage}'
              f'2) {leave_location}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            quit_menu(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':
            while True:
                if leave_point:
                    return
                print(f'1) {read_book}'
                      f'2) {read_log}'
                      f'3) {take_bundle}' 
                      f'4) {leave_storage}' + '\n')
                # sound_effect('sound/voice_actions/option.wav', v_a_settings)
                # time.sleep(2) if not t_settings and v_a_settings else None
                option = input('Введите цифру: ')
                if option == '100':
                    quit_menu(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                elif option == '1':
                    if book_read:
                        random_no(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        book_read = True
                        print_effect(read_3, t_settings)
                        time.sleep(2)
                        print_effect(book_1, t_settings)
                        print_effect(book_2, t_settings)
                        print_effect(book_3, t_settings)
                        time.sleep(2)
                        print('')
                        print_effect(book_4, t_settings)
                        print_effect(book_5, t_settings)
                        print_effect(book_6, t_settings)
                        print_effect(book_7, t_settings)
                        time.sleep(2)
                        print('')
                        print_effect(book_8, t_settings)
                        print_effect(book_9, t_settings)
                        time.sleep(2)
                        print('')
                        print_effect(book_10, t_settings)
                        print_effect(book_11, t_settings)
                        print_effect(book_12, t_settings)
                        time.sleep(2)
                        print('')
                        print_effect(conclusion, t_settings)
                        time.sleep(1)
                        continue
                elif option == '2':
                    if log_read:
                        random_no(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        log_read = True
                        print_effect(read_log_1, t_settings)
                        time.sleep(1)
                        print_effect(read_log_2, t_settings)
                        time.sleep(2)
                        print('')
                        print_effect(log_1, t_settings)
                        print_effect(log_2, t_settings)
                        print_effect(log_3, t_settings)
                        print_effect(log_4, t_settings)
                        print_effect(log_5, t_settings)
                        print_effect(log_6, t_settings)
                        print_effect(log_7, t_settings)
                        print_effect(log_8, t_settings)
                        print_effect(log_9, t_settings)
                        print_effect(log_10, t_settings)
                        print_effect(log_11, t_settings)
                        print_effect(log_12, t_settings)
                        time.sleep(2)
                        print('')
                        print_effect(much_information, t_settings)
                        time.sleep(1)
                        continue
                elif option == '3':
                    if steroids_taken:
                        random_no(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        steroids_taken = True
                        print_effect(get_steroids_1, t_settings)
                        time.sleep(1)
                        print_effect(get_steroids_2, t_settings)
                        time.sleep(1)
                        print_effect(get_steroids_3, t_settings)
                        time.sleep(1)
                        continue
                elif option == '4':
                    break
                else:
                    print(wrong_input(t_settings, v_a_settings))
                    continue
        elif option == '2':
            if leave_point:
                print_effect(get_tools, t_settings)
                time.sleep(1)
                print_effect(get_away, t_settings)
                time.sleep(1)
                return
            else:
                print_effect(cant_go, t_settings)
                time.sleep(1)
                continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue