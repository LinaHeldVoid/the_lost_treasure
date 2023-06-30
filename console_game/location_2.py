import time
import random

from colorama import Fore, Style

from sound_manager import room_2_mp3, dd_mp3
from scenario_generator import generate_base
from console_game.service_fuctions import print_effect as p_e,sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, numbers_check as n_c


def set_generator(line):
    i = 0
    g = generate_base('../text/3_room_2.txt')
    while i < line:
        next(g)
        i += 1
    return g


def set_generator_1(line):
    i = 0
    g = generate_base('../text/2_room_1.txt')
    while i < line:
        next(g)
        i += 1
    return g


def set_generator_riddle(line):
    i = 0
    g = generate_base('../text/4_riddle.txt')
    while i < line:
        next(g)
        i += 1
    return g


def no_use_generator():
    no_use = []
    i = 0
    g = set_generator(130)
    while i < 5:
        no_use.append(next(g))
        i += 1
    return no_use


def generate_open_shelf():
    open_shelf_again = []
    i = 0
    g = set_generator(27)
    while i < 3:
        open_shelf_again.append(next(g))
        i += 1
    return open_shelf_again


def generate_reactions():
    reactions = []
    g = set_generator(49)
    reactions.append(next(g))
    next(g)
    reactions.append(next(g))
    reactions.append(next(g))
    next(g)
    reactions.append(next(g))
    reactions.append(next(g))
    reactions.append(next(g))
    next(g)
    reactions.append(next(g))
    next(g)
    reactions.append(next(g))
    reactions.append(next(g))
    reactions.append(next(g))
    next(g)
    reactions.append(next(g))
    next(g)
    reactions.append(next(g))
    reactions.append(next(g))
    next(g)
    next(g)
    reactions.append(next(g))
    return reactions


def generate_chest_wont_open():
    chest_wont_open = []
    i = 0
    g = set_generator(107)
    while i < 3:
        chest_wont_open.append(next(g))
        i += 1
    return chest_wont_open


def generate_tries():
    tries = []
    i = 0
    g = set_generator(107)
    while i < 4:
        tries.append(next(g))
        i += 1
    return tries


def generate_failures():
    failures = []
    i = 0
    g = set_generator(116)
    while i < 4:
        failures.append(next(g))
        i += 1
    return failures


def generate_riddle():
    riddle = []
    i = 0
    g = set_generator_riddle(11)
    while i < 4:
        next(g)
        i += 1
        j = 0
        while j < 4:
            riddle.append(next(g))
            j += 1
    return riddle


def random_wont_open(t_settings, v_p_settings, wont_open_list):
    choice = random.choice(wont_open_list)
    if choice == next(set_generator(112)):
        p_e(choice, t_settings)
    elif choice == next(set_generator(113)):
        p_e(choice, t_settings)
    else:
        p_e(choice, t_settings)
    return


def random_try(t_settings, v_p_settings, tries):
    choice = random.choice(tries)
    if choice == next(set_generator(135)):
        p_e(choice, t_settings)
    elif choice == next(set_generator(136)):
        p_e(choice, t_settings)
    elif choice == next(set_generator(137)):
        p_e(choice, t_settings)
    else:
        p_e(choice, t_settings)
    return


def random_failure(t_settings, v_p_settings, failures):
    choice = random.choice(failures)
    if choice == next(set_generator(144)):
        p_e(choice, t_settings)
    elif choice == next(set_generator(145)):
        p_e(choice, t_settings)
    elif choice == next(set_generator(146)):
        p_e(choice, t_settings)
    else:
        p_e(choice, t_settings)
    return


def random_open_shelf(t_settings, v_p_settings, open_shelf_again):
    choose_reaction = random.choice(open_shelf_again)
    p_e(choose_reaction, t_settings)
    return


