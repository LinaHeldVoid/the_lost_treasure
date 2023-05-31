from pprint import pprint

"""построчное чтение сценария"""
with open('text/scenario.txt', 'r', encoding='utf-8') as text:
    scenario = {}
    i = 1
    for index, line in enumerate(text):
        scenario[index] = line

pprint(scenario)
