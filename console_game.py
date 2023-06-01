import pygame
import time
from pprint import pprint
from read_scenario import scenario
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
    intro_1 = scenario[1]
    intro_2 = scenario[2]
    begin = scenario[5]
    entrance = scenario[8]

    """алгоритм"""
    print_effect(intro_1)
    time.sleep(2)
    print_effect(intro_2)
    time.sleep(2)
    print_effect(begin)
    time.sleep(2)
    print_effect(entrance)
    time.sleep(2)


def room_1():

    """перевод сценария в переменные"""
    enter = scenario[11] + scenario[12]
    room_examined = scenario[15]
    bowl_examined = scenario[19] + scenario[20]
    painful_death = scenario[23]
    bowl_not_lifted = scenario[26]
    chest_examined = scenario[29]
    stonewall_examined = scenario[32]
    stone_examined = scenario[35]
    key_found = scenario[38]
    chest_opened = scenario[41]
    need_to_think = scenario[49]
    twig_attempt = scenario[52]
    twig_failure = scenario[53] + scenario[54] + scenario[55]
    no_rope = scenario[58]
    no_glass = scenario[61]
    took_diamond = scenario[64]
    lets_smash = scenario[67]
    wall_smashed = scenario[68] + scenario[69] + scenario[70] + scenario[71]
    trapped = scenario[74] + scenario[75]
    decision = scenario[78]

    look_around = scenario[14]
    examine_bowl = scenario[18]
    get_coin = scenario[22]
    lift_bowl = scenario[25]
    examine_chest = scenario[28]
    examine_stonewall = scenario[31]
    examine_stone = scenario[34]
    move_stone = scenario[37]
    open_chest = scenario[40]
    twig = scenario[43]
    rope = scenario[44]
    sledgehammer = scenario[45]
    diamond = scenario[46]
    glass = scenario[47]
    get_coin_twig = scenario[51]
    take_the_rope = scenario[57]
    take_the_glass = scenario[60]
    take_the_brilliant = scenario[63]
    smash_the_wall = scenario[66]
    to_room_2 = scenario[84]

    """алгоритм"""
    chest_is_opened = False
    stonewall_is_examined = False
    print_effect(enter)
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
            while True:
                print_effect(bowl_examined)
                print(f'1) {get_coin}'
                      f'2) {lift_bowl}'
                      f'3) <Отойти от чаши>' + '\n')
                option = input('Введите цифру: ')
                if option == '1':
                    while True:
                        room_1_mp3.stop()
                        print_effect(painful_death)
                        dd_mp3.play(-1)
                        option = input('Введите цифру: ')
                        if option == '1':
                            dd_mp3.stop()
                            room_1_mp3.play(-1)
                            break
                        elif option == '2':
                            exit()
                        else:
                            print(wrong_input())
                            continue
                    continue
                elif option == '2':
                    print_effect(bowl_not_lifted)
                    break
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
                          f'6) <Покинуть сундук>')
                    option = input('Введите цифру: ')
                    if option == '1':
                        while True:
                            print(f'1) {get_coin_twig}'
                                  f'2) <Отложить прут>' + '\n')
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
                        print_effect(no_rope)
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
                                    room_1_mp3.stop()
                                    dd_mp3.play()
                                    print_effect(trapped)
                                    time.sleep(10)
                                    return
                                else:
                                    print(wrong_input())
                                    continue
                        else:
                            print_effect(no_rope)
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
                      f'2) <Отойти от камня>' + '\n')
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
pprint(scenario)
run_the_game()
