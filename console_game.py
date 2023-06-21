import time
import random

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


def numbers_check(num_list):
    message = 'Ввод должен состоять из четырёх разных цифр. Попробуйте снова!'

    """проверяем состав ввода"""
    if len(num_list) != '4':
        print(message)
        time.sleep(1)
        return

    """проверяем состав ввода"""
    good_list = [1, 2, 3, 4]
    for i in num_list:
        if i.isnumeric():
            if int(i) not in good_list:
                print(message)
                time.sleep(1)
                return
        else:
            print(message)
            time.sleep(1)
            return

    """проверяем уникальность чисел"""
    if len(set(num_list)) != len(num_list):
        print(message)
        time.sleep(1)
        return
    else:
        return True


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
        return record
    else:
        return


def quit_menu(t_settings, v_a_settings):
    sound_effect('sound/voice_actions/option.wav', v_a_settings)
    time.sleep(2) if not t_settings and v_a_settings else None
    print('Вы уверены, что хотите выйти из игры?' + '\n'
          '1) Да, выйти' + '\n'
          '2) Нет, остаться' + '\n')
    record = sound_effect('sound/voice_actions/quit_menu.wav', v_a_settings)
    option = input('Введите цифру: ')
    record.stop() if v_a_settings else None
    while True:
        if option == '1':
            exit()
        elif option == '2':
            return
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue


