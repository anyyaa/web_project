from googletrans import Translator


translator = Translator()


def translate(text, lang):
    '''
    Переводчик
    :param text:
    :param lang:
    :return:
    '''
    text = ' '.join(text)
    try:
        text = int(text)
        return f'Некорректные входные данные. Повторите ввод'
    except:
        res = translator.translate(text, dest=lang)
        return res.text
