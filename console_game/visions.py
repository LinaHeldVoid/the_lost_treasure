import time
import random
import threading

from sound_manager import sight_1, sight_2, sight_3
from scenario_generator import generate_base
from console_game.service_functions import print_effect as p_e, sound_effect as s_e, wrong_input as w, \
    quit_menu as q, random_no as r_n, numbers_check as n_c, determination_announcement as d_a, \
    new_determination, death_menu, print_help, sound_interrupt as s_i


def set_generator(line):
    i = 0
    g = generate_base('text/9_visions.txt')
    while i < line:
        next(g)
        i += 1
    return g


# калькулятор событий
def check_probability(sight, determination, move, spell=None):

    # определяем вероятность в зависимости от решимости
    sight = sight
    determination = determination
    result = False
    bonus = 0
    d = {}
    if sight == 1:
        if determination > 40:
            probability = 90
        elif determination < 31:
            probability = 60
        else:
            probability = 75
    elif sight == 2:
        if move == 1:
            if spell == 1:
                if determination > 40:
                    probability = 90
                elif determination < 31:
                    probability = 70
                else:
                    probability = 80
            elif spell == 2:
                if determination > 40:
                    probability = 85
                elif determination < 31:
                    probability = 55
                else:
                    probability = 70
            else:
                if determination > 40:
                    probability = 80
                elif determination < 31:
                    probability = 40
                else:
                    probability = 60
        elif move == 2:
            if determination > 40:
                probability = 75
            elif determination < 31:
                probability = 45
            else:
                probability = 60
        else:
            if determination > 40:
                probability = 70
            elif determination < 31:
                probability = 40
            else:
                probability = 55
    else:
        if move == 1:
            if determination > 40:
                probability = 65
            elif determination < 31:
                probability = 45
            else:
                probability = 55
        elif move == 2:
            if determination > 40:
                probability = 70
            elif determination < 31:
                probability = 30
            else:
                probability = 50
        else:
            if determination > 40:
                probability = 60
            elif determination < 31:
                probability = 15
            else:
                probability = 35

    # кидаем кубик
    dice = random.randint(0, 100)
    if probability >= dice:
        result = True

    # определяем бонус в зависимости от результата
    # успех
    if result:
        operation = '+'
        if sight == 1:
            if move == 1:
                bonus = 3
            else:

                # этот вариант всегда неудачный
                operation = '-'
                bonus = 5
        elif sight == 2:
            if move == 1:
                if spell == 1:
                    bonus = 3
                elif spell == 2:
                    bonus = 5
                else:
                    bonus = 7
            elif move == 2:
                bonus = 2
            else:
                bonus = 0
        else:
            if move == 1:
                bonus = 4
            elif move == 2:
                bonus = 5
            else:
                bonus = 4

    # провал
    else:
        operation = '-'
        if sight == 1:
            if move == 1:
                bonus = 2
            else:
                bonus = 5
        elif sight == 2:
            if move == 1:
                bonus = 2
            elif move == 2:
                bonus = 3
            else:
                bonus = 5
        else:
            if move == 1:
                bonus = 8
            elif move == 2:
                bonus = 9
            else:
                bonus = 10

    d['bonus'] = bonus
    d['operation'] = operation
    return d


# провальные проверки для 2 видения
# провал по касту заклинания
def magic_fail(t_settings, v_p_settings):
    g = set_generator(127)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)

    record = s_e('sound/voice_person/visions/S2_2_4.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record.stop() if v_p_settings else None

    return


# провал по другим действиям
def non_magic_fail(t_settings, v_p_settings):
    g = set_generator(177)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)

    record = s_e('sound/voice_person/visions/S2_fail.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record.stop() if v_p_settings else None

    return


# получение кары в третьем видении
def abyss_fail(t_settings, v_p_settings):
    g = set_generator(235)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)

    record = s_e('sound/voice_person/visions/S3_death.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record.stop() if v_p_settings else None

    return


# первое видение
def case_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination):
    sight_1.set_volume(0.1)
    sight_1.play(-1) if m_settings else None

    report = {}

    g = set_generator(0)
    print(next(g))
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')
    next(g)
    p_e(next(g), t_settings)

    record_1 = s_e('sound/voice_person/visions/S1_1.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record_1.stop() if v_p_settings else None

    next(g)
    print('')
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')
    next(g)
    p_e(next(g), t_settings)

    record_1 = s_e('sound/voice_person/visions/S1_2.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record_1.stop() if v_p_settings else None

    while True:
        g = set_generator(31)
        print(f'1) {next(g)}'
              f'2) {next(g)}' + '\n')
        option = input('Введите цифру: ')
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
            dice_result = check_probability(1, determination, 1)
        elif option == '2':
            dice_result = check_probability(1, determination, 2)
        else:
            print(w(t_settings, v_a_settings))
            continue

        if dice_result['operation'] == '+':
            g = set_generator(42)

            p_e(next(g), t_settings)
            next(g)
            p_e(next(g), t_settings)
            p_e(next(g), t_settings)

            record_1 = s_e('sound/voice_person/visions/S1_3.ogg', v_p_settings, 2)
            s_i() if not t_settings and v_p_settings else None
            record_1.stop() if v_p_settings else None

        else:
            g = set_generator(49)
            p_e(next(g), t_settings)
            p_e(next(g), t_settings)

            record_1 = s_e('sound/voice_person/visions/S1_4.ogg', v_p_settings, 2)
            s_i() if not t_settings and v_p_settings else None
            record_1.stop() if v_p_settings else None

        new_number = new_determination(t_settings, v_p_settings, v_a_settings, m_settings, s_settings,
                                       determination, dice_result['bonus'], dice_result['operation'])
        report['determination'] = new_number
        report['outcome'] = dice_result['operation']
        sight_1.fadeout(3)
        time.sleep(3) if m_settings else None
        return report


# второе видение
def case_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination):
    sight_2.set_volume(0.15)
    sight_2.play(-1) if m_settings else None

    break_point = False
    dice_result = {}
    report = {}

    g = set_generator(60)
    print(next(g))
    next(g)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')
    next(g)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')
    next(g)
    p_e(next(g), t_settings)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')

    record_2 = s_e('sound/voice_person/visions/S2_1.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record_2.stop() if v_p_settings else None

    while True:
        if break_point:
            break
        g = set_generator(74)
        print(f'1) {next(g)}'
              f'2) {next(g)}' 
              f'3) {next(g)}' + '\n')
        option = input('Введите цифру: ')
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

        # кастуем заклинание
        elif option == '1':
            g = set_generator(79)
            p_e(next(g), t_settings)
            next(g)
            p_e(next(g), t_settings)
            next(g)
            p_e(next(g), t_settings)
            p_e(next(g), t_settings)
            print('')

            record_2 = s_e('sound/voice_person/visions/S2_2.ogg', v_p_settings, 2)
            s_i() if not t_settings and v_p_settings else None
            record_2.stop() if v_p_settings else None

            while True:
                if break_point:
                    break
                g = set_generator(89)
                print(f'1) {next(g)}'
                      f'2) {next(g)}'
                      f'3) {next(g)}' + '\n')
                option = input('Введите цифру: ')
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

                # телекинез
                elif option == '1':
                    break_point = True
                    dice_result = check_probability(2, determination, 1, 1)

                    # успех
                    if dice_result['operation'] == '+':
                        g = set_generator(109)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)

                        record_2 = s_e('sound/voice_person/visions/S2_2_1.ogg', v_p_settings, 2)
                        s_i() if not t_settings and v_p_settings else None
                        record_2.stop() if v_p_settings else None

                    # провал
                    else:
                        magic_fail(t_settings, v_p_settings)
                    break

                # молния
                elif option == '2':
                    break_point = True
                    dice_result = check_probability(2, determination, 1, 2)

                    # успех
                    if dice_result['operation'] == '+':
                        g = set_generator(115)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)

                        record_2 = s_e('sound/voice_person/visions/S2_2_2.ogg', v_p_settings, 2)
                        s_i() if not t_settings and v_p_settings else None
                        record_2.stop() if v_p_settings else None

                    # провал
                    else:
                        magic_fail(t_settings, v_p_settings)
                    break

                # инферно
                elif option == '3':
                    break_point = True
                    dice_result = check_probability(2, determination, 1, 3)

                    # успех
                    if dice_result['operation'] == '+':
                        g = set_generator(121)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)
                        p_e(next(g), t_settings)

                        record_2 = s_e('sound/voice_person/visions/S2_2_3.ogg', v_p_settings, 2)
                        s_i() if not t_settings and v_p_settings else None
                        record_2.stop() if v_p_settings else None

                    # провал
                    else:
                        magic_fail(t_settings, v_p_settings)
                    continue

                else:
                    print(w(t_settings, v_a_settings))
                    break

        # прячем сестру
        elif option == '2':
            break_point = True
            g = set_generator(137)
            p_e(next(g), t_settings)
            next(g)
            p_e(next(g), t_settings)

            record_2 = s_e('sound/voice_person/visions/S2_3.ogg', v_p_settings, 2)
            s_i() if not t_settings and v_p_settings else None
            record_2.stop() if v_p_settings else None

            dice_result = check_probability(2, determination, 2)

            # успех
            if dice_result['operation'] == '+':
                g = set_generator(148)
                p_e(next(g), t_settings)
                next(g)
                p_e(next(g), t_settings)
                p_e(next(g), t_settings)

                record_2 = s_e('sound/voice_person/visions/S2_3_1.ogg', v_p_settings, 2)
                s_i() if not t_settings and v_p_settings else None
                record_2.stop() if v_p_settings else None

            # провал
            else:
                non_magic_fail(t_settings, v_p_settings)
            continue

        # бежим
        elif option == '3':
            break_point = True
            g = set_generator(163)
            p_e(next(g), t_settings)
            next(g)
            p_e(next(g), t_settings)

            record_2 = s_e('sound/voice_person/visions/S2_4.ogg', v_p_settings, 2)
            s_i() if not t_settings and v_p_settings else None
            record_2.stop() if v_p_settings else None

            dice_result = check_probability(2, determination, 3)

            # успех
            if dice_result['operation'] == '+':
                g = set_generator(174)
                p_e(next(g), t_settings)

                record_2 = s_e('sound/voice_person/visions/S4_1.ogg', v_p_settings, 2)
                s_i() if not t_settings and v_p_settings else None
                record_2.stop() if v_p_settings else None

            # провал
            else:
                non_magic_fail(t_settings, v_p_settings)
            continue

        else:
            print(w(t_settings, v_a_settings))
            continue

    new_number = new_determination(t_settings, v_p_settings, v_a_settings, m_settings, s_settings,
                                   determination, dice_result['bonus'], dice_result['operation'])
    report['determination'] = new_number
    report['outcome'] = dice_result['operation']
    sight_2.fadeout(3)
    time.sleep(3) if m_settings else None
    return report