def random_no(t_settings, v_p_settings, no_use):
    choose_no_use = random.choice(no_use)
    if choose_no_use == r_1[119]:
        sound_effect('sound/voice_person/no_use.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(4) if not t_settings and v_p_settings else None
    elif choose_no_use == r_1[120]:
        sound_effect('sound/voice_person/no_use_2.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2.5) if not t_settings and v_p_settings else None
    elif choose_no_use == r_1[121]:
        sound_effect('sound/voice_person/no_use_3.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    elif choose_no_use == r_1[122]:
        sound_effect('sound/voice_person/no_use_4.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(2) if not t_settings and v_p_settings else None
    else:
        sound_effect('sound/voice_person/no_use_5.wav', v_p_settings)
        print_effect(choose_no_use, t_settings)
        time.sleep(3) if not t_settings and v_p_settings else None
    return


def random_wont_open(t_settings, v_p_settings, wont_open_list):
    choice = random.choice(wont_open_list)
    if choice == r_2[226]:
        print_effect(choice, t_settings)
    elif choice == r_2[227]:
        print_effect(choice, t_settings)
    else:
        print_effect(choice, t_settings)
    return


def random_try(t_settings, v_p_settings, tries):
    choice = random.choice(tries)
    if choice == r_2[107]:
        print_effect(choice, t_settings)
    elif choice == r_2[108]:
        print_effect(choice, t_settings)
    elif choice == r_2[109]:
        print_effect(choice, t_settings)
    else:
        print_effect(choice, t_settings)
    return


def random_failure(t_settings, v_p_settings, failures):
    choice = random.choice(failures)
    if choice == r_2[116]:
        print_effect(choice, t_settings)
    elif choice == r_2[117]:
        print_effect(choice, t_settings)
    elif choice == r_2[118]:
        print_effect(choice, t_settings)
    else:
        print_effect(choice, t_settings)
    return


def random_open_shelf(t_settings, v_p_settings, open_shelf_again):
    choose_reaction = random.choice(open_shelf_again)
    print_effect(choose_reaction, t_settings)
    return


# начало, вход
def start_game(t_settings, v_a_settings, v_p_settings):

    """Перевод сценария в переменные"""
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
    sound_effect('sound/voice_person/room_1/1_intro_1.wav', v_p_settings)
    print_effect(intro_1, t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/2_intro_2.wav', v_p_settings)
    print_effect(intro_2, t_settings)
    time.sleep(11) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/3_intro_3.wav', v_p_settings)
    print_effect(intro_3, t_settings)
    time.sleep(8) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/4_intro_4.wav', v_p_settings)
    print_effect(intro_4, t_settings)
    time.sleep(5) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/5_intro_5.wav', v_p_settings)
    print_effect(intro_5 + '\n', t_settings)
    time.sleep(6) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/6_begin.wav', v_p_settings)
    print_effect(begin + '\n', t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    time.sleep(2)
    print(cave_entrance)
    sound_effect('sound/voice_actions/3_cave_entrance.wav', v_a_settings)
    time.sleep(2) if not t_settings and v_a_settings else None
    sound_effect('sound/voice_person/room_1/7_entrance.wav', v_p_settings)
    print_effect(entrance + '\n', t_settings)
    time.sleep(7) if not t_settings and v_p_settings else None
    time.sleep(2)


def room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, book_found):

    """Перевод сценария в переменные"""
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
            record = sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            option = input('Введите цифру: ')
            record.stop() if v_a_settings else None
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

    """Перевод сценария в переменные"""
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
    no_use_twig = r_1[113]
    no_use = [r_1[119], r_1[120], r_1[121], r_1[122], r_1[123]]
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
    need_diamond = r_1[116]
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
    bowl_is_examined = False
    diamond_is_taken = False
    twig_melted = False
    print(room_1_location)
    sound_effect('sound/voice_actions/4_room_1.wav', v_a_settings)
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/8_enter_1.wav', v_p_settings)
    print_effect(enter_1, t_settings)
    time.sleep(10) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/9_enter_2.wav', v_p_settings)
    print_effect(enter_2, t_settings)
    time.sleep(9) if not t_settings and v_p_settings else None
    time.sleep(2)
    sound_effect('sound/voice_person/room_1/10_enter_3.wav', v_p_settings)
    print_effect(enter_3, t_settings)
    time.sleep(2) if not t_settings and v_p_settings else None
    time.sleep(2)

    """осматриваемся"""
    while True:
        print(f'1) {look_around}')
        sound_effect('sound/voice_actions/option.wav', v_a_settings)
        time.sleep(2) if not t_settings and v_a_settings else None
        record = sound_effect('sound/voice_actions/5_look_around.wav', v_a_settings)
        option = input('Введите цифру: ')
        record.stop() if v_a_settings else None if v_a_settings else None
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
            sound_effect('sound/voice_person/room_1/11_room_examined.wav', v_p_settings)
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
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            record = sound_effect('sound/voice_actions/12_menu_2.wav', v_a_settings)
            option = input('Введите цифру: ')
            record.stop() if v_a_settings else None
        else:
            print(f'1) {examine_bowl}'
                  f'2) {examine_chest}'
                  f'3) {examine_stonewall}'
                  f'4) {examine_stone}' + '\n')
            sound_effect('sound/voice_actions/option.wav', v_a_settings)
            time.sleep(2) if not t_settings and v_a_settings else None
            record = sound_effect('sound/voice_actions/6_menu_1.wav', v_a_settings)
            option = input('Введите цифру: ')
            record.stop() if v_a_settings else None
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
            bowl_is_examined = True
            sound_effect('sound/voice_person/room_1/12_bowl_examined_1.wav', v_p_settings)
            print_effect(bowl_examined_1, t_settings)
            time.sleep(17) if not t_settings and v_p_settings else None
            time.sleep(1)
            sound_effect('sound/voice_person/room_1/13_bowl_examined_2.wav', v_p_settings)
            print_effect(bowl_examined_2, t_settings)
            time.sleep(6) if not t_settings and v_p_settings else None
            time.sleep(2)

            """осматриваем чашу"""
            while True:
                print(f'1) {get_coin}'
                      f'2) {lift_bowl}'
                      f'3) {leave_bowl}' + '\n')
                sound_effect('sound/voice_actions/option.wav', v_a_settings)
                time.sleep(2) if not t_settings and v_a_settings else None
                record = sound_effect('sound/voice_actions/7_bowl_options.wav', v_a_settings)
                option = input('Введите цифру: ')
                record.stop() if v_a_settings else None

                """смерть"""
                if option == '1':
                    while True:
                        room_1_mp3.stop() if m_settings else None
                        sound_effect('sound/sound_effects/death.wav', s_settings)
                        time.sleep(1) if s_settings else None
                        dd_mp3.set_volume(0.2) if m_settings else None
                        dd_mp3.play(-1) if m_settings else None
                        sound_effect('sound/voice_person/room_1/14_painful_death.wav', v_p_settings)
                        print_effect(painful_death, t_settings)
                        time.sleep(10) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        sound_effect('sound/voice_person/room_1/15_the_end.wav', v_p_settings)
                        print_effect(the_end, t_settings)
                        print('')
                        time.sleep(9) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        print(Fore.RED, f'{game_over}')
                        print(Style.RESET_ALL)
                        print(death_menu)
                        print(f'1) {load_game}'
                              f'2) {exit_game}' + '\n')
                        record = sound_effect('sound/voice_actions/10_death_menu.wav', v_a_settings)
                        option = input(f'Введите цифру: ')
                        record.stop() if v_a_settings else None
                        if option == '1':
                            dd_mp3.stop() if m_settings else None
                            room_1_mp3.play(-1) if m_settings else None
                            sound_effect('sound/voice_actions/11_game_resume.wav', v_a_settings)
                            print('')
                            print(Fore.YELLOW, f'{game_resume}')
                            print(Style.RESET_ALL)
                            time.sleep(2.5) if not t_settings and v_a_settings else None
                            break
                        elif option == '2':

                            """конец игры"""
                            exit()
                        else:
                            print(wrong_input(t_settings, v_a_settings))
                            continue
                    continue
                elif option == '2':
                    sound_effect('sound/voice_person/room_1/16_bowl_not_lifted.wav', v_p_settings)
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
                sound_effect('sound/voice_person/room_1/22_need_to_think.wav', v_p_settings)
                print_effect(need_to_think, t_settings)
                time.sleep(3) if not t_settings and v_p_settings else None
                time.sleep(1)
                while True:
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    if diamond_is_taken:
                        print(f'1) {twig}'
                              f'2) {rope}'
                              f'3) {sledgehammer}'
                              f'4) {glass}'
                              f'5) {close_chest}' + '\n')
                        record = sound_effect('sound/voice_actions/17_chest_inside.wav', v_a_settings)
                    else:
                        print(f'1) {twig}'
                              f'2) {rope}'                  
                              f'3) {sledgehammer}'
                              f'4) {diamond}'
                              f'5) {glass}'
                              f'6) {close_chest}' + '\n')
                        record = sound_effect('sound/voice_actions/17_chest_opened_no_diamond.wav', v_a_settings)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None

                    if option == '1':

                        """используем прут"""
                        while True:
                            if bowl_is_examined:
                                if twig_melted:
                                    print_effect(no_use_twig, t_settings)
                                    sound_effect('sound/voice_person/room_1/26_no_use_twig.wav', v_a_settings)
                                    time.sleep(5.5) if not t_settings and v_a_settings else None
                                    break
                                else:
                                    print(f'1) {get_coin_twig}'
                                          f'2) {get_twig_away}' + '\n')
                                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                    time.sleep(2) if not t_settings and v_a_settings else None
                                    record = sound_effect('sound/voice_actions/9_twig_options.wav', v_a_settings)
                                    option = input('Введите цифру: ')
                                    record.stop() if v_a_settings else None
                                    if option == '1':
                                        twig_melted = True
                                        sound_effect('sound/voice_person/room_1/23_twig_attempt.wav', v_p_settings)
                                        print_effect(twig_attempt, t_settings)
                                        time.sleep(1.5) if not t_settings and v_p_settings else None
                                        time.sleep(1)
                                        print(acid_hiss)
                                        sound_effect('sound/sound_effects/acid_hiss.wav', s_settings)
                                        time.sleep(2.5) if s_settings else None
                                        time.sleep(1)
                                        sound_effect('sound/voice_person/room_1/24_twig_failure_1.wav', v_p_settings)
                                        print_effect(twig_failure_1, t_settings)
                                        time.sleep(10) if not t_settings and v_p_settings else None
                                        time.sleep(1)
                                        sound_effect('sound/voice_person/room_1/25_twig_failure_2.wav', v_p_settings)
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
                            else:
                                random_no(t_settings, v_p_settings, no_use)
                                time.sleep(1)
                                continue
                    elif option == '2':
                        random_no(t_settings, v_p_settings, no_use)
                        time.sleep(1)
                        continue
                    elif option == '3':
                        if stonewall_is_examined:

                            """разбиваем стену"""
                            while True:
                                print(f'1) {smash_the_wall}' + '\n')
                                sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                time.sleep(2) if not t_settings and v_a_settings else None
                                record = sound_effect('sound/voice_actions/14_smash_menu.wav', v_a_settings)
                                option = input('Введите цифру: ')
                                record.stop() if v_a_settings else None
                                if option == '1':
                                    sound_effect('sound/voice_person/room_1/29_lets_smash.wav', v_p_settings)
                                    print_effect(lets_smash, t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    print(rattle)
                                    sound_effect('sound/sound_effects/wall_smashed.wav', s_settings)
                                    time.sleep(8) if s_settings else None
                                    sound_effect('sound/voice_person/room_1/30_wall_smashed.wav', v_p_settings)
                                    print_effect(wall_smashed, t_settings)
                                    time.sleep(5) if not t_settings and v_p_settings else None
                                    print(rattle_intensifies)
                                    sound_effect('sound/sound_effects/stones.wav', s_settings)
                                    time.sleep(1) if s_settings else None
                                    sound_effect('sound/sound_effects/giant_stone.wav', s_settings)
                                    time.sleep(7) if s_settings else None
                                    sound_effect('sound/voice_person/room_1/30_something_wrong.wav', v_p_settings)
                                    print_effect(something_wrong, t_settings)
                                    time.sleep(4) if not t_settings and v_p_settings else None
                                    time.sleep(2)

                                    """обвал"""
                                    print(run_away)
                                    time.sleep(1)
                                    room_1_mp3.stop() if m_settings else None
                                    dd_mp3.set_volume(0.2) if m_settings else None
                                    dd_mp3.play(-1) if m_settings else None
                                    sound_effect('sound/voice_person/room_1/31_trapped_1.wav', v_p_settings)
                                    print_effect(trapped_1, t_settings)
                                    time.sleep(4) if not t_settings and v_p_settings else None
                                    time.sleep(2)
                                    sound_effect('sound/voice_person/room_1/32_trapped_2.wav', v_p_settings)
                                    print_effect(trapped_2, t_settings)
                                    time.sleep(12) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    sound_effect('sound/voice_person/room_1/33_trapped_3.wav', v_p_settings)
                                    print_effect(trapped_3, t_settings)
                                    time.sleep(6) if not t_settings and v_p_settings else None
                                    time.sleep(1)
                                    print(return_to_room_1)
                                    time.sleep(1)
                                    dd_mp3.stop() if m_settings else None
                                    room_1_mp3.play(-1) if m_settings else None
                                    sound_effect('sound/voice_person/room_1/34_decision.wav', v_p_settings)
                                    print_effect(decision, t_settings)
                                    time.sleep(16) if not t_settings and v_p_settings else None
                                    time.sleep(2)

                                    """принимаем решение"""
                                    while True:
                                        print(f'1) {open_chest}'
                                              f'2) {to_room_2}')
                                        sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                        time.sleep(2) if not t_settings and v_a_settings else None
                                        record = sound_effect('sound/voice_actions/16_final_menu.wav', v_a_settings)
                                        option = input('Введите цифру: ')
                                        record.stop() if v_a_settings else None
                                        if option == '1':
                                            sound_effect('sound/sound_effects/open_chest.wav', s_settings)
                                            time.sleep(1.5) if s_settings else None
                                            while True:
                                                if diamond_is_taken:
                                                    print(f'1) {rope}'
                                                          f'2) {glass}'
                                                          f'3) {close_chest}')
                                                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                                    time.sleep(2) if not t_settings and v_a_settings else None
                                                    record = sound_effect('sound/voice_actions/18_fm_2.wav',
                                                                          v_a_settings)
                                                    option = input('Введите цифру: ')
                                                    record.stop() if v_a_settings else None
                                                    if option == '1':
                                                        random_no(t_settings, v_p_settings, no_use)
                                                        continue
                                                    elif option == '2':
                                                        if glass_is_examined:
                                                            random_no(t_settings, v_p_settings, no_use)
                                                        else:
                                                            sound_effect('sound/voice_person/room_1/27_no_glass.wav',
                                                                         v_p_settings)
                                                            print_effect(no_glass, t_settings)
                                                            time.sleep(6) if not t_settings and v_p_settings else None
                                                            time.sleep(1)
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
                                                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                                                    time.sleep(2) if not t_settings and v_a_settings else None
                                                    record = sound_effect('sound/voice_actions/19_fm_3.wav',
                                                                          v_a_settings)
                                                    option = input('Введите цифру: ')
                                                    record.stop() if v_a_settings else None
                                                    if option == '1':
                                                        random_no(t_settings, v_p_settings, no_use)
                                                        continue
                                                    elif option == '2':
                                                        if glass_is_examined:
                                                            random_no(t_settings, v_p_settings, no_use)
                                                        else:
                                                            sound_effect('sound/voice_person/room_1/27_no_glass.wav',
                                                                         v_p_settings)
                                                            print_effect(no_glass, t_settings)
                                                            time.sleep(6) if not t_settings and v_p_settings else None
                                                            time.sleep(1)
                                                        continue
                                                    elif option == '3':
                                                        diamond_is_taken = True
                                                        sound_effect('sound/voice_person/room_1/28_took_diamond.wav',
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
                                            if diamond_is_taken:
                                                sound_effect('sound/voice_person/room_1/36_last_hope.wav', v_p_settings)
                                                print_effect(last_hope, t_settings)
                                                time.sleep(4) if not t_settings and v_p_settings else None
                                                time.sleep(2)
                                                print(another_location)
                                                return
                                            else:
                                                sound_effect('sound/voice_person/room_1/35_need_diamond.wav',
                                                             v_p_settings)
                                                print_effect(need_diamond, t_settings)
                                                time.sleep(6.5) if not t_settings and v_p_settings else None
                                                continue
                                else:
                                    print(wrong_input(t_settings, v_a_settings))
                                    continue
                        else:
                            random_no(t_settings, v_p_settings, no_use)
                            time.sleep(1)
                        continue
                    elif option == '4':
                        if diamond_is_taken:
                            if glass_is_examined:
                                print_effect(enough_watching, t_settings)
                                break
                            else:
                                sound_effect('sound/voice_person/room_1/27_no_glass.wav', v_p_settings)
                                print_effect(no_glass, t_settings)
                                time.sleep(6) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                continue
                        else:
                            diamond_is_taken = True
                            sound_effect('sound/voice_person/room_1/28_took_diamond.wav', v_p_settings)
                            print_effect(took_diamond, t_settings)
                            time.sleep(16) if not t_settings and v_p_settings else None
                            time.sleep(1)
                            continue
                    elif option == '5':
                        if diamond_is_taken:
                            sound_effect('sound/sound_effects/close_chest.wav', s_settings)
                            time.sleep(1.5) if s_settings else None
                            break
                        else:
                            if glass_is_examined:
                                print_effect(enough_watching, t_settings)
                                break
                            else:
                                sound_effect('sound/voice_person/room_1/27_no_glass.wav', v_p_settings)
                                print_effect(no_glass, t_settings)
                                time.sleep(6) if not t_settings and v_p_settings else None
                                time.sleep(1)
                                continue
                    elif option == '6':
                        if diamond_is_taken:
                            print(wrong_input(t_settings, v_a_settings))
                            continue
                        else:
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
                    sound_effect('sound/voice_person/room_1/17_chest_examined.wav', v_p_settings)
                    print_effect(chest_examined, t_settings)
                    time.sleep(11) if not t_settings and v_p_settings else None
                    time.sleep(1)
        elif option == '3':
            if stonewall_is_examined:
                print_effect(enough_watching, t_settings)
                continue
            else:
                stonewall_is_examined = True
                sound_effect('sound/voice_person/room_1/18_stonewall_examined.wav', v_p_settings)
                print_effect(stonewall_examined, t_settings)
                time.sleep(12.5) if not t_settings and v_p_settings else None
                time.sleep(1)
                continue
        elif option == '4':
            if stone_moved:
                sound_effect('sound/voice_person/no_use_2.wav', v_p_settings)
                print_effect(r_1[120], t_settings)
                time.sleep(2.5) if not t_settings and v_p_settings else None
                continue
            else:
                """двигаем камень"""
                stone_moved = True
                sound_effect('sound/voice_person/room_1/19_stone_examined.wav', v_p_settings)
                print_effect(stone_examined, t_settings)
                time.sleep(6.5) if not t_settings and v_p_settings else None
                time.sleep(1)
                while True:
                    print(f'1) {move_stone}'
                          f'2) {leave_stone}' + '\n')
                    sound_effect('sound/voice_actions/option.wav', v_a_settings)
                    time.sleep(2) if not t_settings and v_a_settings else None
                    record = sound_effect('sound/voice_actions/13_stone_menu.wav', v_a_settings)
                    option = input('Введите цифру: ')
                    record.stop() if v_a_settings else None
                    if option == '1':
                        sound_effect('sound/sound_effects/move_stone.wav', s_settings)
                        time.sleep(6.5) if s_settings else None
                        sound_effect('sound/voice_person/room_1/20_key_found.wav', v_p_settings)
                        print_effect(key_found, t_settings)
                        time.sleep(3) if not t_settings and v_p_settings else None
                        time.sleep(1)
                        while True:
                            print(f'1) {open_chest}' + '\n')
                            sound_effect('sound/voice_actions/option.wav', v_a_settings)
                            time.sleep(2) if not t_settings and v_a_settings else None
                            record = sound_effect('sound/voice_actions/17_open_chest_menu.wav', v_a_settings)
                            option = input('Введите цифру: ')
                            record.stop() if v_a_settings else None
                            if option == '1':
                                sound_effect('sound/sound_effects/key.wav', s_settings)
                                time.sleep(2) if s_settings else None
                                sound_effect('sound/voice_person/room_1/21_chest_opened.wav', v_p_settings)
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
    insert_stone = r_2[155]
    knock_the_wall = r_2[162]
    hit_the_wall = r_2[165]
    read_book = r_2[170]
    read_log = r_2[171]
    take_bundle = r_2[172]
    leave_location = r_2[222]
    chest_wont_open = [r_2[226], r_2[227], r_2[228]]
    leave_candles = r_2[230]
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
    riddle_is_combined = False
    papers_combined = False
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
            paper_1_read = False
            paper_2_read = False
            paper_3_read = False
            language_found = 0
            read_count = 0
            while True:
                if papers_combined:
                    break
                if paper_1_read and paper_2_read and paper_3_read:
                    print(f'1) {read_paper_1}'
                          f'2) {read_paper_2}'
                          f'3) {read_paper_3}'
                          f'4) {combine_papers}' + '\n')
                else:
                    print(f'1) {read_paper_1}'
                          f'2) {read_paper_2}'
                          f'3) {read_paper_3}' + '\n')
                option = input('Введите цифру: ')
                print_effect(reactions[0], t_settings) if read_count == 0 else None
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
                        print(wrong_input(t_settings, v_a_settings))
                        continue
        else:
            print(wrong_input(t_settings, v_a_settings))
            continue

    # while True:
    #     print_effect(chest_opened, t_settings)
    #     time.sleep(1)
    #     print(f'1) {examine_the_table}'
    #           f'2) {examine_altar}' + '\n')
    #     option = input('Введите цифру: ')

    # """головоломка со светом"""
    # light_on = False
    # papers_read = False
    # mechanism_examined = False
    # while True:
    #     if papers_read and mechanism_examined:
    #         break
    #     else:
    #         print(f'1) {read_papers}'
    #               f'3) {light_candle}' + '\n')
    #
    #         option = input('Введите цифру: ')
    #         if option == '1':
    #             if light_on is True:
    #                 papers_read = True
    #                 print_effect(begin_reading, t_settings)
    #                 print_effect(line_1, t_settings)
    #                 print_effect(line_2 + '\n', t_settings)
    #                 time.sleep(2)
    #                 print_effect(line_3, t_settings)
    #                 print_effect(line_4 + '\n', t_settings)
    #                 time.sleep(2)
    #                 print_effect(need_to_think, t_settings)
    #                 time.sleep(1)
    #                 print_effect(why_religion, t_settings)
    #                 time.sleep(2)
    #                 print_effect(back_to_business, t_settings)
    #                 time.sleep(1)
    #                 continue
    #             else:
    #                 print_effect(no_light, t_settings)
    #                 time.sleep(1)
    #                 continue
    #
    # """вставляем камень в оправу"""
    # while True:
    #     print(f'1) {insert_stone}' + '\n')
    #     sound_effect('sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         print_effect(stone_inserted, t_settings)
    #         time.sleep(2)
    #         print_effect(diamond_correct, t_settings)
    #         time.sleep(1)
    #         print_effect(great_diamond, t_settings)
    #         time.sleep(1)
    #         print_effect(follow_the_light, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(wrong_input(t_settings, v_a_settings))
    #
    # """обнаруживаем тайник"""
    # while True:
    #     print(f'1) {knock_the_wall}' + '\n')
    #     sound_effect('sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         print_effect(storage_found, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(wrong_input(t_settings, v_a_settings))
    # while True:
    #     print(f'1) {hit_the_wall}' + '\n')
    #     sound_effect('sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         print_effect(storage_opened, t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(wrong_input(t_settings, v_a_settings))
    #
    # """читаем записку"""
    # while True:
    #     print(f'1) {read_book}' + '\n')
    #     sound_effect('sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         print_effect(read_1, t_settings)
    #         time.sleep(1)
    #         print_effect(read_2 + '\n', t_settings)
    #         time.sleep(2)
    #         print_effect(book_1, t_settings)
    #         print_effect(book_2, t_settings)
    #         print_effect(book_3, t_settings)
    #         print_effect(book_4, t_settings)
    #         print_effect(book_5, t_settings)
    #         print_effect(book_6, t_settings)
    #         print_effect(book_7, t_settings)
    #         print_effect(book_8, t_settings)
    #         print_effect(book_9 + '\n', t_settings)
    #         time.sleep(2)
    #         print_effect(conclusion, t_settings)
    #         time.sleep(2)
    #         print_effect(get_tools, t_settings)
    #         time.sleep(1)
    #         print_effect(get_away + '\n', t_settings)
    #         time.sleep(1)
    #         break
    #     else:
    #         print(wrong_input(t_settings, v_a_settings))
    #
    # """уходим"""
    # while True:
    #     print(f'1) {leave_location}' + '\n')
    #     sound_effect('sound/voice_actions/option.wav', v_a_settings)
    #     time.sleep(2) if not t_settings and v_a_settings else None
    #     option = input('Введите цифру: ')
    #     if option == '1':
    #         return
    #     else:
    #         print(wrong_input(t_settings, v_a_settings))
    #         continue


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
    # room_1_mp3.set_volume(0.2) if m_settings else None
    # room_1_mp3.play(-1) if m_settings else None
    # start_game(t_settings, v_a_settings, v_p_settings)
    # room_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    room_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    # room_1_mp3.play(-1) if m_settings else None
    # room_1_again(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
    # final_location(t_settings, v_a_settings, v_p_settings, m_settings, s_settings)
