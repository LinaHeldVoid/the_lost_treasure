import pygame
import time

from colorama import Fore, Style
from read_scenario import scenario as s
from sound_manager import room_1_mp3, room_2_mp3, dd_mp3


# неверный ввод
def wrong_input():
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


# имитация чтения книги
def print_effect(text):
    for i in text:
        time.sleep(0.005)
        print(i, end='', flush=True)


# начало, вход
def start_game():

    """перевод сценария в переменные"""
    start = s[0]
    intro_1 = s[2]
    intro_2 = s[3]
    intro_3 = s[4]
    intro_4 = s[5]
    intro_5 = s[6]
    begin = s[9]
    cave_entrance = s[11]
    entrance = s[12]

    """алгоритм"""
    print(Fore.GREEN, f'<------------{start}')
    print(Style.RESET_ALL)
    time.sleep(3)
    print_effect(intro_1)
    time.sleep(2)
    print_effect(intro_2)
    time.sleep(2)
    print_effect(intro_3)
    time.sleep(2)
    print_effect(intro_4)
    time.sleep(2)
    print_effect(intro_5 + '\n')
    time.sleep(2)
    print_effect(begin + '\n')
    time.sleep(2)
    print(cave_entrance)
    print_effect(entrance + '\n')
    time.sleep(2)


