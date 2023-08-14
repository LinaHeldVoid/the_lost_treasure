import time
import random

from sound_manager import room_2_mp3, dd_mp3
from scenario_generator import generate_base
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, numbers_check as n_c, determination_announcement as d_a, \
    new_determination, death_menu, print_help, random_revival


def set_generator(line):
    i = 0
    g = generate_base('text/3_room_2.txt')
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


def set_generator_riddle(line):
    i = 0
    g = generate_base('text/4_riddle.txt')
    while i < line:
        next(g)
        i += 1
    return g


def no_use_generator():
    no_use = []
    i = 0
    k = set_generator(275)
    while i < 5:
        no_use.append(next(k))
        i += 1
    return no_use


def generate_open_shelf():
    open_shelf_again = []
    i = 0
    k = set_generator(40)
    while i < 3:
        open_shelf_again.append(next(k))
        i += 1
    return open_shelf_again


def generate_reactions():
    reactions = []
    k = set_generator(67)
    reactions.append(next(k))
    next(k)
    reactions.append(next(k))
    reactions.append(next(k))
    next(k)
    next(k)
    reactions.append(next(k))
    reactions.append(next(k))
    reactions.append(next(k))
    next(k)
    reactions.append(next(k))
    next(k)
    next(k)
    reactions.append(next(k))
    reactions.append(next(k))
    reactions.append(next(k))
    next(k)
    reactions.append(next(k))
    next(k)
    next(k)
    reactions.append(next(k))
    reactions.append(next(k))
    next(k)
    next(k)
    reactions.append(next(k))
    return reactions


def generate_chest_wont_open():
    chest_wont_open = []
    i = 0
    k = set_generator(112)
    while i < 3:
        chest_wont_open.append(next(k))
        i += 1
    return chest_wont_open


def generate_tries():
    tries = []
    i = 0
    k = set_generator(135)
    while i < 4:
        tries.append(next(k))
        i += 1
    return tries


def generate_failures():
    failures = []
    i = 0
    k = set_generator(144)
    while i < 4:
        failures.append(next(k))
        i += 1
    return failures


def generate_riddle():
    riddle = []
    i = 0
    k = set_generator_riddle(11)
    while i < 4:
        next(k)
        i += 1
        j = 0
        while j < 4:
            riddle.append(next(k))
            j += 1
    return riddle


def random_wont_open(t_settings, v_p_settings, wont_open_list):
    choice = random.choice(wont_open_list)
    if choice == next(set_generator(112)):
        s_e('sound/voice_person/room_2/112.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(1) if not t_settings and v_p_settings else None
        time.sleep(1)
    elif choice == next(set_generator(113)):
        s_e('sound/voice_person/room_2/113.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(1) if not t_settings and v_p_settings else None
        time.sleep(1)
    else:
        s_e('sound/voice_person/room_2/114.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(1) if not t_settings and v_p_settings else None
        time.sleep(1)
    return


def random_try(t_settings, v_p_settings, tries):
    choice = random.choice(tries)
    if choice == next(set_generator(135)):
        s_e('sound/voice_person/room_2/135.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
        time.sleep(1)
    elif choice == next(set_generator(136)):
        s_e('sound/voice_person/room_2/136.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
        time.sleep(1)
    elif choice == next(set_generator(137)):
        s_e('sound/voice_person/room_2/137.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(1) if not t_settings and v_p_settings else None
        time.sleep(1)
    else:
        s_e('sound/voice_person/room_2/138.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
        time.sleep(1)
    return


def random_failure(t_settings, v_p_settings, failures):
    choice = random.choice(failures)
    if choice == next(set_generator(144)):
        s_e('sound/voice_person/room_2/144.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    elif choice == next(set_generator(145)):
        s_e('sound/voice_person/room_2/145.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    elif choice == next(set_generator(146)):
        s_e('sound/voice_person/room_2/146.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    else:
        s_e('sound/voice_person/room_2/147.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    return


def random_open_shelf(t_settings, v_p_settings, open_shelf_again):
    choice = random.choice(open_shelf_again)
    if choice == next(set_generator(40)):
        s_e('sound/voice_person/room_2/40.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    elif choice == next(set_generator(41)):
        s_e('sound/voice_person/room_2/41.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(6) if not t_settings and v_p_settings else None
    else:
        s_e('sound/voice_person/room_2/42.ogg', v_p_settings, 2)
        p_e(choice, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    return


# рабочий кабинет
def room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination):

    """алгоритм"""
    open_shelf_again = generate_open_shelf()
    reactions = generate_reactions()
    tries = generate_tries()
    failures = generate_failures()
    riddle_strings = generate_riddle()
    no_use = no_use_generator()
    chest_wont_open = generate_chest_wont_open()
    no_light = next(set_generator(60))
    final_data = {}

    break_out_flag = False
    altar_examined = False
    chest_opened = False
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
    chest_is_examined = False
    candles_examined = False
    candle_look_count = 0
    tries_number = 0

    g = set_generator(0)
    room_2_mp3.set_volume(0.1)
    room_2_mp3.play(-1) if m_settings else None
    s_e('sound/voice_actions/room_2/0.ogg', v_a_settings, 1)
    print(next(g))
    time.sleep(3) if not t_settings and v_p_settings else None
    s_e('sound/voice_person/room_2/1.ogg', v_p_settings, 2)
    p_e(next(g), t_settings)
    time.sleep(11) if not t_settings and v_p_settings else None
    s_e('sound/voice_person/room_2/2.ogg', v_p_settings, 2)
    p_e(next(g), t_settings)
    time.sleep(3) if not t_settings and v_p_settings else None

    """главное меню"""
    while True:
        if break_out_flag:
            break

        if open_1 and open_2 and open_3:
            if papers_combined:
                g = set_generator(4)
                print(f'1) {next(g)}'
                      f'2) {next(g)}' + '\n')
                s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                time.sleep(2) if v_a_settings else None
                record = s_e('sound/voice_actions/room_2/4. menu.ogg', v_a_settings, 1)
            else:
                g = set_generator(7)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
                s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                time.sleep(2) if v_a_settings else None
                record = s_e('sound/voice_actions/room_2/7. menu.ogg', v_a_settings, 1)
        else:
            g = set_generator(4)
            print(f'1) {next(g)}'
                  f'2) {next(g)}' + '\n')
            s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
            time.sleep(2) if v_a_settings else None
            record = s_e('sound/voice_actions/room_2/4. menu.ogg', v_a_settings, 1)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None
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

            """осматриваем стол"""
            if not table_is_examined:
                g = set_generator(12)
                table_is_examined = True
                s_e('sound/voice_person/room_2/12.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(12) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/13.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(5) if not t_settings and v_p_settings else None

            while True:

                """проверяем полки"""
                if open_1 and open_2 and open_3 and mechanism_is_examined:
                    r_n(t_settings, v_p_settings, no_use)
                    break
                else:
                    if light_on:
                        g = set_generator(15)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}' + '\n')
                        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                        time.sleep(2) if v_a_settings else None
                        record = s_e('sound/voice_actions/room_2/15. menu.ogg', v_a_settings, 1)
                    else:
                        g = set_generator(21)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}'
                              f'6) {next(g)}' + '\n')
                        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                        time.sleep(2) if v_a_settings else None
                        record = s_e('sound/voice_actions/room_2/21. menu.ogg', v_a_settings, 1)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None
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
                        if open_1:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            continue
                        else:
                            g = set_generator(29)
                            open_1 = True
                            s_e('sound/voice_person/room_2/29.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(7) if not t_settings and v_p_settings else None
                            continue
                    elif option == '2':
                        if open_2:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            continue
                        else:
                            g = set_generator(32)
                            open_2 = True
                            s_e('sound/voice_person/room_2/32.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(9) if not t_settings and v_p_settings else None
                            s_e('sound/voice_person/room_2/33.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(5) if not t_settings and v_p_settings else None
                            continue
                    elif option == '3':
                        if open_3:
                            random_open_shelf(t_settings, v_p_settings, open_shelf_again)
                            continue
                        else:
                            g = set_generator(36)
                            open_3 = True
                            s_e('sound/voice_person/room_2/36.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(9) if not t_settings and v_p_settings else None
                            continue
                    elif option == '4':
                        if mechanism_is_examined:
                            r_n(t_settings, v_p_settings, no_use)
                            continue
                        else:
                            if light_on is True:
                                g = set_generator(63)
                                mechanism_is_examined = True
                                s_e('sound/voice_person/room_2/63.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(11) if not t_settings and v_p_settings else None
                                s_e('sound/voice_person/room_2/64.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(10) if not t_settings and v_p_settings else None
                                continue
                            else:
                                p_e(no_light, t_settings)
                                continue
                    elif option == '5':
                        if light_on:
                            break
                        else:
                            g = set_generator(56)
                            light_on = True
                            s_e('sound/sound_effects/flint.ogg', s_settings, 2)
                            print(next(g))
                            time.sleep(2.5) if s_settings else None
                            s_e('sound/voice_person/room_2/57.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(3) if not t_settings and v_p_settings else None
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

            if not altar_examined:
                altar_examined = True
                g = set_generator(96)
                s_e('sound/voice_person/room_2/96.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(10) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/97.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(4) if not t_settings and v_p_settings else None
            while True:
                if break_out_flag:
                    break
                if chest_is_examined:
                    g = set_generator(103)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' + '\n')
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_2/103. menu.ogg', v_a_settings, 1)
                else:
                    g = set_generator(107)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' + '\n')
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_2/107. menu.ogg', v_a_settings, 1)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None
                if option == '1':
                    if chest_is_examined:
                        random_wont_open(t_settings, v_p_settings, chest_wont_open)
                        continue
                    else:
                        g = set_generator(100)
                        chest_is_examined = True
                        s_e('sound/voice_person/room_2/100.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(3) if not t_settings and v_p_settings else None
                        s_e('sound/voice_person/room_2/101.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(5) if not t_settings and v_p_settings else None
                        continue
                elif option == '2':
                    candle_look_count += 1
                    if candle_look_count == 1:
                        g = set_generator(117)
                        s_e('sound/voice_person/room_2/117.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(6) if not t_settings and v_p_settings else None
                        s_e('sound/voice_person/room_2/118.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(14) if not t_settings and v_p_settings else None
                    if papers_combined:
                        if not candles_examined:
                            g = set_generator(123)
                            candles_examined = True
                            s_e('sound/voice_person/room_2/123.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(6) if not t_settings and v_p_settings else None
                            s_e('sound/voice_person/room_2/124.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(13) if not t_settings and v_p_settings else None
                            s_e('sound/voice_person/room_2/125.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(7) if not t_settings and v_p_settings else None
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
                            s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                            time.sleep(2) if v_a_settings else None
                            record = s_e('sound/voice_actions/room_2/127. menu.ogg', v_a_settings, 1)
                            option = input('Введите цифру или комбинацию цифр: ')
                            record.stop() if v_a_settings else None
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
                            elif option == '5':
                                s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                                time.sleep(2) if s_settings else None
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
                                s_e('sound/voice_person/room_2/Riddle.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(40) if not t_settings and v_p_settings else None
                                s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                                time.sleep(3) if s_settings else None
                                continue
                            elif option == '6':
                                break
                            elif option == '3241':

                                g = set_generator(155)
                                break_out_flag = True
                                print(next(g))
                                s_e('sound/sound_effects/key.ogg', s_settings, 2)
                                time.sleep(3) if s_settings else None
                                time.sleep(2.5) if s_settings else None
                                s_e('sound/voice_person/room_2/156.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(5) if not t_settings and v_p_settings else None

                                # награждаем игрока за быстрое решение
                                if tries_number == 0:
                                    determination = new_determination(t_settings, v_p_settings,
                                                                      v_a_settings, m_settings,
                                                                      s_settings, determination, 3, '+')
                                elif tries_number == 1:
                                    determination = new_determination(t_settings, v_p_settings,
                                                                      v_a_settings, m_settings,
                                                                      s_settings, determination, 1, '+')

                                s_e('sound/voice_person/room_2/157.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(7) if not t_settings and v_p_settings else None
                            else:
                                if n_c(option):
                                    s_e('sound/sound_effects/flint.ogg', v_a_settings, 1)
                                    time.sleep(1) if s_settings else None
                                    tries_number += 1
                                    if tries_number == 1:
                                        s_e('sound/sound_effects/candles_wind.ogg', s_settings, 2)
                                        time.sleep(3.5) if s_settings else None
                                        g = set_generator(141)
                                        s_e('sound/voice_person/room_2/141.ogg', v_p_settings, 2)
                                        p_e(next(g), t_settings)
                                        time.sleep(7) if not t_settings and v_p_settings else None
                                        continue
                                    else:
                                        if tries_number < 3:
                                            s_e('sound/sound_effects/candles_wind.ogg', s_settings, 2)
                                            time.sleep(3.5) if s_settings else None
                                            random_failure(t_settings, v_p_settings, failures)
                                            continue
                                        else:

                                            """смерть от дротика"""
                                            g = set_generator(150)
                                            print(next(g))
                                            s_e('sound/sound_effects/dart.ogg', s_settings, 2)
                                            time.sleep(1) if s_settings else None
                                            room_2_mp3.stop() if m_settings else None
                                            s_e('sound/sound_effects/death.ogg', s_settings, 2)
                                            time.sleep(1) if s_settings else None
                                            dd_mp3.set_volume(0.2) if m_settings else None
                                            dd_mp3.play(-1) if m_settings else None
                                            s_e('sound/voice_person/room_2/151.ogg', v_p_settings, 2)
                                            p_e(next(g), t_settings)
                                            time.sleep(11) if not t_settings and v_p_settings else None
                                            s_e('sound/voice_person/room_2/152.ogg', v_p_settings, 2)
                                            p_e(next(g), t_settings)
                                            print('')
                                            time.sleep(6) if not t_settings and v_p_settings else None
                                            death_menu(t_settings, v_a_settings, m_settings)
                                            room_2_mp3.set_volume(0.1)
                                            room_2_mp3.play(-1) if m_settings else None
                                            determination = new_determination(t_settings, v_p_settings,
                                                                              v_a_settings, m_settings,
                                                                              s_settings, determination, 7, '-')
                                            random_revival(t_settings, v_p_settings, s_settings)
                                else:
                                    continue
                    else:
                        if candles_examined:
                            g = set_generator(121)
                            s_e('sound/voice_person/room_2/121.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(6.5) if not t_settings and v_p_settings else None
                            continue
                        else:
                            if candle_look_count == 1:
                                g = set_generator(121)
                                s_e('sound/voice_person/room_2/121.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(6) if not t_settings and v_p_settings else None
                                continue
                            else:
                                r_n(t_settings, v_p_settings, no_use)
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
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_2/44.menu.ogg', v_a_settings, 1)

                else:
                    g = set_generator(50)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}'
                          f'4) {next(g)}' + '\n')
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_2/50. menu.ogg', v_a_settings, 1)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None
                if read_count == 0 and option != '4' and option != '5' and light_on:
                    s_e('sound/voice_person/room_2/67.ogg', v_p_settings, 2)
                    p_e(reactions[0], t_settings)
                    time.sleep(1) if v_p_settings else None
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
                    if paper_1_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        if light_on:
                            read_count += 1
                            paper_1_read = True
                            g = set_generator_riddle(1)
                            s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                            time.sleep(2) if s_settings else None
                            p_e(next(g), t_settings)
                            p_e(next(g), t_settings)
                            s_e('sound/voice_person/room_2/R1.ogg', v_p_settings, 2)
                            time.sleep(20) if not t_settings and v_p_settings else None
                            s_e('sound/voice_person/room_2/69.ogg', v_p_settings, 2) if read_count == 1 else None
                            p_e(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(7) if read_count == 1 and v_p_settings else None
                            s_e('sound/voice_person/room_2/70.ogg', v_p_settings, 2) if read_count == 1 else None
                            p_e(reactions[2], t_settings) if read_count == 1 else None
                            time.sleep(4.5) if read_count == 1 and v_p_settings else None
                            s_e('sound/voice_person/room_2/77.ogg', v_p_settings, 2) if read_count == 2 else None
                            p_e(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(7) if read_count == 2 and v_p_settings else None
                            s_e('sound/voice_person/room_2/84.ogg', v_p_settings, 2) if read_count == 3 else None
                            p_e(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(8) if read_count == 3 and v_p_settings else None
                            s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                            time.sleep(2) if s_settings else None
                            continue
                        else:
                            p_e(no_light, t_settings)
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
                            s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                            time.sleep(2) if s_settings else None
                            if language_found == 2:
                                s_e('sound/voice_person/room_2/80.ogg', v_p_settings, 2)
                                p_e(reactions[7], t_settings)
                                time.sleep(5) if v_p_settings else None
                            s_e('sound/voice_person/room_2/73.ogg', v_p_settings, 2)
                            p_e(reactions[3], t_settings)
                            time.sleep(6.5) if v_p_settings else None
                            s_e('sound/voice_person/room_2/74.ogg', v_p_settings, 2)
                            p_e(reactions[4], t_settings)
                            time.sleep(6.5) if v_p_settings else None
                            s_e('sound/voice_person/room_2/75.ogg', v_p_settings, 2)
                            p_e(reactions[5], t_settings)
                            p_e(next(g), t_settings)
                            p_e(next(g), t_settings)
                            s_e('sound/voice_person/room_2/R2.ogg', v_p_settings, 2)
                            time.sleep(20) if not t_settings and v_p_settings else None
                            s_e('sound/voice_person/room_2/69.ogg', v_p_settings, 2) if read_count == 1 else None
                            p_e(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(7) if read_count == 1 and v_p_settings else None
                            s_e('sound/voice_person/room_2/70.ogg', v_p_settings, 2) if read_count == 1 else None
                            p_e(reactions[2], t_settings) if read_count == 1 else None
                            time.sleep(4.5) if read_count == 1 and v_p_settings else None
                            s_e('sound/voice_person/room_2/77.ogg', v_p_settings, 2) if read_count == 2 else None
                            p_e(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(7) if read_count == 2 and v_p_settings else None
                            s_e('sound/voice_person/room_2/84.ogg', v_p_settings, 2) if read_count == 3 else None
                            p_e(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(8) if read_count == 3 and v_p_settings else None
                            time.sleep(1) if read_count == 3 else None
                            s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                            time.sleep(2) if s_settings else None
                            continue
                        else:
                            p_e(no_light, t_settings)
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
                            s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                            time.sleep(2) if s_settings else None
                            if language_found == 2:
                                s_e('sound/voice_person/room_2/80.ogg', v_p_settings, 2)
                                p_e(reactions[7], t_settings)
                                time.sleep(5) if v_p_settings else None
                            s_e('sound/voice_person/room_2/81.ogg', v_p_settings, 2)
                            p_e(reactions[8], t_settings)
                            time.sleep(9) if v_p_settings else None
                            s_e('sound/voice_person/room_2/82.ogg', v_p_settings, 2)
                            p_e(reactions[9], t_settings)
                            p_e(next(g), t_settings)
                            p_e(next(g), t_settings)
                            s_e('sound/voice_person/room_2/R3.ogg', v_p_settings, 2)
                            time.sleep(20) if not t_settings and v_p_settings else None
                            s_e('sound/voice_person/room_2/69.ogg', v_p_settings, 2) if read_count == 1 else None
                            p_e(reactions[1], t_settings) if read_count == 1 else None
                            time.sleep(6) if read_count == 1 and v_p_settings else None
                            s_e('sound/voice_person/room_2/70.ogg', v_p_settings, 2) if read_count == 1 else None
                            p_e(reactions[2], t_settings) if read_count == 1 else None
                            time.sleep(34.5) if read_count == 1 and v_p_settings else None
                            s_e('sound/voice_person/room_2/77.ogg', v_p_settings, 2) if read_count == 2 else None
                            p_e(reactions[6], t_settings) if read_count == 2 else None
                            time.sleep(7) if read_count == 2 and v_p_settings else None
                            s_e('sound/voice_person/room_2/84.ogg', v_p_settings, 2) if read_count == 3 else None
                            p_e(reactions[10], t_settings) if read_count == 3 else None
                            time.sleep(8) if read_count == 3 and v_p_settings else None
                            s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                            time.sleep(2) if s_settings else None
                            continue
                        else:
                            p_e(no_light, t_settings)
                elif option == '4':
                    if paper_1_read and paper_2_read and paper_3_read:
                        papers_combined = True
                        s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        s_e('sound/voice_person/room_2/87.ogg', v_p_settings, 2)
                        p_e(reactions[11], t_settings)
                        time.sleep(7) if v_p_settings else None
                        s_e('sound/voice_person/room_2/88.ogg', v_p_settings, 2)
                        p_e(reactions[12], t_settings)
                        time.sleep(5) if v_p_settings else None
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
                        s_e('sound/voice_person/room_2/Riddle.ogg', v_p_settings, 2)
                        time.sleep(40) if v_p_settings else None
                        s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                        time.sleep(1) if s_settings else None
                        s_e('sound/voice_person/room_2/91.ogg', v_p_settings, 2)
                        p_e(reactions[13], t_settings)
                        time.sleep(10) if v_p_settings else None
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
        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
        time.sleep(2) if v_a_settings else None
        if not chest_opened:
            chest_opened = True
        if sack_took:
            g = set_generator(287)
            print(f'1) {next(g)}'
                  f'2) {next(g)}' + '\n')
            record = s_e('sound/voice_actions/room_2/287.menu.ogg', v_a_settings, 1)
        else:
            g = set_generator(162)
            print(f'1) {next(g)}'
                  f'2) {next(g)}'
                  f'3) {next(g)}' + '\n')
            record = s_e('sound/voice_actions/room_2/162.menu.ogg', v_a_settings, 1)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None
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
            if papers_read:
                r_n(t_settings, v_p_settings, no_use)
                continue
            else:
                papers_read = True
                g = set_generator(167)
                s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                time.sleep(2) if s_settings else None
                s_e('sound/voice_person/room_2/167.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                next(g)
                s_e('sound/voice_person/room_2/169.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                p_e(next(g) + '\n', t_settings)
                time.sleep(9) if not t_settings and v_p_settings else None
                next(g)
                s_e('sound/voice_person/room_2/172.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                p_e(next(g) + '\n', t_settings)
                time.sleep(8) if not t_settings and v_p_settings else None
                s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                time.sleep(2) if s_settings else None
                next(g)
                s_e('sound/voice_person/room_2/175.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(8) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/176.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(13) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/177.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                continue
        elif option == '2':
            if sack_took:
                if papers_read:
                    break
                else:
                    g = set_generator(185)
                    s_e('sound/voice_person/room_2/185.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(7) if not t_settings and v_p_settings else None
                    continue
            else:
                sack_took = True
                g = set_generator(180)
                s_e('sound/voice_person/room_2/180.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(11) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/181.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(4) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/182.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(12) if not t_settings and v_p_settings else None
        elif option == '3':
            if sack_took:
                print(w(t_settings, v_a_settings))
                continue
            else:
                g = set_generator(185)
                s_e('sound/voice_person/room_2/185.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(7) if not t_settings and v_p_settings else None
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
        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
        time.sleep(2) if v_a_settings else None
        record = s_e('sound/voice_actions/room_2/187.menu.ogg', v_a_settings, 1)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None
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
            while True:
                if break_indicator:
                    break
                g = set_generator(191)
                s_e('sound/voice_person/room_2/191.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(5.5) if not t_settings and v_p_settings else None
                next(g)
                print(f'1) {next(g)}'
                      f'2) {next(g)}' + '\n')
                s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                time.sleep(2) if v_a_settings else None
                record = s_e('sound/voice_actions/room_2/193.menu.ogg', v_a_settings, 1)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None
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
                    g = set_generator(197)
                    s_e('sound/voice_person/room_2/197.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(3) if not t_settings and v_p_settings else None
                    print(next(g))
                    s_e('sound/sound_effects/mechanism.ogg', s_settings, 2)
                    time.sleep(2) if s_settings else None
                    s_e('sound/voice_person/room_2/199.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(6) if not t_settings and v_p_settings else None
                    s_e('sound/voice_person/room_2/200.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(6) if not t_settings and v_p_settings else None
                    s_e('sound/voice_person/room_2/201.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(10.5) if not t_settings and v_p_settings else None
                    while True:
                        if break_indicator:
                            break
                        g = set_generator(203)
                        print(f'1) {next(g)}' + '\n')
                        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                        time.sleep(2) if v_a_settings else None
                        record = s_e('sound/voice_actions/room_2/203.menu.ogg', v_a_settings, 1)
                        option = input('Введите цифру: ')
                        record.stop() if v_a_settings else None
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
                            g = set_generator(204)
                            s_e('sound/voice_person/room_2/204.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(11) if not t_settings and v_p_settings else None
                            while True:
                                g = set_generator(206)
                                print(f'1) {next(g)}' + '\n')
                                s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                                time.sleep(2) if v_a_settings else None
                                record = s_e('sound/voice_actions/room_2/206.menu.ogg', v_a_settings, 1)
                                option = input('Введите цифру: ')
                                record.stop() if v_a_settings else None
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
                                    g = set_generator(207)
                                    break_indicator = True
                                    s_e('sound/voice_person/room_2/207.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    s_e('sound/voice_person/room_2/208.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(8) if not t_settings and v_p_settings else None
                                    s_e('sound/voice_person/room_2/209.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(6) if not t_settings and v_p_settings else None
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
    while True:
        g = set_generator(211)
        print(f'1) {next(g)}'
              f'2) {next(g)}')
        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
        time.sleep(2) if v_a_settings else None
        record = s_e('sound/voice_actions/room_2/211.menu.ogg', v_a_settings, 1)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None
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
            while True:
                if steroids_taken:
                    g = set_generator(282)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' + '\n')
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_2/282.menu.ogg', v_a_settings, 1)
                else:
                    g = set_generator(214)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}'
                          f'3) {next(g)}' 
                          f'4) {next(g)}' + '\n')
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_2/214.menu.ogg', v_a_settings, 1)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None
                if option == '100':
                    q(t_settings, v_a_settings, 1)
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
                    if book_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        book_read = True
                        g = set_generator(220)
                        s_e('sound/voice_person/room_2/220.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(5) if not t_settings and v_p_settings else None
                        s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        next(g)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/222.ogg', v_p_settings, 2)
                        time.sleep(24) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/226.ogg', v_p_settings, 2)
                        time.sleep(34) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        s_e('sound/voice_person/room_2/231.ogg', v_p_settings, 2)
                        time.sleep(25) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        s_e('sound/voice_person/room_2/235.ogg', v_p_settings, 2)
                        time.sleep(25) if not t_settings and v_p_settings else None
                        s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        print('')
                        next(g)
                        s_e('sound/voice_person/room_2/239.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(11) if not t_settings and v_p_settings else None
                        continue
                elif option == '2':
                    if log_read:
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    else:
                        log_read = True
                        g = set_generator(242)
                        s_e('sound/voice_person/room_2/242.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(5) if not t_settings and v_p_settings else None
                        s_e('sound/voice_person/room_2/243.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(6) if not t_settings and v_p_settings else None
                        next(g)
                        print('')
                        s_e('sound/sound_effects/papers_open.mp3', s_settings, 2)
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
                        s_e('sound/voice_person/room_2/245.ogg', v_p_settings, 2)
                        time.sleep(61) if not t_settings and v_p_settings else None
                        s_e('sound/sound_effects/papers_close.mp3', s_settings, 2)
                        time.sleep(2) if s_settings else None
                        next(g)
                        print('')
                        s_e('sound/voice_person/room_2/258.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(5) if not t_settings and v_p_settings else None
                        continue
                elif option == '3':
                    if steroids_taken:
                        break
                    else:
                        g = set_generator(261)
                        steroids_taken = True
                        s_e('sound/voice_person/room_2/261.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(8) if not t_settings and v_p_settings else None
                        s_e('sound/voice_person/room_2/262.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(8) if not t_settings and v_p_settings else None
                        s_e('sound/voice_person/room_2/263.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(4) if not t_settings and v_p_settings else None
                        continue
                elif option == '4':
                    if steroids_taken:
                        print(w(t_settings, v_a_settings))
                        continue
                    else:
                        break
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        elif option == '2':
            if book_read and log_read:
                g = set_generator(269)
                s_e('sound/voice_person/room_2/269.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(6) if not t_settings and v_p_settings else None
                s_e('sound/voice_person/room_2/270.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                room_2_mp3.fadeout(2) if m_settings else None
                time.sleep(2) if m_settings else None
                final_data['determination'] = determination
                final_data['sack_took'] = steroids_taken
                return final_data
            else:
                g = set_generator(267)
                s_e('sound/voice_person/room_2/267.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(5) if not t_settings and v_p_settings else None
                continue
        else:
            print(w(t_settings, v_a_settings))
            continue
