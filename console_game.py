import time

import pygame.mixer
from colorama import Fore, Style
from sound_manager import room_1_mp3, room_2_mp3, dd_mp3
from read_scenario import prologue as p, room_1 as r_1, room_2 as r_2, \
    riddle, room_1_again as r_1_2, escape as e, epilogue as ep


# неверный ввод
def wrong_input(t_settings, v_a_settings):
    sound_effect('sound/voice_actions/wrong_input.wav', v_a_settings)
    time.sleep(5) if not t_settings and v_a_settings else None
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


# имитация чтения книги
def print_effect(text, t_settings):
    if t_settings:
        for i in text:
            time.sleep(0.07)
            print(i, end='', flush=True)
    else:
        print(text, end='')


# управление запуском звука
def sound_effect(sound_path, settings):
    if settings:
        record = pygame.mixer.Sound(sound_path)
        record.play()
    else:
        return


def quit_menu(t_settings, v_a_settings):
    print('Вы уверены, что хотите выйти из игры?' + '\n'
          '1) Да, выйти' + '\n'
          '2) Нет, остаться' + '\n')
    sound_effect('sound/voice_actions/quit_menu.wav', v_a_settings)
    time.sleep(13) if not t_settings and v_a_settings else None
    sound_effect('sound/voice_actions/option.wav', v_a_settings)
    time.sleep(2) if not t_settings and v_a_settings else None
    option = input('Введите цифру: ')
    while True:
        if option == '1':
            exit()
        elif option == '2':
            return
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue


