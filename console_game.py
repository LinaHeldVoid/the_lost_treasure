import pygame
import time

from colorama import Fore, Back, Style
from pprint import pprint
from read_scenario import scenario as s
from sound_manager import room_1_mp3, room_2_mp3, dd_mp3


def wrong_input():
    message = 'Извините, ваш ответ не распознан. Попробуйте ещё раз!'
    return message


def print_effect(text):
    for i in text:
        time.sleep(0.0001)
        print(i, end='', flush=True)


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
            while True:
                print(f'1) {get_coin}'
                      f'2) {lift_bowl}'
                      f'3) {leave_bowl}' + '\n')
                option = input('Введите цифру: ')
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
                            while True:
                                print(f'1) {smash_the_wall}' + '\n')
                                option = input('Введите цифру: ')
                                if option == '1':
                                    print_effect(lets_smash)
                                    time.sleep(2)
                                    print_effect(wall_smashed)
                                    time.sleep(2)
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


def run_the_game():
    room_1_mp3.play(-1)
    start_game()
    room_1()


pygame.init()
pygame.mixer.init()
pprint(s)
run_the_game()