# рабочий кабинет
def room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    """алгоритм"""
    open_shelf_again = generate_open_shelf()
    reactions = generate_reactions()
    tries = generate_tries()
    failures = generate_failures()
    riddle_strings = generate_riddle()
    no_use = no_use_generator()
    chest_wont_open = generate_chest_wont_open()
    no_light = next(set_generator(60))

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
    tries_number = 0

    g = set_generator(0)
    room_2_mp3.play(-1) if m_settings else None
    s_e('../sound/voice_actions/room_2/0.wav', v_a_settings)
    print(next(g))
    time.sleep(2) if not t_settings and v_p_settings else None
    time.sleep(1)
    s_e('../sound/voice_person/room_2/1.wav', v_a_settings)
    p_e(next(g), t_settings)
    time.sleep(11) if not t_settings and v_p_settings else None
    time.sleep(1)
    s_e('../sound/voice_person/room_2/2.wav', v_a_settings)
    p_e(next(g), t_settings)
    time.sleep(11) if not t_settings and v_p_settings else None
    time.sleep(1)

    """главное меню"""
    while True:
        if break_out_flag:
            break

        if open_1 and open_2 and open_3:
            if papers_combined:
                g = set_generator(4)
                print(f'1) {next(g)}'
                      f'2) {next(g)}' + '\n')
                s_e('../sound/voice_actions/option.wav', v_a_settings)
                time.sleep(2) if not t_settings and v_a_settings else None
                record = s_e('../sound/voice_actions/room_2/4. menu.wav', v_a_settings)
            else:
                g = set_generator(7)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
                s_e('../sound/voice_actions/option.wav', v_a_settings)
                time.sleep(2) if not t_settings and v_a_settings else None
                record = s_e('../sound/voice_actions/room_2/7. menu.wav', v_a_settings)
        else:
            g = set_generator(4)
            print(f'1) {next(g)}'
                  f'2) {next(g)}' + '\n')
            s_e('../sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            record = s_e('../sound/voice_actions/room_2/4. menu.wav', v_a_settings)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None
        s_e('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        if option == '100':
            q(t_settings, v_a_settings)
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
                g = set_generator(12)
                table_is_examined = True
                s_e('../sound/voice_person/room_2/12.wav', v_a_settings)
                p_e(next(g), t_settings)
                time.sleep(11) if not t_settings and v_p_settings else None
                time.sleep(1)
                s_e('../sound/voice_person/room_2/13.wav', v_a_settings)
                p_e(next(g), t_settings)
                time.sleep(4) if not t_settings and v_p_settings else None
                time.sleep(1)
            while True:

                """проверяем полки"""
                if open_1 and open_2 and open_3 and mechanism_is_examined:
                    g = set_generator(37)
                    s_e('../sound/voice_person/room_2/2.wav', v_a_settings)
                    p_e(next(g), t_settings)
                    time.sleep(3) if not t_settings and v_p_settings else None
                    time.sleep(1)
                    break
                else:
                    if light_on:
                        g = set_generator(15)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}' + '\n')
                        s_e('../sound/voice_actions/option.wav', v_a_settings)
                        time.sleep(2) if not t_settings and v_a_settings else None
                        record = s_e('../sound/voice_actions/room_2/15. menu.wav', v_a_settings)
                    else:
                        g = set_generator(21)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}'
                              f'6) {next(g)}' + '\n')
                        s_e('../sound/voice_actions/option.wav', v_a_settings)
                        time.sleep(2) if not t_settings and v_a_settings else None
                        record = s_e('../sound/voice_actions/room_2/21. menu.wav', v_a_settings)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None
                    if option == '100':
                        q(t_settings, v_a_settings)
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
                            g = set_generator(29)
                            open_1 = True
                            s_e('../sound/voice_person/room_2/29.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(6) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '2':
                        if open_2:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            time.sleep(1)
                            continue
                        else:
                            g = set_generator(32)
                            open_2 = True
                            s_e('../sound/voice_person/room_2/32.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(8) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            s_e('../sound/voice_person/room_2/33.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(4) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '3':
                        if open_3:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            time.sleep(1)
                            continue
                        else:
                            g = set_generator(36)
                            open_3 = True
                            s_e('../sound/voice_person/room_2/36.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(8) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '4':
                        if mechanism_is_examined:
                            r_n(t_settings, v_p_settings, no_use)
                            time.sleep(1)
                            continue
                        else:
                            if light_on is True:
                                g = set_generator(63)
                                mechanism_is_examined = True
                                s_e('../sound/voice_person/room_2/63.wav', v_a_settings)
                                p_e(next(g), t_settings)
                                time.sleep(10) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                s_e('../sound/voice_person/room_2/64.wav', v_a_settings)
                                p_e(next(g), t_settings)
                                time.sleep(9) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                continue
                            else:
                                p_e(no_light, t_settings)
                                time.sleep(1)
                                continue
                    elif option == '5':
                        if light_on:
                            break
                        else:
                            g = set_generator(56)
                            light_on = True
                            s_e('../sound/sound_effects/flint.wav', v_a_settings)
                            print(next(g), t_settings)
                            time.sleep(1.5) if s_settings else None
                            time.sleep(1)
                            s_e('../sound/voice_person/room_2/33.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(2) if not t_settings and v_p_settings else None
                            time.sleep(1)
                    elif option == '6':
                        if not light_on:
                            break
                        else:
                            print(w(t_settings, v_a_settings))
                            continue
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
        elif option == '2':
            if break_out_flag:
                break

            chest_is_examined = False
            candles_examined = False
            if not altar_examined:
                altar_examined = True
                g = set_generator(96)
                s_e('../sound/voice_person/room_2/96.wav', v_a_settings)
                p_e(next(g), t_settings)
                time.sleep(9) if not t_settings and v_p_settings else None
                time.sleep(1)
                s_e('../sound/voice_person/room_2/97.wav', v_a_settings)
                p_e(next(g), t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                time.sleep(1)
            while True:
                if break_out_flag:
                    break
                if chest_is_examined:
                    g = set_generator(103)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' + '\n')
                    s_e('../sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    record = s_e('../sound/voice_actions/room_2/103. menu.wav', v_a_settings)
                else:
                    g = set_generator(107)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' + '\n')
                    s_e('../sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    record = s_e('../sound/voice_actions/room_2/107. menu.wav', v_a_settings)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None
                if option == '1':
                    if chest_is_examined:
                        random_wont_open(t_settings, v_p_settings, chest_wont_open)
                        continue
                    else:
                        g = set_generator(100)
                        chest_is_examined = True
                        s_e('../sound/voice_person/room_2/100.wav', v_a_settings)
                        p_e(next(g), t_settings)
                        time.sleep(2) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        s_e('../sound/voice_person/room_2/101.wav', v_a_settings)
                        p_e(next(g), t_settings)
                        time.sleep(3) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        continue
                elif option == '2':
                    if papers_combined:
                        if not candles_examined:
                            g = set_generator(117)
                            candles_examined = True
                            s_e('../sound/voice_person/room_2/117.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(5) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            s_e('../sound/voice_person/room_2/118.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(3) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            next(g)
                            next(g)
                            s_e('../sound/voice_person/room_2/121.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(6) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            s_e('../sound/voice_person/room_2/123.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(5) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            s_e('../sound/voice_person/room_2/124.wav', v_a_settings)
                            p_e(next(g), t_settings)
                            time.sleep(12) if not t_settings and v_p_settings else None
                            time.sleep(1)
                        while True:
                            if break_out_flag:
                                break
                            g = set_generator(127)
                            print(f'1) {next(g)}'
                                  f'2) {next(g)}'
                                  f'3) {next(g)}'
                                  f'4) {next(g)}'
                                  f'5) {next(g)}'
                                  f'6) {next(g)}' + '\n')
                            s_e('../sound/voice_actions/option.wav', v_a_settings)
                            time.sleep(2) if not t_settings and v_a_settings else None
                            record = s_e('../sound/voice_actions/room_2/127. menu.wav', v_a_settings)
                            option = input('Введите цифру или комбинацию цифр: ')
                            record.stop() if v_a_settings else None
                            if option == '100':
                                q(t_settings, v_a_settings)
                                continue
                            elif option == '0':
                                if v_a_settings:
                                    continue
                                else:
                                    print('Озвучивание опций отключено')
                                    continue
                            elif option == '5':
                                p_e(riddle_strings[0], t_settings)
                                p_e(riddle_strings[1], t_settings)
                                p_e(riddle_strings[2], t_settings)
                                p_e(riddle_strings[3], t_settings)
                                print('')
                                p_e(riddle_strings[4], t_settings)
                                p_e(riddle_strings[5], t_settings)
                                p_e(riddle_strings[6], t_settings)
                                p_e(riddle_strings[7], t_settings)
                                print('')
                                p_e(riddle_strings[8], t_settings)
                                p_e(riddle_strings[9], t_settings)
                                p_e(riddle_strings[10], t_settings)
                                p_e(riddle_strings[11], t_settings)
                                print('')
                                p_e(riddle_strings[12], t_settings)
                                p_e(riddle_strings[13], t_settings)
                                p_e(riddle_strings[14], t_settings)
                                p_e(riddle_strings[15], t_settings)
                                print('')
                                s_e('../sound/voice_person/room_2/Riddle.wav', v_a_settings)
                                p_e(next(g), t_settings)
                                time.sleep(39) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                continue
                            elif option == '6':
                                break
                            elif option == '3241':
                                g = set_generator(155)
                                break_out_flag = True
                                s_e('../sound/sound_effects/key.wav', v_a_settings)
                                print(next(g), t_settings)
                                time.sleep(1) if s_settings else None
                                time.sleep(1)
                                s_e('../sound/voice_person/room_2/156.wav', v_a_settings)
                                p_e(next(g), t_settings)
                                time.sleep(4) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                s_e('../sound/voice_person/room_2/157', v_a_settings)
                                p_e(next(g), t_settings)
                                time.sleep(6) if not t_settings and v_p_settings else None
                                time.sleep(1)
                            else:
                                if n_c(option):
                                    tries_number += 1
                                    if tries_number == 1:
                                        g = set_generator(135)
                                        s_e('../sound/voice_person/room_2/135.wav', v_a_settings)
                                        p_e(next(g), t_settings)
                                        time.sleep(2) if not t_settings and v_p_settings else None
                                        time.sleep(1)
                                        continue
                                    else:
                                        if tries_number < 3:
                                            random_failure(t_settings, v_p_settings, failures)
                                            continue
                                        else:

                                            """смерть от дротика"""
                                            while True:
                                                g = set_generator(150)
                                                print(next(g))
                                                room_2_mp3.stop() if m_settings else None
                                                s_e('../sound/sound_effects/death.wav', s_settings)
                                                time.sleep(1) if s_settings else None
                                                dd_mp3.set_volume(0.2) if m_settings else None
                                                dd_mp3.play(-1) if m_settings else None
                                                s_e('../sound/voice_person/room_2/151.wav', v_p_settings)
                                                p_e(next(g), t_settings)
                                                time.sleep(10) if not t_settings and v_p_settings else None
                                                time.sleep(1)
                                                s_e('../sound/voice_person/room_2/152.wav', v_p_settings)
                                                p_e(next(g), t_settings)
                                                print('')
                                                time.sleep(5) if not t_settings and v_p_settings else None
                                                time.sleep(1)
                                                g = set_generator_1(32)
                                                print(Fore.RED, f'{next(g)}')
                                                print(Style.RESET_ALL)
                                                print(next(g))
                                                next(g)
                                                print(f'1) {next(g)}'
                                                      f'2) {next(g)}' + '\n')
                                                record = s_e('../sound/voice_actions/10_death_menu.wav',
                                                             v_a_settings)
                                                option = input(f'Введите цифру: ')
                                                record.stop() if v_a_settings else None
                                                if option == '1':
                                                    dd_mp3.stop() if m_settings else None
                                                    room_2_mp3.play(-1) if m_settings else None
                                                    s_e('../sound/voice_actions/11_game_resume.wav', v_a_settings)
                                                    print('')
                                                    next(g)
                                                    next(g)
                                                    print(Fore.YELLOW, f'{next(g)}')
                                                    print(Style.RESET_ALL)
                                                    time.sleep(2.5) if not t_settings and v_a_settings else None
                                                    break
                                                elif option == '2':

                                                    """конец игры"""
                                                    exit()
                                                else:
                                                    print(w(t_settings, v_a_settings))
                                                    continue
                                else:
                                    continue
                    else:
                        if candles_examined:
                            g = set_generator(121)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            continue
                        else:
                            g = set_generator(123)
                            candles_examined = True
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            continue
                elif option == '3':
                    break
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        elif option == '3':

            """читаем отрывки загадки"""
            language_found = 0
            read_count = 0
            while True:
                if papers_combined:
                    break
                if paper_1_read and paper_2_read and paper_3_read:
                    g = set_generator(44)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}'
                          f'4) {next(g)}'
                          f'5) {next(g)}' + '\n')
                else:
                    g = set_generator(50)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}'
                          f'4) {next(g)}' + '\n')
                option = input('Введите цифру: ')
                p_e(reactions[0], t_settings) if \
                    read_count == 0 and option != '4' and option != '5' else None
                if option == '100':
                    q(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                elif option == '1':
                    if paper_1_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            read_count += 1
                            paper_1_read = True
                            g = set_generator_riddle(1)
                            p_e(next(g), t_settings)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            p_e(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(1) if read_count == 1 else None
                            p_e(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(1) if read_count == 2 else None
                            p_e(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(1) if read_count == 3 else None
                            continue
                        else:
                            p_e(no_light, t_settings)
                            time.sleep(1)
                    continue
                elif option == '2':
                    if paper_2_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            language_found += 1
                            read_count += 1
                            paper_2_read = True
                            g = set_generator_riddle(5)
                            p_e(reactions[7], t_settings) if language_found == 2 else None
                            time.sleep(1) if language_found == 2 else None
                            p_e(reactions[3], t_settings)
                            time.sleep(1)
                            p_e(reactions[4], t_settings)
                            time.sleep(1)
                            p_e(reactions[5], t_settings)
                            time.sleep(1)
                            p_e(next(g), t_settings)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            p_e(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(1) if read_count == 1 else None
                            p_e(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(1) if read_count == 2 else None
                            p_e(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(1) if read_count == 3 else None
                            continue
                        else:
                            p_e(no_light, t_settings)
                            time.sleep(1)
                elif option == '3':
                    if paper_3_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            language_found += 1
                            read_count += 1
                            paper_3_read = True
                            g = set_generator_riddle(9)
                            p_e(reactions[7], t_settings) if language_found == 2 else None
                            time.sleep(1) if language_found == 2 else None
                            p_e(reactions[8], t_settings)
                            time.sleep(1)
                            p_e(reactions[9], t_settings)
                            time.sleep(1)
                            time.sleep(1)
                            p_e(next(g), t_settings)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            p_e(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(1) if read_count == 1 else None
                            p_e(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(1) if read_count == 2 else None
                            p_e(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(1) if read_count == 3 else None
                            continue
                        else:
                            p_e(no_light, t_settings)
                            time.sleep(1)
                elif option == '4':
                    if paper_1_read and paper_2_read and paper_3_read:
                        papers_combined = True
                        p_e(reactions[11], t_settings)
                        time.sleep(1)
                        p_e(reactions[12], t_settings)
                        time.sleep(1)
                        p_e(riddle_strings[0], t_settings)
                        p_e(riddle_strings[1], t_settings)
                        p_e(riddle_strings[2], t_settings)
                        p_e(riddle_strings[3], t_settings)
                        print('')
                        p_e(riddle_strings[4], t_settings)
                        p_e(riddle_strings[5], t_settings)
                        p_e(riddle_strings[6], t_settings)
                        p_e(riddle_strings[7], t_settings)
                        print('')
                        p_e(riddle_strings[8], t_settings)
                        p_e(riddle_strings[9], t_settings)
                        p_e(riddle_strings[10], t_settings)
                        p_e(riddle_strings[11], t_settings)
                        print('')
                        p_e(riddle_strings[12], t_settings)
                        p_e(riddle_strings[13], t_settings)
                        p_e(riddle_strings[14], t_settings)
                        p_e(riddle_strings[15], t_settings)
                        print('')
                        p_e(reactions[13], t_settings)
                        time.sleep(1)
                        continue
                    else:
                        break
                elif option == '5':
                    if paper_1_read and paper_2_read and paper_3_read:
                        break
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        else:
            print(w(t_settings, v_a_settings))
            continue

    """изучаем содержимое шкатулки"""
    papers_read = False
    sack_took = False
    while True:
        if papers_read and sack_took:
            break
        if not chest_opened:
            chest_opened = True
            p_e(chest_opened, t_settings)
            time.sleep(1)
        g = set_generator(162)
        print(f'1) {next(g)}'
              f'2) {next(g)}'
              f'3) {next(g)}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            q(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':
            if papers_read:
                r_n(t_settings, v_p_settings, no_use)
                continue
            else:
                papers_read = True
                g = set_generator(167)
                s_e('../sound/voice_person/room_2/167.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(2) if not t_settings and v_p_settings else None
                time.sleep(2)
                next(g)
                s_e('../sound/voice_person/room_2/169.wav', v_p_settings)
                p_e(next(g), t_settings)
                p_e(next(g) + '\n', t_settings)
                time.sleep(8) if not t_settings and v_p_settings else None
                time.sleep(2)
                next(g)
                s_e('../sound/voice_person/room_2/173.wav', v_p_settings)
                p_e(next(g), t_settings)
                p_e(next(g) + '\n', t_settings)
                time.sleep(8) if not t_settings and v_p_settings else None
                time.sleep(2)
                next(g)
                s_e('../sound/voice_person/room_2/175.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(7) if not t_settings and v_p_settings else None
                time.sleep(1)
                s_e('../sound/voice_person/room_2/176.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(12) if not t_settings and v_p_settings else None
                time.sleep(2)
                s_e('../sound/voice_person/room_2/177.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(2) if not t_settings and v_p_settings else None
                time.sleep(1)
                continue
        elif option == '2':
            if sack_took:
                r_n(t_settings, v_p_settings, no_use)
                continue
            else:
                sack_took = True
                g = set_generator(180)
                s_e('../sound/voice_person/room_2/180.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(10) if not t_settings and v_p_settings else None
                time.sleep(1)
                s_e('../sound/voice_person/room_2/181.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                time.sleep(1)
                s_e('../sound/voice_person/room_2/182.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(11) if not t_settings and v_p_settings else None
                time.sleep(1)
        elif option == '3':
            if papers_read:
                break
            else:
                g = set_generator(185)
                s_e('../sound/voice_person/room_2/185.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(6) if not t_settings and v_p_settings else None
                continue
        else:
            print(w(t_settings, v_a_settings))
            continue

    """обнаруживаем тайник"""
    break_indicator = False
    while True:
        if break_indicator:
            break
        g = set_generator(187)
        print(f'1) {next(g)}'
              f'2) {next(g)}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            q(t_settings, v_a_settings)
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
                g = set_generator(191)
                p_e(next(g), t_settings)
                time.sleep(1)
                print(f'1) {next(g)}'
                      f'2) {next(g)}' + '\n')
                option = input('Введите цифру: ')
                if option == '100':
                    q(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                elif option == '1':
                    g = set_generator(197)
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
                    while True:
                        if break_indicator:
                            break
                        g = set_generator(203)
                        print(f'1) {next(g)}' + '\n')
                        option = input('Введите цифру: ')
                        if option == '100':
                            q(t_settings, v_a_settings)
                            continue
                        elif option == '0':
                            if v_a_settings:
                                continue
                            else:
                                print('Озвучивание опций отключено')
                                continue
                        elif option == '1':
                            g = set_generator(204)
                            p_e(next(g), t_settings)
                            time.sleep(1)
                            while True:
                                s = set_generator(206)
                                print(f'1) {next(g)}' + '\n')
                                option = input('Введите цифру: ')
                                if option == '100':
                                    q(t_settings, v_a_settings)
                                    continue
                                elif option == '0':
                                    if v_a_settings:
                                        continue
                                    else:
                                        print('Озвучивание опций отключено')
                                        continue
                                elif option == '1':
                                    g = set_generator(207)
                                    break_indicator = True
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                    p_e(next(g), t_settings)
                                    time.sleep(1)
                                    break
                        else:
                            print(w(t_settings, v_a_settings))
                            continue
                elif option == '2':
                    break
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        elif option == '2':
            r_n(t_settings, v_p_settings, no_use)
            continue
        else:
            print(w(t_settings, v_a_settings))
            continue

    """осматриваем тайник и уходим"""
    book_read = False
    log_read = False
    steroids_taken = False
    leave_point = False
    while True:
        if book_read and log_read:
            leave_point = True
        g = set_generator(211)
        print(f'1) {next(g)}'
              f'2) {next(g)}' + '\n')
        option = input('Введите цифру: ')
        if option == '100':
            q(t_settings, v_a_settings)
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
                g = set_generator(214)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' 
                      f'4) {next(g)}' + '\n')
                # sound_effect('sound/voice_actions/option.wav', v_a_settings)
                # time.sleep(2) if not t_settings and v_a_settings else None
                option = input('Введите цифру: ')
                if option == '100':
                    q(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                elif option == '1':
                    if book_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        g = set_generator(220)
                        book_read = True
                        p_e(next(g), t_settings)
                        next(g)
                        time.sleep(2)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        next(g)
                        time.sleep(2)
                        print('')
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        time.sleep(2)
                        print('')
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        next(g)
                        time.sleep(2)
                        print('')
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        next(g)
                        time.sleep(2)
                        print('')
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        continue
                elif option == '2':
                    if log_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        log_read = True
                        g = set_generator(242)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        p_e(next(g), t_settings)
                        time.sleep(2)
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
                        next(g)
                        time.sleep(2)
                        print('')
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        continue
                elif option == '3':
                    if steroids_taken:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        g = set_generator(261)
                        steroids_taken = True
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        p_e(next(g), t_settings)
                        time.sleep(1)
                        continue
                elif option == '4':
                    break
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        elif option == '2':
            if leave_point:
                g = set_generator(265)
                p_e(next(g), t_settings)
                time.sleep(1)
                p_e(next(g), t_settings)
                time.sleep(1)
                return
            else:
                g = set_generator(267)
                p_e(next(g), t_settings)
                time.sleep(1)
                continue
        else:
            print(w(t_settings, v_a_settings))
            continue