# главный зал
def room_1():

    """перевод сценария в переменные"""
    enter_1 = s[15]
    enter_2 = s[16]
    enter_3 = s[17]
    room_examined = s[20]
    bowl_examined = s[23] + s[24]
    painful_death = s[27]
    the_end = s[28]
    game_over = s[29]
    death_menu = s[30]
    game_resume = s[31]
    bowl_not_lifted = s[36]
    chest_examined = s[41]
    stonewall_examined = s[44]
    stone_examined = s[47]
    key_found = s[50]
    chest_opened = s[54]
    need_to_think = s[63]
    twig_attempt = s[66]
    twig_failure = s[67] + s[68] + s[69]
    no_use = s[73]
    no_glass = s[75]
    took_diamond = s[79]
    lets_smash = s[82]
    wall_smashed = s[84] + s[85] + s[86] + s[87]
    trapped_1 = s[89]
    trapped_2 = s[90]
    trapped_3 = s[91]
    decision = s[94]
    last_hope = s[101]

    room_1_location = s[14]
    look_around = s[19]
    examine_bowl = s[22]
    get_coin = s[26]
    load_game = s[31]
    exit_game = s[32]
    lift_bowl = s[35]
    leave_bowl = s[38]
    examine_chest = s[40]
    examine_stonewall = s[43]
    examine_stone = s[46]
    move_stone = s[49]
    leave_stone = s[51]
    open_chest = s[53]
    twig = s[56]
    rope = s[57]
    sledgehammer = s[58]
    diamond = s[59]
    glass = s[60]
    close_chest = s[61]
    get_coin_twig = s[65]
    get_twig_away = s[70]
    smash_the_wall = s[81]
    run_away = s[88]
    return_to_room_1 = s[93]
    to_room_2 = s[100]
    another_location = s[102]

    """алгоритм"""
    chest_is_opened = False
    stonewall_is_examined = False
    print(room_1_location)
    print_effect(enter_1)
    time.sleep(2)
    print_effect(enter_2)
    time.sleep(2)
    print_effect(enter_3)
    time.sleep(2)

    """осматриваемся"""
    while True:
        print(f'1) {look_around}')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(room_examined)
            break
        else:
            print(wrong_input())
            continue
    while True:
        print(f'1) {examine_bowl}'
              f'2) {examine_chest}'
              f'3) {examine_stonewall}'
              f'4) {examine_stone}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(bowl_examined)

            """осматриваем чашу"""
            while True:
                print(f'1) {get_coin}'
                      f'2) {lift_bowl}'
                      f'3) {leave_bowl}' + '\n')
                option = input('Введите цифру: ')

                """смерть"""
                if option == '1':
                    while True:
                        room_1_mp3.stop()
                        dd_mp3.play(-1)
                        print_effect(painful_death)
                        time.sleep(2)
                        print_effect(the_end)
                        print(Fore.RED, f'<------------{game_over}')
                        print(Style.RESET_ALL)
                        print(death_menu)
                        print(f'1) {load_game}'
                              f'2) {exit_game}' + '\n')
                        option = input(f'Введите цифру: ')
                        if option == '1':
                            dd_mp3.stop()
                            room_1_mp3.play(-1)
                            print(Fore.YELLOW, f'<------------{game_resume}')
                            print(Style.RESET_ALL)
                            break
                        elif option == '2':

                            """конец игры"""
                            exit()
                        else:
                            print(wrong_input())
                            continue
                    continue
                elif option == '2':
                    print_effect(bowl_not_lifted)
                    continue
                elif option == '3':
                    break
                else:
                    print(wrong_input())
                    continue
        elif option == '2':

            """открываем сундук"""
            if chest_is_opened:
                print_effect(need_to_think)
                while True:
                    print(f'1) {twig}'
                          f'2) {rope}'                  
                          f'3) {sledgehammer}'
                          f'4) {diamond}'
                          f'5) {glass}'
                          f'6) {close_chest}' + '\n')
                    option = input('Введите цифру: ')
                    if option == '1':

                        """используем прут"""
                        while True:
                            print(f'1) {get_coin_twig}'
                                  f'2) {get_twig_away}' + '\n')
                            option = input('Введите цифру: ')
                            if option == '1':
                                print_effect(twig_attempt)
                                print_effect(twig_failure)
                                break
                            elif option == '2':
                                break
                            else:
                                print(wrong_input())
                                continue
                    elif option == '2':
                        print_effect(no_use)
                        continue
                    elif option == '3':
                        if stonewall_is_examined:

                            """развиваем стену"""
                            while True:
                                print(f'1) {smash_the_wall}' + '\n')
                                option = input('Введите цифру: ')
                                if option == '1':
                                    print_effect(lets_smash)
                                    time.sleep(2)
                                    print_effect(wall_smashed)
                                    time.sleep(2)

                                    """обвал"""
                                    print(run_away)
                                    room_1_mp3.stop()
                                    dd_mp3.play(-1)
                                    print_effect(trapped_1)
                                    time.sleep(2)
                                    print_effect(trapped_2)
                                    time.sleep(2)
                                    print_effect(trapped_3)
                                    time.sleep(2)
                                    print(return_to_room_1)
                                    dd_mp3.stop()
                                    room_1_mp3.play(-1)
                                    print_effect(decision)

                                    """принимаем решение"""
                                    while True:
                                        print(f'1) {open_chest}'
                                              f'2) {to_room_2}')
                                        option = input('Введите цифру: ')
                                        if option == '1':
                                            while True:
                                                print(f'1) {rope}'
                                                      f'2) {glass}'
                                                      f'3) {close_chest}')
                                                option = input('Введите цифру: ')
                                                if option == '1':
                                                    print_effect(no_use)
                                                    continue
                                                elif option == '2':
                                                    print_effect(no_glass)
                                                    continue
                                                elif option == '3':
                                                    break
                                                else:
                                                    print(wrong_input())
                                                    continue
                                        elif option == '2':
                                            print_effect(last_hope)
                                            print(another_location)
                                            return
                                else:
                                    print(wrong_input())
                                    continue
                        else:
                            print_effect(no_use)
                        continue
                    elif option == '4':
                        print_effect(took_diamond)
                        continue
                    elif option == '5':
                        print_effect(no_glass)
                        continue
                    elif option == '6':
                        break
                    else:
                        print(wrong_input())
                        continue
            else:
                print_effect(chest_examined)
        elif option == '3':
            print_effect(stonewall_examined)
            stonewall_is_examined = True
            continue
        elif option == '4':

            """двигаем камень"""
            print_effect(stone_examined)
            while True:
                print(f'1) {move_stone}'
                      f'2) {leave_stone}' + '\n')
                option = input('Введите цифру: ')
                if option == '1':
                    print_effect(key_found)
                    while True:
                        print(f'1) {open_chest}' + '\n')
                        option = input('Введите цифру: ')
                        if option == '1':
                            print_effect(chest_opened)
                            chest_is_opened = True
                            break
                    break
                elif option == '2':
                    break
                else:
                    print(wrong_input())
                    continue
            continue
        else:
            print(wrong_input())
            continue


# рабочий кабинет
def room_2():

    """перевод сценария в переменные"""
    look_around_1 = s[105]
    look_around_2 = s[106]
    table_examined_1 = s[109]
    table_examined_2 = s[110]
    shelf_1 = s[113]
    shelf_2 = s[116]
    shelf_3 = s[119]
    shelves_examined = s[120]
    candle_lightened = s[123]
    no_light = s[127]
    mechanism_examined_1 = s[130]
    mechanism_examined_2 = s[131]
    begin_reading = s[134]
    line_1 = s[135]
    line_2 = s[136]
    line_3 = s[138]
    line_4 = s[139]
    need_to_think = s[141]
    why_religion = s[142]
    back_to_business = s[143]
    stone_inserted = s[146]
    diamond_correct = s[148]
    great_diamond = s[149]
    follow_the_light = s[150]
    storage_found = s[153]
    storage_opened = s[156]
    read_1 = s[159]
    read_2 = s[160]
    book_1 = s[162]
    book_2 = s[163]
    book_3 = s[164]
    book_4 = s[165]
    book_5 = s[166]
    book_6 = s[167]
    book_7 = s[168]
    book_8 = s[169]
    book_9 = s[170]
    conclusion = s[172]
    get_tools = s[173]
    get_away = s[174]

    entry = s[104]
    examine_the_table = s[108]
    open_shelf_1 = s[112]
    open_shelf_2 = s[115]
    open_shelf_3 = s[118]
    light_candle = s[122]
    examine_mechanism = s[129]
    read_papers = s[133]
    insert_stone = s[145]
    knock_the_wall = s[152]
    hit_the_wall = s[155]
    read_book = s[158]
    leave_location = s[176]

    """алгоритм"""
    room_2_mp3.play(-1)
    print(entry)
    time.sleep(1)
    print_effect(look_around_1)
    time.sleep(1)
    print_effect(look_around_2)
    time.sleep(1)

    """осматриваем стол"""
    while True:
        print(f'1) {examine_the_table}')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(table_examined_1)
            time.sleep(1)
            print_effect(table_examined_2)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue
    open_1 = False
    open_2 = False
    open_3 = False

    """проверяем полки"""
    while True:
        if open_1 is True and open_2 is True and open_3 is True:
            print_effect(shelves_examined)
            break
        else:
            print(f'1) {open_shelf_1}'
                  f'2) {open_shelf_2}'
                  f'3) {open_shelf_3}' + '\n')
            option = input('Введите цифру: ')
            if option == '1':
                open_1 = True
                print_effect(shelf_1)
                time.sleep(1)
                continue
            elif option == '2':
                open_2 = True
                print_effect(shelf_2)
                time.sleep(1)
                continue
            elif option == '3':
                open_3 = True
                print_effect(shelf_3)
                time.sleep(1)
                continue
            else:
                print(wrong_input())
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
            option = input('Введите цифру: ')
            if option == '1':
                if light_on is True:
                    papers_read = True
                    print_effect(begin_reading)
                    print_effect(line_1)
                    print_effect(line_2 + '\n')
                    time.sleep(2)
                    print_effect(line_3)
                    print_effect(line_4 + '\n')
                    time.sleep(2)
                    print_effect(need_to_think)
                    time.sleep(1)
                    print_effect(why_religion)
                    time.sleep(2)
                    print_effect(back_to_business)
                    time.sleep(1)
                    continue
                else:
                    print_effect(no_light)
                    time.sleep(1)
                    continue
            elif option == '2':
                if light_on is True:
                    mechanism_examined = True
                    print_effect(mechanism_examined_1)
                    time.sleep(1)
                    print_effect(mechanism_examined_2)
                    time.sleep(1)
                    continue
                else:
                    print_effect(no_light)
                    time.sleep(1)
                    continue
            elif option == '3':
                light_on = True
                print_effect(candle_lightened)
                time.sleep(1)
                continue
            else:
                print(wrong_input())
                continue

    """вставляем камень в оправу"""
    while True:
        print(f'1) {insert_stone}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(stone_inserted)
            time.sleep(2)
            print_effect(diamond_correct)
            time.sleep(1)
            print_effect(great_diamond)
            time.sleep(1)
            print_effect(follow_the_light)
            time.sleep(1)
            break
        else:
            print(wrong_input())

    """обнаруживаем тайник"""
    while True:
        print(f'1) {knock_the_wall}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(storage_found)
            time.sleep(1)
            break
        else:
            print(wrong_input())
    while True:
        print(f'1) {hit_the_wall}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(storage_opened)
            time.sleep(1)
            break
        else:
            print(wrong_input())

    """читаем записку"""
    while True:
        print(f'1) {read_book}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(read_1)
            time.sleep(1)
            print_effect(read_2 + '\n')
            time.sleep(2)
            print_effect(book_1)
            print_effect(book_2)
            print_effect(book_3)
            print_effect(book_4)
            print_effect(book_5)
            print_effect(book_6)
            print_effect(book_7)
            print_effect(book_8)
            print_effect(book_9 + '\n')
            time.sleep(2)
            print_effect(conclusion)
            time.sleep(2)
            print_effect(get_tools)
            time.sleep(1)
            print_effect(get_away + '\n')
            time.sleep(1)
            break
        else:
            print(wrong_input())

    """уходим"""
    while True:
        print(f'1) {leave_location}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            return
        else:
            print(wrong_input())
            continue


def room_1_again():

    """перевод сценария в переменные"""
    begin = s[177]
    glass = s[182]
    pouring_potion = s[185]
    result_1 = s[187]
    result_2 = s[188]
    result_3 = s[189]
    result_4 = s[190]
    start_experiment = s[193]
    paper_in_glass = s[197]
    need_to_think = s[200]
    no_effect = s[203]
    of_course = s[206]
    effect_1 = s[207]
    effect_2 = s[208]
    effect_3 = s[209]
    coin_stuck = s[212]
    bowl_effect = s[214]
    bowl_destiny_1 = s[215]
    bowl_destiny_2 = s[216]
    read_paper = s[218]
    paper_1 = s[220]
    paper_2 = s[221]
    paper_3 = s[222]
    paper_4 = s[223]
    paper_5 = s[224]
    paper_6 = s[225]
    paper_7 = s[227]
    paper_8 = s[228]
    so_cool = s[230]
    lets_get_out = s[231]
    rope = s[234]
    sledgehammer = s[236]
    get_out = s[239]

    open_chest = s[53]
    close_chest = s[61]
    no_use = s[73]
    get_rope = s[179]
    get_sledgehammer = s[180]
    get_glass = s[181]
    pour_potion = s[184]
    burn_paper = s[192]
    put_paper = s[196]
    put_glass = s[199]
    normal = s[202]
    upside_down = s[205]
    get_coin = s[211]

    """алгоритм"""
    print_effect(begin)
    glass_taken = False
    while True:
        if glass_taken:
            break
        else:
            print(f'1) {open_chest}' + '\n')
            option = input('Введите цифру: ')
            if option == '1':
                while True:
                    print(f'1) {get_glass}'
                          f'2) {get_rope}'
                          f'3) {get_sledgehammer}'
                          f'4) {close_chest}' + '\n')
                    option = input('Введите цифру: ')
                    if option == '1':
                        glass_taken = True
                        print_effect(glass)
                        time.sleep(1)
                        break
                    elif option == '2' or option == '3':
                        print_effect(no_use)
                        time.sleep(1)
                        continue
                    elif option == '4':
                        break
                    else:
                        print(wrong_input())
                        continue
            else:
                print(wrong_input())
                continue

    """разбираемся с зельем"""
    while True:
        print(f'1) {pour_potion}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(pouring_potion)
            time.sleep(2)
            print_effect(result_1)
            time.sleep(1)
            print_effect(result_2)
            time.sleep(1)
            print_effect(result_3)
            time.sleep(1)
            print_effect(result_4)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue
    while True:
        print(f'1) {burn_paper}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(start_experiment)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue
    while True:
        print(f'1) {put_paper}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(paper_in_glass)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue
    bowl_ready = False
    mistake_made = False
    while True:
        if bowl_ready:
            break
        else:
            print(f'1) {put_glass}' + '\n')
            option = input('Введите цифру: ')
            if option == '1':
                print_effect(need_to_think)
                time.sleep(1)
                while True:
                    print(f'1) {normal}'
                          f'2) {upside_down}' + '\n')
                    option = input('Введите цифру: ')
                    if option == '1':
                        mistake_made = True
                        print_effect(no_effect)
                        time.sleep(1)
                        continue
                    elif option == '2':
                        bowl_ready = True
                        if mistake_made:
                            print_effect(of_course)
                            time.sleep(1)
                        print_effect(effect_1)
                        time.sleep(1)
                        print_effect(effect_2)
                        time.sleep(1)
                        print_effect(effect_3)
                        time.sleep(1)
                        break
            else:
                print(wrong_input())
                continue
    while True:
        print(f'1) {get_coin}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(coin_stuck)
            time.sleep(1)
            print_effect(bowl_effect)
            time.sleep(1)
            print_effect(bowl_destiny_1)
            time.sleep(1)
            print_effect(bowl_destiny_2)
            time.sleep(1)
            print_effect(read_paper)
            time.sleep(2)
            print_effect(paper_1)
            time.sleep(1)
            print_effect(paper_2)
            print_effect(paper_3)
            time.sleep(1)
            print_effect(paper_4)
            print_effect(paper_5)
            print_effect(paper_6 + '\n')
            time.sleep(2)
            print_effect(paper_7)
            time.sleep(1)
            print_effect(paper_8 + '\n')
            time.sleep(2)
            print_effect(so_cool)
            time.sleep(1)
            print_effect(lets_get_out)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue

    """забираем всё из сундука"""
    rope_taken = False
    sledgehammer_taken = False
    print(f'1) {open_chest}' + '\n')
    option = input('Введите цифру: ')
    while True:
        if option == '1':
            while True:
                if rope_taken and sledgehammer_taken:
                    break
                else:
                    print(f'1) {get_rope}'
                          f'2) {get_sledgehammer}' + '\n')
                    option = input('Введите цифру: ')
                    if option == '1':
                        rope_taken = True
                        print_effect(rope)
                        time.sleep(1)
                        continue
                    elif option == '2':
                        sledgehammer_taken = True
                        print_effect(sledgehammer)
                        time.sleep(1)
                        continue
                    else:
                        print(wrong_input())
                        continue
        else:
            print(wrong_input())
            continue

        """уходим"""
        while True:
            print(f'1) {get_out}' + '\n')
            option = input('Введите цифру: ')
            if option == '1':
                return
            else:
                print(wrong_input())
                continue


def final_location():

    """перевод сценария в переменные"""
    need_to_think = s[242]
    cant_smash = s[248]
    lets_pray = s[249]
    prayer_1 = s[252]
    prayer_2 = s[253]
    hole = s[257]
    lets_go = s[258]
    final = s[262]
    epilogue_1 = s[265]
    epilogue_2 = s[266]
    epilogue_3 = s[267]
    epilogue_4 = s[268]
    epilogue_5 = s[269]
    thanks = s[271]
    good_luck = s[272]
    end_game = s[274]

    cave_entrance = s[241]
    smash_wall = s[244]
    pray = s[245]
    through_sledgehammer = s[255]
    escape = s[260]
    dots = s[261]
    epilogue = s[264]

    """алгоритм"""
    print(cave_entrance)
    time.sleep(1)
    print_effect(need_to_think)
    time.sleep(1)
    while True:
        print(f'1) {smash_wall}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(cant_smash)
            time.sleep(2)
            print_effect(lets_pray)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue

    """молитва и побег"""
    while True:
        print(f'1) {pray}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            print_effect(prayer_1)
            time.sleep(2)
            print_effect(prayer_2)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue
    while True:
        print(f'1) {through_sledgehammer}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            time.sleep(1)
            print_effect(hole)
            time.sleep(2)
            print_effect(lets_go)
            time.sleep(1)
            break
        else:
            print(wrong_input())
            continue
    while True:
        print(f'1) {escape}' + '\n')
        option = input('Введите цифру: ')
        if option == '1':
            time.sleep(1)
            print_effect(dots)
            time.sleep(1)
            print_effect(final)
            room_1_mp3.fadeout(2000)
            time.sleep(1)
            time.sleep(2)
            break
        else:
            print(wrong_input())
            continue

    """ЭПИЛОГ"""
    room_2_mp3.play()
    print(epilogue)
    time.sleep(2)
    print_effect(epilogue_1)
    time.sleep(2)
    print_effect(epilogue_2)
    time.sleep(2)
    print_effect(epilogue_3)
    time.sleep(2)
    print_effect(epilogue_4 + '\n')
    time.sleep(2)
    print_effect(epilogue_5 + '\n')
    time.sleep(2)
    room_2_mp3.fadeout(3000)
    print_effect(thanks)
    time.sleep(1)
    print_effect(good_luck)
    time.sleep(1)
    print(Fore.GREEN, end_game)
    print(Style.RESET_ALL)
    time.sleep(2)
    return


# запуск игры в консоли
def run_game_console(voice_settings=False):
    room_1_mp3.play(-1)
    start_game()
    room_1()
    room_2()
    room_1_mp3.play(-1)
    room_1_again()
    final_location()
