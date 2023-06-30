import time

from colorama import Fore, Style

from sound_manager import room_1_mp3, dd_mp3
from scenario_generator import generate_base
from console_game.service_fuctions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n


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
    g = set_generator(276)
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

    g = set_generator(0)
    print(next(g))
    s_e('../sound/voice_actions/room_1/4_room_1.wav', v_a_settings)
    time.sleep(2)
    s_e('../sound/voice_person/room_1/8_enter_1.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    time.sleep(2)
    s_e('../sound/voice_person/room_1/9_enter_2.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    time.sleep(2)
    s_e('../sound/voice_person/room_1/10_enter_3.wav', v_p_settings)
    p_e(next(g), t_settings)
    time.sleep(2) if not t_settings and v_p_settings else None
    time.sleep(2)

    """осматриваемся"""
    while True:
        g = set_generator(5)
        print(f'1) {next(g)}')
        s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        record = s_e('../sound/voice_actions/room_1/5_look_around.wav', v_a_settings)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None if v_a_settings else None
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
            s_e('../sound/voice_person/room_1/11_room_examined.wav', v_p_settings)
            p_e(next(g), t_settings)
            time.sleep(8) if not t_settings and v_p_settings else None
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
            s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            record = s_e('../sound/voice_actions/room_1/12_menu_2.wav', v_a_settings)
            option = input('Введите цифру: ')
            record.stop() if v_a_settings else None
        else:
            g = set_generator(8)
            print(f'1) {next(g)}'
                  f'2) {next(g)}'
                  f'3) {next(g)}'
                  f'4) {next(g)}' + '\n')
            s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            record = s_e('../sound/voice_actions/room_1/6_menu_1.wav', v_a_settings)
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
            g = set_generator(19)
            bowl_is_examined = True
            s_e('../sound/voice_person/room_1/12_bowl_examined_1.wav', v_p_settings)
            p_e(next(g), t_settings)
            time.sleep(17) if not t_settings and v_p_settings else None
            time.sleep(1)
            s_e('../sound/voice_person/room_1/13_bowl_examined_2.wav', v_p_settings)
            p_e(next(g), t_settings)
            time.sleep(6) if not t_settings and v_p_settings else None
            time.sleep(2)

            """осматриваем чашу"""
            while True:
                g = set_generator(22)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
                s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                time.sleep(2) if not t_settings and v_a_settings else None
                record = s_e('../sound/voice_actions/room_1/7_bowl_options.wav', v_a_settings)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None

                """смерть"""
                if option == '1':
                    while True:
                        g = set_generator(29)
                        print(next(g))
                        room_1_mp3.stop() if m_settings else None
                        s_e('../sound/sound_effects/death.wav', s_settings)
                        time.sleep(1) if s_settings else None
                        dd_mp3.set_volume(0.2) if m_settings else None
                        dd_mp3.play(-1) if m_settings else None
                        s_e('../sound/voice_person/room_1/14_painful_death.wav', v_p_settings)
                        p_e(next(g), t_settings)
                        time.sleep(10) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        s_e('../sound/voice_person/room_1/15_the_end.wav', v_p_settings)
                        p_e(next(g), t_settings)
                        print('')
                        time.sleep(9) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        print(Fore.RED, f'{next(g)}')
                        print(Style.RESET_ALL)
                        print(next(g))
                        next(g)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}' + '\n')
                        record = s_e('../sound/voice_actions/room_1/10_death_menu.wav',
                                              v_a_settings)
                        option = input(f'Введите цифру: ')
                        record.stop() if v_a_settings else None
                        if option == '1':
                            dd_mp3.stop() if m_settings else None
                            room_1_mp3.play(-1) if m_settings else None
                            s_e('../sound/voice_actions/room_1/11_game_resume.wav', v_a_settings)
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
                elif option == '2':
                    g = set_generator(39)
                    s_e('../sound/voice_person/room_1/16_bowl_not_lifted.wav', v_p_settings)
                    p_e(next(g), t_settings)
                    time.sleep(9) if not t_settings and v_p_settings else None
                    time.sleep(1)
                    continue
                elif option == '3':
                    break
                elif option == '100':
                    q(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                else:
                    print(w(t_settings, v_a_settings))
                    continue
        elif option == '2':

            """открываем сундук"""
            if chest_is_opened:
                g = set_generator(59)
                s_e('../sound/s_es/open_chest.wav', s_settings)
                time.sleep(1.5) if s_settings else None
                s_e('../sound/voice_person/room_1/22_need_to_think.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                time.sleep(1)
                while True:
                    s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    if diamond_is_taken:
                        g = set_generator(68)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}' + '\n')
                        record = s_e('../sound/voice_actions/room_1/17_chest_inside.wav', v_a_settings)
                    else:
                        g = set_generator(61)
                        print(f'1) {next(g)}'
                              f'2) {next(g)}'                  
                              f'3) {next(g)}'
                              f'4) {next(g)}'
                              f'5) {next(g)}'
                              f'6) {next(g)}' + '\n')
                        record = s_e('../sound/voice_actions/room_1/17_chest_opened_no_diamond.wav', v_a_settings)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None

                    if option == '1':

                        """используем прут"""
                        while True:
                            if bowl_is_examined:
                                if twig_melted:
                                    g = set_generator(87)
                                    p_e(next(g), t_settings)
                                    s_e('../sound/voice_person/room_1/26_no_use_twig.wav', v_a_settings)
                                    time.sleep(5.5) if not t_settings and v_a_settings else None
                                    break
                                else:
                                    g = set_generator(78)
                                    print(f'1) {next(g)}'
                                          f'2) {next(g)}' + '\n')
                                    s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                                    time.sleep(2) if not t_settings and v_a_settings else None
                                    record = s_e('../sound/voice_actions/room_1/9_twig_options.wav', v_a_settings)
                                    option = input('Введите цифру: ')
                                    record.stop() if v_a_settings else None
                                    if option == '1':
                                        g = set_generator(82)
                                        twig_melted = True
                                        s_e('../sound/voice_person/room_1/23_twig_attempt.wav', v_p_settings)
                                        p_e(next(g), t_settings)
                                        time.sleep(1.5) if not t_settings and v_p_settings else None
                                        time.sleep(1)
                                        print(next(g))
                                        s_e('../sound/s_es/acid_hiss.wav', s_settings)
                                        time.sleep(2.5) if s_settings else None
                                        time.sleep(1)
                                        s_e('../sound/voice_person/room_1/24_twig_failure_1.wav', v_p_settings)
                                        p_e(next(g), t_settings)
                                        time.sleep(10) if not t_settings and v_p_settings else None
                                        time.sleep(1)
                                        s_e('../sound/voice_person/room_1/25_twig_failure_2.wav', v_p_settings)
                                        p_e(next(g), t_settings)
                                        time.sleep(15) if not t_settings and v_p_settings else None
                                        time.sleep(1)
                                        break
                                    elif option == '2':
                                        break
                                    elif option == '100':
                                        q(t_settings, v_a_settings)
                                        continue
                                    elif option == '0':
                                        if v_a_settings:
                                            continue
                                        else:
                                            print('Озвучивание опций отключено')
                                            continue
                                    else:
                                        print(w(t_settings, v_a_settings))
                                        continue
                            else:
                                r_n(t_settings, v_p_settings, no_use)
                                time.sleep(1)
                                continue
                    elif option == '2':
                        r_n(t_settings, v_p_settings, no_use)
                        time.sleep(1)
                        continue
                    elif option == '3':
                        if stonewall_is_examined:

                            """разбиваем стену"""
                            while True:
                                g = set_generator(107)
                                print(f'1) {next(g)}' + '\n')
                                s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                                time.sleep(2) if not t_settings and v_a_settings else None
                                record = s_e('../sound/voice_actions/room_1/14_smash_menu.wav', v_a_settings)
                                option = input('Введите цифру: ')
                                record.stop() if v_a_settings else None
                                if option == '1':
                                    g = set_generator(108)
                                    s_e('../sound/voice_person/room_1/29_lets_smash.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    print(next(g))
                                    s_e('../sound/s_es/wall_smashed.wav', s_settings)
                                    time.sleep(8) if s_settings else None
                                    s_e('../sound/voice_person/room_1/30_wall_smashed.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    print(next(g))
                                    s_e('../sound/s_es/stones.wav', s_settings)
                                    time.sleep(1) if s_settings else None
                                    s_e('../sound/s_es/giant_stone.wav', s_settings)
                                    time.sleep(7) if s_settings else None
                                    s_e('../sound/voice_person/room_1/30_something_wrong.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(4) if not t_settings and v_p_settings else None
                                    time.sleep(2)

                                    """обвал"""
                                    next(g)
                                    print(next(g))
                                    time.sleep(1)
                                    room_1_mp3.stop() if m_settings else None
                                    dd_mp3.set_volume(0.2) if m_settings else None
                                    dd_mp3.play(-1) if m_settings else None
                                    s_e('../sound/voice_person/room_1/31_trapped_1.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(4) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    s_e('../sound/voice_person/room_1/32_trapped_2.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(12) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    s_e('../sound/voice_person/room_1/33_trapped_3.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(6) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    next(g)
                                    print(next(g))
                                    time.sleep(1)
                                    dd_mp3.stop() if m_settings else None
                                    room_1_mp3.play(-1) if m_settings else None
                                    s_e('../sound/voice_person/room_1/34_decision.wav', v_p_settings)
                                    p_e(next(g), t_settings)
                                    time.sleep(16) if not t_settings and v_p_settings else None
                                    time.sleep(2)

                                    """принимаем решение"""
                                    while True:
                                        g = set_generator(122)
                                        print(f'1) {next(g)}'
                                              f'2) {next(g)}')
                                        s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                                        time.sleep(2) if not t_settings and v_a_settings else None
                                        record = s_e('../sound/voice_actions/room_1/16_final_menu.wav', v_a_settings)
                                        option = input('Введите цифру: ')
                                        record.stop() if v_a_settings else None
                                        if option == '1':
                                            g = set_generator(127)
                                            s_e('../sound/s_es/open_chest.wav', s_settings)
                                            time.sleep(1.5) if s_settings else None
                                            while True:
                                                if diamond_is_taken:
                                                    print(f'1) {next(g)}'
                                                          f'2) {next(g)}'
                                                          f'3) {next(g)}')
                                                    s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                                                    time.sleep(2) if not t_settings and v_a_settings else None
                                                    record = s_e('../sound/voice_actions/room_1/18_fm_2.wav', v_a_settings)
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
                                                            s_e('../sound/voice_person/room_1/27_no_glass.wav',
                                                                v_p_settings)
                                                            p_e(next(g), t_settings)
                                                            time.sleep(6) if not t_settings and v_p_settings else None
                                                            time.sleep(1)
                                                        continue
                                                    elif option == '3':
                                                        s_e('../sound/s_es/close_chest.wav', s_settings)
                                                        time.sleep(1.5) if s_settings else None
                                                        break
                                                    elif option == '100':
                                                        q(t_settings, v_a_settings)
                                                        continue
                                                    elif option == '0':
                                                        if v_a_settings:
                                                            continue
                                                        else:
                                                            print('Озвучивание опций отключено')
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
                                                    s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                                                    time.sleep(2) if not t_settings and v_a_settings else None
                                                    record = s_e('../sound/voice_actions/room_1/19_fm_3.wav', v_a_settings)
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
                                                            s_e('../sound/voice_person/room_1/27_no_glass.wav',
                                                                v_p_settings)
                                                            p_e(next(g), t_settings)
                                                            time.sleep(6) if not t_settings and v_p_settings else None
                                                            time.sleep(1)
                                                        continue
                                                    elif option == '3':
                                                        g = set_generator(98)
                                                        diamond_is_taken = True
                                                        s_e('../sound/voice_person/room_1/28_took_diamond.wav',
                                                            v_p_settings)
                                                        p_e(next(g), t_settings)
                                                        time.sleep(16) if not t_settings and v_p_settings else None
                                                        time.sleep(1)
                                                        continue
                                                    elif option == '4':
                                                        s_e('../sound/s_es/close_chest.wav', s_settings)
                                                        time.sleep(1.5) if s_settings else None
                                                        break
                                                    elif option == '100':
                                                        q(t_settings, v_a_settings)
                                                        continue
                                                    elif option == '0':
                                                        if v_a_settings:
                                                            continue
                                                        else:
                                                            print('Озвучивание опций отключено')
                                                            continue
                                                    else:
                                                        print(w(t_settings, v_a_settings))
                                                        continue

                                        elif option == '2':
                                            if diamond_is_taken:
                                                g = set_generator(139)
                                                s_e('../sound/voice_person/room_1/36_last_hope.wav', v_p_settings)
                                                p_e(next(g), t_settings)
                                                time.sleep(4) if not t_settings and v_p_settings else None
                                                time.sleep(2)
                                                print(next(g))
                                                return
                                            else:
                                                g = set_generator(137)
                                                s_e('../sound/voice_person/room_1/35_need_diamond.wav', v_p_settings)
                                                p_e(next(g), t_settings)
                                                time.sleep(6.5) if not t_settings and v_p_settings else None
                                                continue
                                else:
                                    print(w(t_settings, v_a_settings))
                                    continue
                        else:
                            r_n(t_settings, v_p_settings, no_use)
                            time.sleep(1)
                        continue
                    elif option == '4':
                        if diamond_is_taken:
                            if glass_is_examined:
                                g = set_generator(95)
                                p_e(next(g), t_settings)
                                break
                            else:
                                g = set_generator(93)
                                s_e('../sound/voice_person/room_1/27_no_glass.wav', v_p_settings)
                                p_e(next(g), t_settings)
                                time.sleep(6) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                continue
                        else:
                            g = set_generator(98)
                            diamond_is_taken = True
                            s_e('../sound/voice_person/room_1/28_took_diamond.wav', v_p_settings)
                            p_e(next(g), t_settings)
                            time.sleep(16) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '5':
                        if diamond_is_taken:
                            s_e('../sound/s_es/close_chest.wav', s_settings)
                            time.sleep(1.5) if s_settings else None
                            break
                        else:
                            if glass_is_examined:
                                g = set_generator(100)
                                p_e(next(g), t_settings)
                                break
                            else:
                                g = set_generator(98)
                                s_e('../sound/voice_person/room_1/27_no_glass.wav', v_p_settings)
                                p_e(next(g), t_settings)
                                time.sleep(6) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                continue
                    elif option == '6':
                        if diamond_is_taken:
                            print(w(t_settings, v_a_settings))
                            continue
                        else:
                            s_e('../sound/s_es/close_chest.wav', s_settings)
                            time.sleep(1.5) if s_settings else None
                            break
                    elif option == '100':
                        q(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            continue
                        else:
                            print('Озвучивание опций отключено')
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
                    s_e('../sound/voice_person/room_1/17_chest_examined.wav', v_p_settings)
                    p_e(next(g), t_settings)
                    time.sleep(11) if not t_settings and v_p_settings else None
                    time.sleep(1)
        elif option == '3':
            if stonewall_is_examined:
                g = set_generator(95)
                p_e(next(g), t_settings)
                continue
            else:
                g = set_generator(45)
                stonewall_is_examined = True
                s_e('../sound/voice_person/room_1/18_stonewall_examined.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(12.5) if not t_settings and v_p_settings else None
                time.sleep(1)
                continue
        elif option == '4':
            if stone_moved:
                g = set_generator(100)
                s_e('../sound/voice_person/no_use_2.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(2.5) if not t_settings and v_p_settings else None
                continue
            else:
                """двигаем камень"""
                g = set_generator(48)
                stone_moved = True
                s_e('../sound/voice_person/room_1/19_stone_examined.wav', v_p_settings)
                p_e(next(g), t_settings)
                time.sleep(6.5) if not t_settings and v_p_settings else None
                time.sleep(1)
                while True:
                    g = set_generator(50)
                    print(f'1) {next(g)}'
                          f'2) {next(g)}' + '\n')
                    s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    record = s_e('../sound/voice_actions/room_1/13_stone_menu.wav', v_a_settings)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None
                    if option == '1':
                        g = set_generator(54)
                        s_e('../sound/s_es/move_stone.wav', s_settings)
                        time.sleep(6.5) if s_settings else None
                        if chest_is_examined:
                            s_e('../sound/voice_person/room_1/20_key_found.wav', v_p_settings)
                            p_e(next(g), t_settings)
                            time.sleep(3) if not t_settings and v_p_settings else None
                        else:
                            g = set_generator(56)
                            s_e('../sound/voice_person/room_1/57_unexpected_key.wav', v_p_settings)
                            p_e(next(g), t_settings)
                            time.sleep(5.5) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        while True:
                            g = set_generator(58)
                            print(f'1) {next(g)}' + '\n')
                            s_e('../sound/voice_actions/room_1/option.wav', v_a_settings)
                            time.sleep(2) if not t_settings and v_a_settings else None
                            record = s_e('../sound/voice_actions/room_1/17_open_chest_menu.wav', v_a_settings)
                            option = input('Введите цифру: ')
                            record.stop() if v_a_settings else None
                            if option == '1':
                                g = set_generator(59)
                                s_e('../sound/s_es/key.wav', s_settings)
                                time.sleep(2) if s_settings else None
                                s_e('../sound/voice_person/room_1/21_chest_opened.wav', v_p_settings)
                                p_e(next(g), t_settings)
                                time.sleep(6.5) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                chest_is_opened = True
                                break
                            elif option == '100':
                                q(t_settings, v_a_settings)
                                continue
                            elif option == '0':
                                if v_a_settings:
                                    continue
                                else:
                                    print('Озвучивание опций отключено')
                                    continue
                        break
                    elif option == '2':
                        break
                    elif option == '100':
                        q(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            continue
                        else:
                            print('Озвучивание опций отключено')
                            continue
                    else:
                        print(w(t_settings, v_a_settings))
                        continue
                continue
        else:
            print(w(t_settings, v_a_settings))
            continue
