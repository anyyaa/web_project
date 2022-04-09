import csv
from pprint import pprint


def load_pack(filename):
    file = open(filename, mode='r', encoding='utf-8')
    reader = csv.reader(file, delimiter=';', quotechar='"')
    data = list(reader)

    rounds_num = int(data[0][1])
    pack_name = data[0][0]
    date = data[0][3]
    authors = data[0][2]

    greet_string = f'Пак {pack_name}, создатели: {authors}, дата создания: {date}, количество раундов: {rounds_num}'
    quiz = []
    delta = 0

    for round in range(rounds_num):

        round_title = data[1 + delta]
        quest_num = int(round_title[2])
        round_data = [round_title]

        for i in range(1 + delta + 1, 1 + delta + quest_num + 1):
            round_data.append(data[i])

        delta += quest_num + 1
        quiz.append(round_data)

    return greet_string, quiz
