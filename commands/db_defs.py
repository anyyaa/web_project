import sqlite3


def db_loadpacks():
    '''
    Загрузить список паков
    :return:
    '''
    con = sqlite3.connect("database/packs.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM packs_list""").fetchall()
    con.close()
    return '\n'.join([elem[1] for elem in result])


def db_getfilename(pack_name):
    '''
    Получить по названию пака его файл
    :param pack_name:
    :return:
    '''
    con = sqlite3.connect("database/packs.db")
    cur = con.cursor()
    result = cur.execute(f"""SELECT file_name FROM packs_list
    WHERE pack_name='{pack_name}'""").fetchall()
    con.close()
    return result[0][0]


def update_results(packname, username, score):
    '''
    Обновить таблицу рекордов
    :param packname:
    :param username:
    :param score:
    :return:
    '''
    con = sqlite3.connect("database/packs.db")
    cur = con.cursor()
    users = cur.execute(f"""SELECT username FROM results""").fetchall()
    usernames = []
    for user in users:
        usernames.append(user[0])
    if username in usernames:
        cur.execute(f"""UPDATE results
SET {packname} = '{score}'
WHERE username = '{username}' AND {packname} < '{score}'""")
    con.commit()
    con.close()