# третье видение
def case_3(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination):
    sight_3.set_volume(0.1)
    sight_3.play(-1) if m_settings else None

    break_point = False
    dice_result = {}
    report = {}

    g = set_generator(187)
    print(next(g))
    next(g)
    p_e(next(g), t_settings)
    next(g)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    print('')
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    p_e(next(g), t_settings)
    next(g)

    record_3 = s_e('sound/voice_person/visions/S3_1.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record_3.stop() if v_p_settings else None

    print('')
    p_e(next(g), t_settings)
    print('')

    record_3_1 = s_e('sound/voice_person/visions/203.ogg', v_p_settings, 2)
    s_i() if not t_settings and v_p_settings else None
    record_3_1.stop() if v_p_settings else None

    while True:
        if break_point:
            break

        g = set_generator(205)
        print(f'1) {next(g)}'
              f'2) {next(g)}' 
              f'3) {next(g)}' + '\n')
        option = input('Введите цифру: ')
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

        # умоляем сущность
        elif option == '1':
            break_point = True
            dice_result = check_probability(3, determination, 1)
            g = set_generator(216)
            p_e(next(g), t_settings)
            next(g)
            p_e(next(g), t_settings)
            p_e(next(g), t_settings)

            record_3_2 = s_e('sound/voice_person/visions/216.ogg', v_p_settings, 2)
            s_i() if not t_settings and v_p_settings else None
            record_3_2.stop() if v_p_settings else None

            # успех
            if dice_result['operation'] == '+':
                g = set_generator(223)
                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

            # провал
            else:
                g = set_generator(231)
                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

                next(g)
                abyss_fail(t_settings, v_p_settings)
            continue

        # сопротивляемся сущности
        elif option == '2':
            break_point = True
            dice_result = check_probability(3, determination, 2)

            g = set_generator(251)
            p_e(next(g), t_settings)

            next(g)
            p_e(next(g), t_settings)

            # успех
            if dice_result['operation'] == '+':
                g = set_generator(256)
                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

                p_e(next(g), t_settings)

                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

            # провал
            else:
                g = set_generator(265)
                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

                p_e(next(g), t_settings)

                abyss_fail(t_settings, v_p_settings)
            continue

        # в ужасе молчим
        elif option == '3':
            break_point = True
            dice_result = check_probability(3, determination, 3)

            g = set_generator(285)
            p_e(next(g), t_settings)

            # успех
            if dice_result['operation'] == '+':
                g = set_generator(288)
                p_e(next(g), t_settings)
                next(g)
                p_e(next(g), t_settings)
                p_e(next(g), t_settings)
                next(g)
                p_e(next(g), t_settings)

            # провал
            else:
                g = set_generator(298)
                p_e(next(g), t_settings)

                next(g)
                p_e(next(g), t_settings)

                abyss_fail(t_settings, v_p_settings)
            continue
        else:
            print(w(t_settings, v_a_settings))
            continue

    new_number = new_determination(t_settings, v_p_settings, v_a_settings, m_settings, s_settings,
                                   determination, dice_result['bonus'], dice_result['operation'])
    report['determination'] = new_number
    report['outcome'] = dice_result['operation']
    sight_3.fadeout(3)
    time.sleep(3) if m_settings else None
    return report


# определяем количество провалов и считаем новую решимость
def poison_effect(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination):
    final_report = {}
    fail_count = 0

    report_1 = case_1(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination)
    if report_1['outcome'] == '-':
        fail_count += 1
    determination = report_1['determination']
    report_2 = case_2(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination)
    if report_2['outcome'] == '-':
        fail_count += 1
    determination = report_2['determination']
    report_3 = case_3(t_settings, v_a_settings, v_p_settings, m_settings, s_settings, determination)
    if report_3['outcome'] == '-':
        fail_count += 1
    determination = report_3['determination']

    final_report['determination'] = determination
    final_report['fails'] = fail_count
    return final_report
