import csv


def create_pack():

    name = input('Введите название пака: ')
    authors = input('Введите авторов пака: ')
    date = input('Введите дату создания пака: ')
    r_num = int(input('Введите количество раундов: '))

    pack = [[name, authors, date, r_num]]

    for round in range(r_num):
        round_data = []

        round_name = input('Введите название раунда: ')
        quest_num = int(input('Введите количество вопросов: '))
        filename = input('Введите название файла заставки раунда: ')

        pack.append(['!round', round_name, quest_num, filename])

        for i in range(quest_num):
            quest = input('Введите вопрос: ')
            var1 = input('Введите 1-й вариант: ')
            var2 = input('Введите 2-й вариант: ')
            var3 = input('Введите 3-й вариант: ')
            var4 = input('Введите 4-й вариант: ')
            pack.append([quest, var1, var2, var3, var4])

    print(pack)
    return pack


def main():

    filename = input('Введите имя файла: ')
    new_file = open(filename + '.csv', mode='w', newline='')
    writer = csv.writer(new_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    new_pack = create_pack()
    print(new_pack)
    for row in new_pack:
        writer.writerow(row)
    new_file.close()

main()