# начало, вход
def start_game(t_settings, v_a_settings, v_p_settings):

    """перевод сценария в переменные"""
    start = p[0]
    prologue = p[2]
    intro_1 = p[3]
    intro_2 = p[4]
    intro_3 = p[5]
    intro_4 = p[6]
    intro_5 = p[7]
    begin = p[10]
    cave_entrance = p[12]
    entrance = p[13]

    """алгоритм"""
    sound_effect('sound/voice_actions/1_start.wav', v_a_settings)
    print(Fore.GREEN, f'{start}')
    print(Style.RESET_ALL)
    time.sleep(2) if v_a_settings else None
    sound_effect('sound/voice_actions/2_prologue.wav', v_a_settings)
    print(prologue)
    time.sleep(2)
    sound_effect('sound/voice_person/1_intro_1.wav', v_p_settings)
    print_effect(intro_1, t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/2_intro_2.wav', v_p_settings)
    print_effect(intro_2, t_settings)
    time.sleep(11) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/3_intro_3.wav', v_p_settings)
    print_effect(intro_3, t_settings)
    time.sleep(8) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/4_intro_4.wav', v_p_settings)
    print_effect(intro_4, t_settings)
    time.sleep(5) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/5_intro_5.wav', v_p_settings)
    print_effect(intro_5 + '\n', t_settings)
    time.sleep(6) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/6_begin.wav', v_p_settings)
    print_effect(begin + '\n', t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    time.sleep(2)
    print(cave_entrance)
    sound_effect('sound/voice_actions/3_cave_entrance.wav', v_a_settings)
    time.sleep(2) if not t_settings and v_a_settings else None
    sound_effect('sound/voice_person/7_entrance.wav', v_p_settings)
    print_effect(entrance + '\n', t_settings)
    time.sleep(7) if not t_settings and v_p_settings else None
    time.sleep(2)


def room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, book_found):

    """перевод сценария в переменные"""
    begin = r_1_2[177]
    glass = r_1_2[182]
    pouring_potion = r_1_2[185]
    result_1 = r_1_2[187]
    result_2 = r_1_2[188]
    result_3 = r_1_2[189]
    result_4 = r_1_2[190]
    start_experiment = r_1_2[193]
    paper_in_glass = r_1_2[197]
    need_to_think = r_1_2[200]
    no_effect = r_1_2[203]
    of_course = r_1_2[206]
    effect_1 = r_1_2[207]
    effect_2 = r_1_2[208]
    effect_3 = r_1_2[209]
    coin_stuck = r_1_2[212]
    bowl_effect = r_1_2[214]
    bowl_destiny_1 = r_1_2[215]
    bowl_destiny_2 = r_1_2[216]
    read_paper = r_1_2[218]
    paper_1 = r_1_2[220]
    paper_2 = r_1_2[221]
    paper_3 = r_1_2[222]
    paper_4 = r_1_2[223]
    paper_5 = r_1_2[224]
    paper_6 = r_1_2[225]
    paper_7 = r_1_2[227]
    paper_8 = r_1_2[228]
    so_cool = r_1_2[230]
    lets_get_out = r_1_2[231]
    rope = r_1_2[234]
    sledgehammer = r_1_2[236]
    get_out = r_1_2[239]

    to_room_2 = r_1_2[0]
    open_chest = r_1_2[53]
    close_chest = r_1_2[61]
    no_use = r_1_2[73]
    get_rope = r_1_2[179]
    get_sledgehammer = r_1_2[180]
    get_glass = r_1_2[181]
    pour_potion = r_1_2[184]
    burn_paper = r_1_2[192]
    put_paper = r_1_2[196]
    put_glass = r_1_2[199]
    normal = r_1_2[202]
    upside_down = r_1_2[205]
    get_coin = r_1_2[211]

    """алгоритм"""
    book_found = book_found
    print_effect(begin, t_settings)
    glass_taken = False
    while True:
        if glass_taken:
            break
        else:
            print(f'1) {open_chest}' + '\n')
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                sound_effect('sound/voice_actions/6_menu_1.wav', v_a_settings)
                time.sleep(13) if not t_settings and v_a_settings else None
                while True:
                    print(f'1) {get_glass}'
                          f'2) {get_rope}'
                          f'3) {get_sledgehammer}'
                          f'4) {close_chest}'
                          f'5) {to_room_2}' + '\n')
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '100':
                        quit_menu(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            sound_effect('sound/voice_actions/6_menu_1.wav', v_a_settings)
                            time.sleep(13) if not t_settings else None
                            continue
                        else:
                            print('Озвучивание опций отключено')
                            continue
                    elif option == '1':
                        if book_found:
                            glass_taken = True
                            print_effect(glass, t_settings)
                            time.sleep(1)
                            continue
                        else:
                            print_effect(no_use, t_settings)
                            time.sleep(1)
                            continue
                    elif option == '2' or option == '3':
                        print_effect(no_use, t_settings)
                        time.sleep(1)
                        continue
                    elif option == '4':
                        break
                    else:
                        print(wrong_input(t_settings, v_a_settings))
                        continue
            else:
                print(wrong_input(t_settings, v_a_settings))
                continue

    """разбираемся с зельем"""
    while True:
        print(f'1) {pour_potion}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '100':
            quit_menu(t_settings, v_a_settings)
            continue
        elif option == '0':
            if v_a_settings:
                sound_effect('sound/voice_actions/6_menu_1.wav', v_a_settings)
                time.sleep(13) if not t_settings else None
                continue
            else:
                print('Озвучивание опций отключено')
                continue
        elif option == '1':
            print_effect(pouring_potion, t_settings)
            time.sleep(2)
            print_effect(result_1, t_settings)
            time.sleep(1)
            print_effect(result_2, t_settings)
            time.sleep(1)
            print_effect(result_3, t_settings)
            time.sleep(1)
            print_effect(result_4, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {burn_paper}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(start_experiment, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {put_paper}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(paper_in_glass, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    bowl_ready = False
    mistake_made = False
    while True:
        if bowl_ready:
            break
        else:
            print(f'1) {put_glass}' + '\n')
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                print_effect(need_to_think, t_settings)
                time.sleep(1)
                while True:
                    print(f'1) {normal}'
                          f'2) {upside_down}' + '\n')
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '1':
                        mistake_made = True
                        print_effect(no_effect, t_settings)
                        time.sleep(1)
                        continue
                    elif option == '2':
                        bowl_ready = True
                        if mistake_made:
                            print_effect(of_course, t_settings)
                            time.sleep(1)
                        print_effect(effect_1, t_settings)
                        time.sleep(1)
                        print_effect(effect_2, t_settings)
                        time.sleep(1)
                        print_effect(effect_3, t_settings)
                        time.sleep(1)
                        break
            else:
                print(wrong_input(t_settings, v_a_settings))
                continue
    while True:
        print(f'1) {get_coin}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(coin_stuck, t_settings)
            time.sleep(1)
            print_effect(bowl_effect, t_settings)
            time.sleep(1)
            print_effect(bowl_destiny_1, t_settings)
            time.sleep(1)
            print_effect(bowl_destiny_2, t_settings)
            time.sleep(1)
            print_effect(read_paper, t_settings)
            time.sleep(2)
            print_effect(paper_1, t_settings)
            time.sleep(1)
            print_effect(paper_2, t_settings)
            print_effect(paper_3, t_settings)
            time.sleep(1)
            print_effect(paper_4, t_settings)
            print_effect(paper_5, t_settings)
            print_effect(paper_6 + '\n', t_settings)
            time.sleep(2)
            print_effect(paper_7, t_settings)
            time.sleep(1)
            print_effect(paper_8 + '\n', t_settings)
            time.sleep(2)
            print_effect(so_cool, t_settings)
            time.sleep(1)
            print_effect(lets_get_out, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    """забираем всё из сундука"""
    rope_taken = False
    sledgehammer_taken = False
    print(f'1) {open_chest}' + '\n')
    sound_effect('sound/voice_actions/option.wav', v_a_settings)
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
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '1':
                        rope_taken = True
                        print_effect(rope, t_settings)
                        time.sleep(1)
                        continue
                    elif option == '2':
                        sledgehammer_taken = True
                        print_effect(sledgehammer, t_settings)
                        time.sleep(1)
                        continue
                    else:
                        print(wrong_input(t_settings, v_a_settings))
                        continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

        """уходим"""
        while True:
            print(f'1) {get_out}' + '\n')
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                return
            else:
                print(wrong_input(t_settings, v_a_settings))
                continue


# главный зал
def room_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    """перевод сценария в переменные"""
    enter_1 = r_1[1]
    enter_2 = r_1[2]
    enter_3 = r_1[3]
    room_examined = r_1[6]
    bowl_examined_1 = r_1[14]
    bowl_examined_2 = r_1[15]
    painful_death = r_1[22]
    the_end = r_1[23]
    bowl_not_lifted = r_1[34]
    chest_examined = r_1[37]
    stonewall_examined = r_1[40]
    stone_examined = r_1[43]
    key_found = r_1[49]
    chest_opened = r_1[52]
    need_to_think = r_1[61]
    twig_attempt = r_1[69]
    twig_failure_1 = r_1[71]
    twig_failure_2 = r_1[72]
    no_use = r_1[75]
    no_glass = r_1[78]
    enough_watching = r_1[80]
    took_diamond = r_1[83]
    lets_smash = r_1[92]
    rattle = r_1[94]
    wall_smashed = r_1[95]
    rattle_intensifies = r_1[96]
    something_wrong = r_1[97]
    trapped_1 = r_1[100]
    trapped_2 = r_1[101]
    trapped_3 = r_1[102]
    decision = r_1[105]
    last_hope = r_1[108]

    room_1_location = r_1[0]
    look_around = r_1[5]
    examine_bowl = r_1[8]
    examine_chest = r_1[9]
    examine_stonewall = r_1[10]
    examine_stone = r_1[11]
    get_coin = r_1[17]
    game_over = r_1[24]
    death_menu = r_1[25]
    load_game = r_1[27]
    exit_game = r_1[28]
    game_resume = r_1[31]
    lift_bowl = r_1[18]
    leave_bowl = r_1[19]
    move_stone = r_1[45]
    leave_stone = r_1[46]
    open_chest = r_1[51]
    twig = r_1[54]
    rope = r_1[55]
    sledgehammer = r_1[56]
    diamond = r_1[57]
    glass = r_1[58]
    close_chest = r_1[59]
    get_coin_twig = r_1[65]
    get_twig_away = r_1[66]
    acid_hiss = r_1[70]
    smash_the_wall = r_1[90]
    run_away = r_1[99]
    return_to_room_1 = r_1[104]
    to_room_2 = r_1[107]
    another_location = r_1[109]

    """алгоритм"""
    stone_moved = False
    chest_is_examined = False
    chest_is_opened = False
    stonewall_is_examined = False
    glass_is_examined = False
    diamond_is_taken = False
    twig_melted = False
    print(room_1_location)
    sound_effect('sound/voice_actions/4_room_1.wav', v_a_settings)
    time.sleep(2)
    sound_effect('sound/voice_person/8_enter_1.wav', v_p_settings)
    print_effect(enter_1, t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/9_enter_2.wav', v_p_settings)
    print_effect(enter_2, t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/10_enter_3.wav', v_p_settings)
    print_effect(enter_3, t_settings)
    time.sleep(2) if not t_settings and v_p_settings else None
    time.sleep(2)

    """осматриваемся"""
    while True:
        print(f'1) {look_around}')
        sound_effect('sound/voice_actions/5_look_around.wav', v_a_settings)
        time.sleep(3) if not t_settings and v_a_settings else None
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
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
            sound_effect('sound/voice_person/11_room_examined.wav', v_p_settings)
            print_effect(room_examined, t_settings)
            time.sleep(8) if not t_settings and v_p_settings else None
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    while True:
        if chest_is_opened:
            print(f'1) {examine_bowl}'
                  f'2) {open_chest}'
                  f'3) {examine_stonewall}'
                  f'4) {examine_stone}' + '\n')
            sound_effect('sound/voice_actions/12_menu_2.wav', v_a_settings)
            time.sleep(13.5) if not t_settings and v_a_settings else None
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
        else:
            print(f'1) {examine_bowl}'
                  f'2) {examine_chest}'
                  f'3) {examine_stonewall}'
                  f'4) {examine_stone}' + '\n')
            sound_effect('sound/voice_actions/6_menu_1.wav', v_a_settings)
            time.sleep(13) if not t_settings and v_a_settings else None
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
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
            sound_effect('sound/voice_person/12_bowl_examined_1.wav', v_p_settings)
            print_effect(bowl_examined_1, t_settings)
            time.sleep(17) if not t_settings and v_p_settings else None
            time.sleep(1)
            sound_effect('sound/voice_person/13_bowl_examined_2.wav', v_p_settings)
            print_effect(bowl_examined_2, t_settings)
            time.sleep(6) if not t_settings and v_p_settings else None
            time.sleep(2)

            """осматриваем чашу"""
            while True:
                print(f'1) {get_coin}'
                      f'2) {lift_bowl}'
                      f'3) {leave_bowl}' + '\n')
                sound_effect('sound/voice_actions/7_bowl_options.wav', v_a_settings)
                time.sleep(10) if not t_settings and v_a_settings else None
                sound_effect('sound/voice_actions/option.wav', v_a_settings)
                time.sleep(2) if not t_settings and v_a_settings else None
                option = input('Введите цифру: ')

                """смерть"""
                if option == '1':
                    while True:
                        room_1_mp3.stop() if m_settings else None
                        sound_effect('sound/sound_effects/death.wav', s_settings)
                        time.sleep(1) if s_settings else None
                        dd_mp3.set_volume(0.2) if m_settings else None
                        dd_mp3.play(-1) if m_settings else None
                        sound_effect('sound/voice_person/14_painful_death.wav', v_p_settings)
                        print_effect(painful_death, t_settings)
                        time.sleep(10) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        sound_effect('sound/voice_person/15_the_end.wav', v_p_settings)
                        print_effect(the_end, t_settings)
                        print('')
                        time.sleep(9) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        print(Fore.RED, f'{game_over}')
                        print(Style.RESET_ALL)
                        print(death_menu)
                        print(f'1) {load_game}'
                              f'2) {exit_game}' + '\n')
                        sound_effect('sound/voice_actions/10_death_menu.wav', v_a_settings)
                        time.sleep(13) if not t_settings and v_a_settings else None
                        sound_effect('sound/voice_actions/option.wav', v_a_settings)
                        time.sleep(2) if not t_settings and v_a_settings else None
                        option = input(f'Введите цифру: ')
                        if option == '1':
                            dd_mp3.stop() if m_settings else None
                            room_1_mp3.play(-1) if m_settings else None
                            sound_effect('sound/voice_actions/11_game_resume.wav', v_a_settings)
                            time.sleep(2.5) if not t_settings and v_a_settings else None
                            print(Fore.YELLOW, f'{game_resume}')
                            print(Style.RESET_ALL)
                            break
                        elif option == '2':

                            """конец игры"""
                            exit()
                        else:
                            print(wrong_input(t_settings, v_a_settings))
                            continue
                    continue
                elif option == '2':
                    sound_effect('sound/voice_person/16_bowl_not_lifted.wav', v_p_settings)
                    print_effect(bowl_not_lifted, t_settings)
                    time.sleep(9) if not t_settings and v_p_settings else None
                    time.sleep(1)
                    continue
                elif option == '3':
                    break
                elif option == '100':
                    quit_menu(t_settings, v_a_settings)
                    continue
                elif option == '0':
                    if v_a_settings:
                        continue
                    else:
                        print('Озвучивание опций отключено')
                        continue
                else:
                    print(wrong_input(t_settings, v_a_settings))
                    continue
        elif option == '2':

            """открываем сундук"""
            if chest_is_opened:
                sound_effect('sound/sound_effects/open_chest.wav', s_settings)
                time.sleep(1.5) if s_settings else None
                sound_effect('sound/voice_person/22_need_to_think.wav', v_p_settings)
                print_effect(need_to_think, t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                time.sleep(1)
                while True:
                    print(f'1) {twig}'
                          f'2) {rope}'                  
                          f'3) {sledgehammer}'
                          f'4) {diamond}'
                          f'5) {glass}'
                          f'6) {close_chest}' + '\n')
                    sound_effect('sound/voice_actions/8_chest_inside.wav', v_a_settings)
                    time.sleep(20.5) if not t_settings and v_a_settings else None
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')

                    if option == '1':

                        """используем прут"""
                        while True:
                            if twig_melted:
                                print_effect(enough_watching, t_settings)
                                break
                            else:
                                print(f'1) {get_coin_twig}'
                                      f'2) {get_twig_away}' + '\n')
                                sound_effect('sound/voice_actions/9_twig_options.wav', v_a_settings)
                                time.sleep(7.5) if not t_settings and v_a_settings else None
                                sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                time.sleep(2) if not t_settings and v_a_settings else None
                                option = input('Введите цифру: ')
                                if option == '1':
                                    twig_melted = True
                                    sound_effect('sound/voice_person/23_twig_attempt.wav', v_p_settings)
                                    print_effect(twig_attempt, t_settings)
                                    time.sleep(1.5) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    print(acid_hiss)
                                    sound_effect('sound/sound_effects/acid_hiss.wav', s_settings)
                                    time.sleep(2.5) if s_settings else None
                                    time.sleep(1)
                                    sound_effect('sound/voice_person/24_twig_failure_1.wav', v_p_settings)
                                    print_effect(twig_failure_1, t_settings)
                                    time.sleep(10) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    sound_effect('sound/voice_person/25_twig_failure_2.wav', v_p_settings)
                                    print_effect(twig_failure_2, t_settings)
                                    time.sleep(15) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    break
                                elif option == '2':
                                    break
                                elif option == '100':
                                    quit_menu(t_settings, v_a_settings)
                                    continue
                                elif option == '0':
                                    if v_a_settings:
                                        continue
                                    else:
                                        print('Озвучивание опций отключено')
                                        continue
                                else:
                                    print(wrong_input(t_settings, v_a_settings))
                                    continue
                    elif option == '2':
                        sound_effect('sound/voice_person/26_no_use.wav', v_p_settings)
                        print_effect(no_use, t_settings)
                        time.sleep(4) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        continue
                    elif option == '3':
                        if stonewall_is_examined:

                            """разбиваем стену"""
                            while True:
                                print(f'1) {smash_the_wall}' + '\n')
                                sound_effect('sound/voice_actions/14_smash_menu.wav', v_a_settings)
                                time.sleep(3.5) if not t_settings and v_a_settings else None
                                sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                time.sleep(2) if not t_settings and v_a_settings else None
                                option = input('Введите цифру: ')
                                if option == '1':
                                    sound_effect('sound/voice_person/29_lets_smash.wav', v_p_settings)
                                    print_effect(lets_smash, t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    print(rattle)
                                    sound_effect('sound/sound_effects/wall_smashed.wav', s_settings)
                                    time.sleep(8) if s_settings else None
                                    print_effect(wall_smashed, t_settings)
                                    time.sleep(3) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    print(rattle_intensifies)
                                    sound_effect('sound/sound_effects/stones.wav', s_settings)
                                    time.sleep(1) if s_settings else None
                                    sound_effect('sound/sound_effects/giant_stone.wav', s_settings)
                                    time.sleep(7) if s_settings else None
                                    sound_effect('sound/voice_person/30_wall_smashed.wav', v_p_settings)
                                    print_effect(something_wrong, t_settings)
                                    time.sleep(4) if not t_settings and v_p_settings else None
                                    time.sleep(2)

                                    """обвал"""
                                    print(run_away)
                                    room_1_mp3.stop() if m_settings else None
                                    dd_mp3.set_volume(0.2) if m_settings else None
                                    dd_mp3.play(-1) if m_settings else None
                                    sound_effect('sound/voice_person/31_trapped_1.wav', v_p_settings)
                                    print_effect(trapped_1, t_settings)
                                    time.sleep(4) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    sound_effect('sound/voice_person/32_trapped_2.wav', v_p_settings)
                                    print_effect(trapped_2, t_settings)
                                    time.sleep(12) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    sound_effect('sound/voice_person/32_trapped_2.wav', v_p_settings)
                                    print_effect(trapped_3, t_settings)
                                    time.sleep(6) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    print(return_to_room_1)
                                    dd_mp3.stop() if m_settings else None
                                    room_1_mp3.play(-1) if m_settings else None
                                    sound_effect('sound/voice_person/34_decision.wav', v_p_settings)
                                    print_effect(decision, t_settings)
                                    time.sleep(16) if not t_settings and v_p_settings else None
                                    time.sleep(2)

                                    """принимаем решение"""
                                    while True:
                                        print(f'1) {open_chest}'
                                              f'2) {to_room_2}')
                                        sound_effect('sound/voice_actions/16_final_menu.wav', v_a_settings)
                                        time.sleep(6.5) if not t_settings and v_a_settings else None
                                        sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                        time.sleep(2) if not t_settings and v_a_settings else None
                                        option = input('Введите цифру: ')
                                        if option == '1':
                                            sound_effect('sound/sound_effects/open_chest.wav', s_settings)
                                            time.sleep(1.5) if s_settings else None
                                            while True:
                                                if diamond_is_taken:
                                                    print(f'1) {rope}'
                                                          f'2) {glass}'
                                                          f'3) {close_chest}')
                                                    sound_effect('sound/voice_actions/18_fm_2.wav', v_a_settings)
                                                    time.sleep(9.5) if not t_settings and v_a_settings else None
                                                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                                    time.sleep(2) if not t_settings and v_a_settings else None
                                                    option = input('Введите цифру: ')
                                                    if option == '1':
                                                        print_effect(no_use, t_settings)
                                                        continue
                                                    elif option == '2':
                                                        print_effect(enough_watching, t_settings)
                                                        continue
                                                    elif option == '3':
                                                        sound_effect('sound/sound_effects/close_chest.wav', s_settings)
                                                        time.sleep(1.5) if s_settings else None
                                                        break
                                                    elif option == '100':
                                                        quit_menu(t_settings, v_a_settings)
                                                        continue
                                                    elif option == '0':
                                                        if v_a_settings:
                                                            continue
                                                        else:
                                                            print('Озвучивание опций отключено')
                                                            continue
                                                    else:
                                                        print(wrong_input(t_settings, v_a_settings))
                                                        continue
                                                else:
                                                    print(f'1) {rope}'
                                                          f'2) {glass}'
                                                          f'3) {diamond}'
                                                          f'4) {close_chest}')
                                                    sound_effect('sound/voice_actions/19_fm_3.wav', v_a_settings)
                                                    time.sleep(13) if not t_settings and v_a_settings else None
                                                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                                    time.sleep(2) if not t_settings and v_a_settings else None
                                                    option = input('Введите цифру: ')
                                                    if option == '1':
                                                        print_effect(no_use, t_settings)
                                                        continue
                                                    elif option == '2':
                                                        print_effect(enough_watching, t_settings)
                                                        continue
                                                    elif option == '3':
                                                        diamond_is_taken = True
                                                        sound_effect('sound/voice_person/28_took_diamond.wav',
                                                                     v_p_settings)
                                                        print_effect(took_diamond, t_settings)
                                                        time.sleep(16) if not t_settings and v_p_settings else None
                                                        time.sleep(1)
                                                        continue
                                                    elif option == '4':
                                                        sound_effect('sound/sound_effects/close_chest.wav', s_settings)
                                                        time.sleep(1.5) if s_settings else None
                                                        break
                                                    elif option == '100':
                                                        quit_menu(t_settings, v_a_settings)
                                                        continue
                                                    elif option == '0':
                                                        if v_a_settings:
                                                            continue
                                                        else:
                                                            print('Озвучивание опций отключено')
                                                            continue
                                                    else:
                                                        print(wrong_input(t_settings, v_a_settings))
                                                        continue

                                        elif option == '2':
                                            sound_effect('sound/voice_person/35_last_hope.wav', v_p_settings)
                                            print_effect(last_hope, t_settings)
                                            time.sleep(4) if not t_settings and v_p_settings else None
                                            time.sleep(2)
                                            print(another_location)
                                            return
                                else:
                                    print(wrong_input(t_settings, v_a_settings))
                                    continue
                        else:
                            sound_effect('sound/voice_person/26_no_use.wav', v_p_settings)
                            print_effect(no_use, t_settings)
                            time.sleep(4) if not t_settings and v_p_settings else None
                            time.sleep(1)
                        continue
                    elif option == '4':
                        if diamond_is_taken:
                            print_effect(enough_watching, t_settings)
                            continue
                        else:
                            diamond_is_taken = True
                            sound_effect('sound/voice_person/28_took_diamond.wav', v_p_settings)
                            print_effect(took_diamond, t_settings)
                            time.sleep(16) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '5':
                        if glass_is_examined:
                            print_effect(enough_watching, t_settings)
                            break
                        else:
                            sound_effect('sound/voice_person/27_no_glass.wav', v_p_settings)
                            print_effect(no_glass, t_settings)
                            time.sleep(6) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '6':
                        sound_effect('sound/sound_effects/close_chest.wav', s_settings)
                        time.sleep(1.5) if s_settings else None
                        break
                    elif option == '100':
                        quit_menu(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            continue
                        else:
                            print('Озвучивание опций отключено')
                            continue
                    else:
                        print(wrong_input(t_settings, v_a_settings))
                        continue
            else:
                if chest_is_examined:
                    print_effect(enough_watching, t_settings)
                    continue
                else:
                    chest_is_examined = True
                    sound_effect('sound/voice_person/17_chest_examined.wav', v_p_settings)
                    print_effect(chest_examined, t_settings)
                    time.sleep(11) if not t_settings and v_p_settings else None
                    time.sleep(1)
        elif option == '3':
            if stonewall_is_examined:
                print_effect(enough_watching, t_settings)
                continue
            else:
                stonewall_is_examined = True
                sound_effect('sound/voice_person/18_stonewall_examined.wav', v_p_settings)
                print_effect(stonewall_examined, t_settings)
                time.sleep(12.5) if not t_settings and v_p_settings else None
                time.sleep(1)
                continue
        elif option == '4':
            if stone_moved:
                sound_effect('sound/voice_person/26_no_use.wav', v_p_settings)
                time.sleep(5) if not t_settings and v_p_settings else None
                continue
            else:
                """двигаем камень"""
                sound_effect('sound/voice_person/19_stone_examined.wav', v_p_settings)
                print_effect(stone_examined, t_settings)
                time.sleep(6.5) if not t_settings and v_p_settings else None
                time.sleep(1)
                while True:
                    print(f'1) {move_stone}'
                          f'2) {leave_stone}' + '\n')
                    sound_effect('sound/voice_actions/13_stone_menu.wav', v_a_settings)
                    time.sleep(6.5) if not t_settings and v_a_settings else None
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    option = input('Введите цифру: ')
                    if option == '1':
                        sound_effect('sound/sound_effects/move_stone.wav', s_settings)
                        time.sleep(6.5) if s_settings else None
                        sound_effect('sound/voice_person/20_key_found.wav', v_p_settings)
                        print_effect(key_found, t_settings)
                        time.sleep(3) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        while True:
                            print(f'1) {open_chest}' + '\n')
                            sound_effect('sound/voice_actions/17_open_chest_menu.wav', v_a_settings)
                            time.sleep(2) if not t_settings and v_a_settings else None
                            sound_effect('sound/voice_actions/option.wav', v_a_settings)
                            time.sleep(2) if not t_settings and v_a_settings else None
                            option = input('Введите цифру: ')
                            if option == '1':
                                sound_effect('sound/sound_effects/key.wav', s_settings)
                                time.sleep(2) if s_settings else None
                                sound_effect('sound/voice_person/21_chest_opened.wav', v_p_settings)
                                print_effect(chest_opened, t_settings)
                                time.sleep(6.5) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                chest_is_opened = True
                                break
                            elif option == '100':
                                quit_menu(t_settings, v_a_settings)
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
                        quit_menu(t_settings, v_a_settings)
                        continue
                    elif option == '0':
                        if v_a_settings:
                            continue
                        else:
                            print('Озвучивание опций отключено')
                            continue
                    else:
                        print(wrong_input(t_settings, v_a_settings))
                        continue
                continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue


# рабочий кабинет
def room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    """перевод сценария в переменные"""
    look_around_1 = r_2[105]
    look_around_2 = r_2[106]
    table_examined_1 = r_2[109]
    table_examined_2 = r_2[110]
    shelf_1 = r_2[113]
    shelf_2 = r_2[116]
    shelf_3 = r_2[119]
    shelves_examined = r_2[120]
    candle_lightened = r_2[123]
    no_light = r_2[127]
    mechanism_examined_1 = r_2[130]
    mechanism_examined_2 = r_2[131]
    begin_reading = r_2[134]
    line_1 = r_2[135]
    line_2 = r_2[136]
    line_3 = r_2[138]
    line_4 = r_2[139]
    need_to_think = r_2[141]
    why_religion = r_2[142]
    back_to_business = r_2[143]
    stone_inserted = r_2[146]
    diamond_correct = r_2[148]
    great_diamond = r_2[149]
    follow_the_light = r_2[150]
    storage_found = r_2[153]
    storage_opened = r_2[156]
    read_1 = r_2[159]
    read_2 = r_2[160]
    book_1 = r_2[162]
    book_2 = r_2[163]
    book_3 = r_2[164]
    book_4 = r_2[165]
    book_5 = r_2[166]
    book_6 = r_2[167]
    book_7 = r_2[168]
    book_8 = r_2[169]
    book_9 = r_2[170]
    conclusion = r_2[172]
    get_tools = r_2[173]
    get_away = r_2[174]

    entry = r_2[104]
    examine_the_table = r_2[108]
    open_shelf_1 = r_2[112]
    open_shelf_2 = r_2[115]
    open_shelf_3 = r_2[118]
    light_candle = r_2[122]
    examine_mechanism = r_2[129]
    read_papers = r_2[133]
    insert_stone = r_2[145]
    knock_the_wall = r_2[152]
    hit_the_wall = r_2[155]
    read_book = r_2[158]
    leave_location = r_2[176]

    """алгоритм"""
    room_2_mp3.play(-1) if m_settings else None
    print(entry)
    time.sleep(1)
    print_effect(look_around_1, t_settings)
    time.sleep(1)
    print_effect(look_around_2, t_settings)
    time.sleep(1)

    """осматриваем стол"""
    while True:
        print(f'1) {examine_the_table}')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(table_examined_1, t_settings)
            time.sleep(1)
            print_effect(table_examined_2, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    open_1 = False
    open_2 = False
    open_3 = False

    """проверяем полки"""
    while True:
        if open_1 is True and open_2 is True and open_3 is True:
            print_effect(shelves_examined, t_settings)
            break
        else:
            print(f'1) {open_shelf_1}'
                  f'2) {open_shelf_2}'
                  f'3) {open_shelf_3}' + '\n')
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                open_1 = True
                print_effect(shelf_1, t_settings)
                time.sleep(1)
                continue
            elif option == '2':
                open_2 = True
                print_effect(shelf_2, t_settings)
                time.sleep(1)
                continue
            elif option == '3':
                open_3 = True
                print_effect(shelf_3, t_settings)
                time.sleep(1)
                continue
            else:
                print(wrong_input(t_settings, v_a_settings))
                continue

    """головоломка со светом"""
    light_on = False
    papers_read = False
    mechanism_examined = False
    while True:
        if papers_read and mechanism_examined:
            break
        else:
            print(f'1) {read_papers}'
                  f'2) {examine_mechanism}'
                  f'3) {light_candle}' + '\n')
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            if option == '1':
                if light_on is True:
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
                else:
                    print_effect(no_light, t_settings)
                    time.sleep(1)
                    continue
            elif option == '2':
                if light_on is True:
                    mechanism_examined = True
                    print_effect(mechanism_examined_1, t_settings)
                    time.sleep(1)
                    print_effect(mechanism_examined_2, t_settings)
                    time.sleep(1)
                    continue
                else:
                    print_effect(no_light, t_settings)
                    time.sleep(1)
                    continue
            elif option == '3':
                if light_on:
                    print('Свеча уже горит')
                    continue
                else:
                    light_on = True
                    print_effect(candle_lightened, t_settings)
                    time.sleep(1)
                    continue
            else:
                print(wrong_input(t_settings, v_a_settings))
                continue

    """вставляем камень в оправу"""
    while True:
        print(f'1) {insert_stone}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(stone_inserted, t_settings)
            time.sleep(2)
            print_effect(diamond_correct, t_settings)
            time.sleep(1)
            print_effect(great_diamond, t_settings)
            time.sleep(1)
            print_effect(follow_the_light, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))

    """обнаруживаем тайник"""
    while True:
        print(f'1) {knock_the_wall}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(storage_found, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
    while True:
        print(f'1) {hit_the_wall}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(storage_opened, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))

    """читаем записку"""
    while True:
        print(f'1) {read_book}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(read_1, t_settings)
            time.sleep(1)
            print_effect(read_2 + '\n', t_settings)
            time.sleep(2)
            print_effect(book_1, t_settings)
            print_effect(book_2, t_settings)
            print_effect(book_3, t_settings)
            print_effect(book_4, t_settings)
            print_effect(book_5, t_settings)
            print_effect(book_6, t_settings)
            print_effect(book_7, t_settings)
            print_effect(book_8, t_settings)
            print_effect(book_9 + '\n', t_settings)
            time.sleep(2)
            print_effect(conclusion, t_settings)
            time.sleep(2)
            print_effect(get_tools, t_settings)
            time.sleep(1)
            print_effect(get_away + '\n', t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))

    """уходим"""
    while True:
        print(f'1) {leave_location}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            return
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue


def final_location(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):

    """перевод сценария в переменные"""
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
    print_effect(need_to_think, t_settings)
    time.sleep(1)
    while True:
        print(f'1) {smash_wall}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(cant_smash, t_settings)
            time.sleep(2)
            print_effect(lets_pray, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    """молитва и побег"""
    while True:
        print(f'1) {pray}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(prayer_1, t_settings)
            time.sleep(2)
            print_effect(prayer_2, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {through_sledgehammer}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            time.sleep(1)
            print_effect(hole, t_settings)
            time.sleep(2)
            print_effect(lets_go, t_settings)
            time.sleep(1)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue
    while True:
        print(f'1) {escape}' + '\n')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        option = input('Введите цифру: ')
        if option == '1':
            time.sleep(1)
            print_effect(dots, t_settings)
            time.sleep(1)
            print_effect(final, t_settings)
            room_1_mp3.fadeout(2000) if m_settings else None
            time.sleep(1)
            time.sleep(2)
            break
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    """ЭПИЛОГ"""
    room_2_mp3.play() if m_settings else None
    print(epilogue)
    time.sleep(2)
    print_effect(epilogue_1, t_settings)
    time.sleep(2)
    print_effect(epilogue_2, t_settings)
    time.sleep(2)
    print_effect(epilogue_3, t_settings)
    time.sleep(2)
    print_effect(epilogue_4 + '\n', t_settings)
    time.sleep(2)
    print_effect(epilogue_5 + '\n', t_settings)
    time.sleep(2)
    room_2_mp3.fadeout(3000) if m_settings else None
    print_effect(thanks, t_settings)
    time.sleep(1)
    print_effect(good_luck, t_settings)
    time.sleep(1)
    print(Fore.GREEN, end_game)
    print(Style.RESET_ALL)
    time.sleep(2)
    return


# запуск игры в консоли
def run_game_console(t_settings, v_a_settings, v_p_settings, m_settings, s_settings):
    room_1_mp3.set_volume(0.2) if m_settings else None
    room_1_mp3.play(-1) if m_settings else None
    start_game(t_settings, v_a_settings, v_p_settings)
    room_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    # room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    # room_1_mp3.play(-1) if m_settings else None
    # room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    # final_location(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
