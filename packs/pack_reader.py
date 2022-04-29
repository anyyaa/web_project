import csv


def load_pack(filename):
    '''
    Загрузить пак из csv
    :param filename:
    :return:
    '''
    file = open(filename, mode='r', encoding='windows-1251')
    reader = csv.reader(file, delimiter=';', quotechar='"')
    data = list(reader)

    rounds_num = int(data[0][3])
    pack_name = data[0][0]
    date = data[0][2]
    authors = data[0][1]

    greet_string = [pack_name, authors, date, rounds_num]
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


gs, quiz = load_pack('test1.csv')
print(gs, quiz)
