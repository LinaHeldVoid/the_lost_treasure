import time

from colorama import Fore, Style

from sound_manager import room_1_mp3, dd_mp3
from scenario_generator import generate_base
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, random_revival, determination_announcement as d_a, death_menu, \
    new_determination, print_help


def set_generator(line):
    i = 0
    g = generate_base('text/2_room_1.txt')
    while i < line:
        next(g)
        i += 1
    return g


def no_use_generator():
    no_use = []
    i = 0
    g = set_generator(145)
    while i < 5:
        no_use.append(next(g))
        i += 1
    return no_use


# главный зал
def room_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    no_use = no_use_generator()
    stone_moved = False
    chest_is_examined = False
    chest_is_opened = False
    stonewall_is_examined = False
    glass_is_examined = False
    bowl_is_examined = False
    diamond_is_taken = False
    twig_melted = False
    open_count = 0
    determination = 50

    g = set_generator(0)
    print(next(g))
    s_e('sound/voice_actions/room_1/4_room_1.ogg', v_a_settings, 1)
    time.sleep(2)
    s_e('sound/voice_person/room_1/8_enter_1.ogg', v_p_settings, 2)
    p_e(next(g), t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    s_e('sound/voice_person/room_1/9_enter_2.ogg', v_p_settings, 2)
    p_e(next(g), t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    s_e('sound/voice_person/room_1/10_enter_3.ogg', v_p_settings, 2)
    p_e(next(g), t_settings)
    time.sleep(2) if not t_settings and v_p_settings else None

    """осматриваемся"""
    while True:
        g = set_generator(5)
        print(f'1) {next(g)}')
        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
        time.sleep(2) if v_a_settings else None
        record = s_e('sound/voice_actions/room_1/5_look_around.ogg', v_a_settings, 1)
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
            s_e('sound/voice_person/room_1/11_room_examined.ogg', v_p_settings, 2)
            p_e(next(g), t_settings)
            time.sleep(9) if not t_settings and v_p_settings else None
            break
        else:
            print(w(t_settings, v_a_settings))
            continue

    while True:
        if chest_is_opened:
            g = set_generator(13)
            print(f'1) {next(g)}'
                  f'2) {next(g)}'
                  f'3) {next(g)}'
                  f'4) {next(g)}' + '\n')
            s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
            time.sleep(2) if v_a_settings else None
            record = s_e('sound/voice_actions/room_1/12_menu_2.ogg', v_a_settings, 1)
            option = input('Введите цифру: ')
            record.stop() if v_a_settings else None
        else:
            g = set_generator(8)
            print(f'1) {next(g)}'
                  f'2) {next(g)}'
                  f'3) {next(g)}'
                  f'4) {next(g)}' + '\n')
            s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
            time.sleep(2) if v_a_settings else None
            record = s_e('sound/voice_actions/room_1/6_menu_1.ogg', v_a_settings, 1)
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
            g = set_generator(19)
            bowl_is_examined = True
            s_e('sound/voice_person/room_1/12_bowl_examined_1.ogg', v_p_settings, 2)
            p_e(next(g), t_settings)
            time.sleep(18) if not t_settings and v_p_settings else None
            s_e('sound/voice_person/room_1/13_bowl_examined_2.ogg', v_p_settings, 2)
            p_e(next(g), t_settings)
            time.sleep(7) if not t_settings and v_p_settings else None

            """осматриваем чашу"""
            while True:
                g = set_generator(22)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
                s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                time.sleep(2) if v_a_settings else None
                record = s_e('sound/voice_actions/room_1/7_bowl_options.ogg', v_a_settings, 1)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None

                """смерть"""
                if option == '1':
                        g = set_generator(27)
                        room_1_mp3.stop() if m_settings else None
                        s_e('sound/sound_effects/death.ogg', s_settings, 3)
                        time.sleep(1) if s_settings else None
                        dd_mp3.set_volume(0.5) if m_settings else None
                        dd_mp3.play(-1) if m_settings else None
                        s_e('sound/voice_person/room_1/14_painful_death.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        time.sleep(11) if not t_settings and v_p_settings else None
                        s_e('sound/voice_person/room_1/15_the_end.ogg', v_p_settings, 2)
                        p_e(next(g), t_settings)
                        print('')
                        time.sleep(10) if not t_settings and v_p_settings else None
                        print(Fore.RED, f'{next(g)}')
                        print(Style.RESET_ALL)
                        death_menu(t_settings, v_a_settings, m_settings)
                        room_1_mp3.play(-1) if m_settings else None
                        determination = new_determination(t_settings, v_p_settings, v_a_settings, m_settings,
                                                          s_settings, determination, 7, '-')
                        random_revival(t_settings, v_p_settings, s_settings)
                elif option == '2':
                    g = set_generator(39)
                    s_e('sound/voice_person/room_1/16_bowl_not_lifted.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(10) if not t_settings and v_p_settings else None
                    continue
                elif option == '3':
                    break
                elif option == '100':
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
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        elif option == '2':

            """открываем сундук"""
            if chest_is_opened:
                open_count += 1
                g = set_generator(74)
                s_e('sound/sound_effects/open_chest.ogg', s_settings, 3)
                time.sleep(1.5) if s_settings else None
                if open_count == 1:
                    s_e('sound/voice_person/room_1/22_need_to_think.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(4) if not t_settings and v_p_settings else None
                while True:
                    if diamond_is_taken:
                        g = set_generator(68)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}' + '\n')
                        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                        time.sleep(2) if v_a_settings else None
                        record = s_e('sound/voice_actions/room_1/17_chest_opened_no_diamond.ogg', v_a_settings, 1)
                    else:
                        g = set_generator(61)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'                  
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}'
                              f'6) {next(g)}' + '\n')
                        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                        time.sleep(2) if v_a_settings else None
                        record = s_e('sound/voice_actions/room_1/17_chest_inside.ogg', v_a_settings, 1)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None

                    if option == '1':

                        """используем прут"""
                        while True:
                            if bowl_is_examined:
                                if twig_melted:
                                    g = set_generator(87)
                                    p_e(next(g), t_settings)
                                    s_e('sound/voice_person/room_1/26_no_use_twig.ogg', v_a_settings, 1)
                                    time.sleep(6.5) if not t_settings and v_a_settings else None
                                    break
                                else:
                                    g = set_generator(78)
                                    print(f'1) {next(g)}'
                                          f'2) {next(g)}' + '\n')
                                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                                    time.sleep(2) if v_a_settings else None
                                    record = s_e('sound/voice_actions/room_1/9_twig_options.ogg', v_a_settings, 1)
                                    option = input('Введите цифру: ')
                                    record.stop() if v_a_settings else None
                                    if option == '1':
                                        g = set_generator(82)
                                        twig_melted = True
                                        s_e('sound/voice_person/room_1/23_twig_attempt.ogg', v_p_settings, 2)
                                        p_e(next(g), t_settings)
                                        time.sleep(2.5) if not t_settings and v_p_settings else None
                                        print(next(g))
                                        s_e('sound/sound_effects/acid_hiss.ogg', s_settings, 3)
                                        time.sleep(3.5) if s_settings else None
                                        s_e('sound/voice_person/room_1/24_twig_failure_1.ogg', v_p_settings, 2)
                                        p_e(next(g), t_settings)
                                        time.sleep(11) if not t_settings and v_p_settings else None
                                        s_e('sound/voice_person/room_1/25_twig_failure_2.ogg', v_p_settings, 2)
                                        p_e(next(g), t_settings)
                                        time.sleep(16) if not t_settings and v_p_settings else None
                                        break
                                    elif option == '2':
                                        break
                                    elif option == '100':
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
                                    else:
                                        print(w(t_settings, v_a_settings))
                                        continue
                            else:
                                r_n(t_settings, v_p_settings, no_use)
                                continue
                    elif option == '2':
                        r_n(t_settings, v_p_settings, no_use)
                        continue
                    elif option == '3':
                        if stonewall_is_examined:

                            """разбиваем стену"""
                            while True:
                                g = set_generator(107)
                                print(f'1) {next(g)}' + '\n')
                                s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                                time.sleep(2) if v_a_settings else None
                                record = s_e('sound/voice_actions/room_1/14_smash_menu.ogg', v_a_settings, 1)
                                option = input('Введите цифру: ')
                                record.stop() if v_a_settings else None
                                if option == '1':
                                    g = set_generator(108)
                                    s_e('sound/voice_person/room_1/29_lets_smash.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(6) if not t_settings and v_p_settings else None
                                    print(next(g))
                                    s_e('sound/sound_effects/wall_smashed.ogg', s_settings, 3)
                                    time.sleep(8) if s_settings else None
                                    s_e('sound/voice_person/room_1/30_wall_smashed.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(6) if not t_settings and v_p_settings else None
                                    print(next(g))
                                    s_e('sound/sound_effects/stones.ogg', s_settings, 3)
                                    time.sleep(1) if s_settings else None
                                    s_e('sound/sound_effects/giant_stone.ogg', s_settings, 3)
                                    time.sleep(7) if s_settings else None
                                    s_e('sound/voice_person/room_1/30_something_wrong.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None

                                    """обвал"""
                                    next(g)
                                    print(next(g))
                                    room_1_mp3.stop() if m_settings else None
                                    dd_mp3.set_volume(0.2) if m_settings else None
                                    dd_mp3.play(-1) if m_settings else None
                                    s_e('sound/voice_person/room_1/31_trapped_1.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    determination = new_determination(t_settings, v_p_settings, v_a_settings,
                                                                      m_settings,
                                                                      s_settings, determination, 10, '-')
                                    s_e('sound/voice_person/room_1/32_trapped_2.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(13) if not t_settings and v_p_settings else None
                                    s_e('sound/voice_person/room_1/33_trapped_3.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(7) if not t_settings and v_p_settings else None
                                    next(g)
                                    print(next(g))
                                    dd_mp3.stop() if m_settings else None
                                    room_1_mp3.play(-1) if m_settings else None
                                    s_e('sound/voice_person/room_1/34_decision.ogg', v_p_settings, 2)
                                    p_e(next(g), t_settings)
                                    time.sleep(17) if not t_settings and v_p_settings else None

                                    """принимаем решение"""
                                    while True:
                                        g = set_generator(122)
                                        print(f'1) {next(g)}'
                                              f'2) {next(g)}')
                                        s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                                        time.sleep(2) if v_a_settings else None
                                        record = s_e('sound/voice_actions/room_1/16_final_menu.ogg', v_a_settings, 1)
                                        option = input('Введите цифру: ')
                                        record.stop() if v_a_settings else None
                                        if option == '1':
                                            s_e('sound/sound_effects/open_chest.ogg', s_settings, 3)
                                            time.sleep(1.5) if s_settings else None
                                            while True:
                                                g = set_generator(127)
                                                if diamond_is_taken:
                                                    print(f'1) {next(g)}'
                                                          f'2) {next(g)}'
                                                          f'3) {next(g)}')
                                                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                                                    time.sleep(2) if v_a_settings else None
                                                    record = s_e('sound/voice_actions/room_1/18_fm_2.ogg',
                                                                 v_a_settings, 1)
                                                    option = input('Введите цифру: ')
                                                    record.stop() if v_a_settings else None
                                                    if option == '1':
                                                        r_n(t_settings, v_p_settings, no_use)
                                                        continue
                                                    elif option == '2':
                                                        if glass_is_examined:
                                                            r_n(t_settings, v_p_settings, no_use)
                                                        else:
                                                            g = set_generator(93)
                                                            s_e('sound/voice_person/room_1/27_no_glass.ogg',
                                                                v_p_settings, 2)
                                                            p_e(next(g), t_settings)
                                                            time.sleep(7) if not t_settings and v_p_settings else None
                                                        continue
                                                    elif option == '3':
                                                        s_e('sound/sound_effects/close_chest.ogg', s_settings, 3)
                                                        time.sleep(1.5) if s_settings else None
                                                        break
                                                    elif option == '100':
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
                                                    else:
                                                        print(w(t_settings, v_a_settings))
                                                        continue
                                                else:
                                                    g = set_generator(131)
                                                    print(f'1) {next(g)}'
                                                          f'2) {next(g)}'
                                                          f'3) {next(g)}'
                                                          f'4) {next(g)}')
                                                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                                                    time.sleep(2) if v_a_settings else None
                                                    record = s_e('sound/voice_actions/room_1/19_fm_3.ogg',
                                                                 v_a_settings, 1)
                                                    option = input('Введите цифру: ')
                                                    record.stop() if v_a_settings else None
                                                    if option == '1':
                                                        r_n(t_settings, v_p_settings, no_use)
                                                        continue
                                                    elif option == '2':
                                                        if glass_is_examined:
                                                            r_n(t_settings, v_p_settings, no_use)
                                                        else:
                                                            g = set_generator(93)
                                                            s_e('sound/voice_person/room_1/27_no_glass.ogg',
                                                                v_p_settings, 2)
                                                            p_e(next(g), t_settings)
                                                            time.sleep(7) if not t_settings and v_p_settings else None
                                                        continue
                                                    elif option == '3':
                                                        g = set_generator(98)
                                                        diamond_is_taken = True
                                                        s_e('sound/voice_person/room_1/28_took_diamond.ogg',
                                                            v_p_settings, 2)
                                                        p_e(next(g), t_settings)
                                                        time.sleep(17) if not t_settings and v_p_settings else None
                                                        continue
                                                    elif option == '4':
                                                        s_e('sound/sound_effects/close_chest.ogg', s_settings, 3)
                                                        time.sleep(1.5) if s_settings else None
                                                        break
                                                    elif option == '100':
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
                                                    else:
                                                        print(w(t_settings, v_a_settings))
                                                        continue

                                        elif option == '2':
                                            if diamond_is_taken:
                                                g = set_generator(139)
                                                s_e('sound/voice_person/room_1/36_last_hope.ogg', v_p_settings, 2)
                                                p_e(next(g), t_settings)
                                                time.sleep(5) if not t_settings and v_p_settings else None
                                                print(next(g))
                                                room_1_mp3.fadeout(2) if m_settings else None
                                                time.sleep(2) if m_settings else None
                                                return determination
                                            else:
                                                g = set_generator(137)
                                                s_e('sound/voice_person/room_1/35_need_diamond.ogg', v_p_settings, 2)
                                                p_e(next(g), t_settings)
                                                time.sleep(7.5) if not t_settings and v_p_settings else None
                                                continue
                                else:
                                    print(w(t_settings, v_a_settings))
                                    continue
                        else:
                            r_n(t_settings, v_p_settings, no_use)
                        continue
                    elif option == '4':
                        if diamond_is_taken:
                            if glass_is_examined:
                                g = set_generator(95)
                                p_e(next(g), t_settings)
                                break
                            else:
                                g = set_generator(93)
                                s_e('sound/voice_person/room_1/27_no_glass.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(7) if not t_settings and v_p_settings else None
                                continue
                        else:
                            g = set_generator(98)
                            diamond_is_taken = True
                            s_e('sound/voice_person/room_1/28_took_diamond.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(17) if not t_settings and v_p_settings else None
                            continue
                    elif option == '5':
                        if diamond_is_taken:
                            s_e('sound/sound_effects/close_chest.ogg', s_settings, 3)
                            time.sleep(1.5) if s_settings else None
                            break
                        else:
                            if glass_is_examined:
                                g = set_generator(100)
                                p_e(next(g), t_settings)
                                break
                            else:
                                g = set_generator(93)
                                s_e('sound/voice_person/room_1/27_no_glass.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(7) if not t_settings and v_p_settings else None
                                continue
                    elif option == '6':
                        if diamond_is_taken:
                            print(w(t_settings, v_a_settings))
                            continue
                        else:
                            s_e('sound/sound_effects/close_chest.ogg', s_settings, 3)
                            time.sleep(1.5) if s_settings else None
                            break
                    elif option == '100':
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
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
            else:
                if chest_is_examined:
                    g = set_generator(100)
                    p_e(next(g), t_settings)
                    continue
                else:
                    g = set_generator(42)
                    chest_is_examined = True
                    s_e('sound/voice_person/room_1/17_chest_examined.ogg', v_p_settings, 2)
                    p_e(next(g), t_settings)
                    time.sleep(12) if not t_settings and v_p_settings else None
        elif option == '3':
            if stonewall_is_examined:
                g = set_generator(95)
                p_e(next(g), t_settings)
                continue
            else:
                g = set_generator(45)
                stonewall_is_examined = True
                s_e('sound/voice_person/room_1/18_stonewall_examined.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(13.5) if not t_settings and v_p_settings else None
                continue
        elif option == '4':
            if stone_moved:
                g = set_generator(100)
                s_e('sound/voice_person/no_use_2.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(3.5) if not t_settings and v_p_settings else None
                continue
            else:
                """двигаем камень"""
                g = set_generator(48)
                stone_moved = True
                s_e('sound/voice_person/room_1/19_stone_examined.ogg', v_p_settings, 2)
                p_e(next(g), t_settings)
                time.sleep(7.5) if not t_settings and v_p_settings else None
                while True:
                    g = set_generator(50)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}' + '\n')
                    s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                    time.sleep(2) if v_a_settings else None
                    record = s_e('sound/voice_actions/room_1/13_stone_menu.ogg', v_a_settings, 1)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None
                    if option == '1':
                        g = set_generator(54)
                        s_e('sound/sound_effects/move_stone.ogg', s_settings, 3)
                        time.sleep(6.5) if s_settings else None
                        if chest_is_examined:
                            s_e('sound/voice_person/room_1/20_key_found.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(4) if not t_settings and v_p_settings else None
                        else:
                            chest_is_examined = True
                            g = set_generator(56)
                            s_e('sound/voice_person/room_1/57_unexpected_key.ogg', v_p_settings, 2)
                            p_e(next(g), t_settings)
                            time.sleep(6.5) if not t_settings and v_p_settings else None
                        while True:
                            g = set_generator(58)
                            print(f'1) {next(g)}' + '\n')
                            s_e('sound/voice_actions/option.ogg', v_a_settings, 1)
                            time.sleep(2) if v_a_settings else None
                            record = s_e('sound/voice_actions/room_1/17_open_chest_menu.ogg', v_a_settings, 1)
                            option = input('Введите цифру: ')
                            record.stop() if v_a_settings else None
                            if option == '1':
                                g = set_generator(59)
                                s_e('sound/sound_effects/key.ogg', s_settings, 3)
                                time.sleep(2) if s_settings else None
                                s_e('sound/voice_person/room_1/21_chest_opened.ogg', v_p_settings, 2)
                                p_e(next(g), t_settings)
                                time.sleep(7.5) if not t_settings and v_p_settings else None
                                chest_is_opened = True
                                break
                            elif option == '100':
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
                        break
                    elif option == '2':
                        break
                    elif option == '100':
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
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
                continue
        else:
            print(w(t_settings, v_a_settings))
            continue
