import random
import requests
import json


def truth():
    '''
    Правда
    :return:
    '''
    file = open("truth.txt", encoding="windows-1251")
    lines = file.readlines()
    n = random.randint(0, len(lines) - 1)
    file.close()
    return lines[n]


def dare():
    '''
    Действие
    :return:
    '''
    file = open("dare.txt", encoding="utf8")
    lines = file.readlines()
    n = random.randint(0, len(lines) - 1)
    file.close()
    return lines[n]


def append_truth(question):
    '''
    Добавить правду
    :param question:
    :return:
    '''
    file = open("truth.txt", encoding="latin-1")
    lines = file.readlines()
    lines.append(' '.join(question) + '\n')
    file.close()
    f = open("truth.txt", 'w', encoding='latin-1')
    for i in range(len(lines)):
        f.write(lines[i])
    f.close()


def append_dare(action):
    '''
    Добавить действие
    :param action:
    :return:
    '''
    file = open("dare.txt", encoding="latin-1")
    lines = file.readlines()
    lines.append(' '.join(action) + '\n')
    file.close()
    f = open("dare.txt", 'w', encoding='latin-1')
    for i in range(len(lines)):
        f.write(lines[i])
    f.close()


def get_quote():
    '''
    Рандомная цитата
    :return:
    '''
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote
