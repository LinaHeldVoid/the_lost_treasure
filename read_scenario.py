from pprint import pprint

"""построчное чтение сценария"""
with open('../text/1_prologue.txt', 'r', encoding='utf-8') as text:
    prologue = {}
    for index, line in enumerate(text):
        prologue[index] = line

with open('../text/2_room_1.txt', 'r', encoding='utf-8') as text:
    room_1 = {}
    for index, line in enumerate(text):
        room_1[index] = line

with open('../text/3_room_2.txt', 'r', encoding='utf-8') as text:
    room_2 = {}
    i = 1
    for index, line in enumerate(text):
        room_2[index] = line

with open('../text/4_riddle.txt', 'r', encoding='utf-8') as text:
    riddle = {}
    i = 1
    for index, line in enumerate(text):
        riddle[index] = line

with open('../text/5_back_to_room_1.txt', 'r', encoding='utf-8') as text:
    room_1_again = {}
    i = 1
    for index, line in enumerate(text):
        room_1_again[index] = line

with open('../text/6_escape.txt', 'r', encoding='utf-8') as text:
    escape = {}
    i = 1
    for index, line in enumerate(text):
        escape[index] = line

with open('../text/7_epilogue.txt', 'r', encoding='utf-8') as text:
    epilogue = {}
    i = 1
    for index, line in enumerate(text):
        epilogue[index] = line

with open('../text/8_death&determination.txt', 'r', encoding='utf-8') as text:
    dnd = {}
    i = 1
    for index, line in enumerate(text):
        dnd[index] = line


pprint(room_1)
