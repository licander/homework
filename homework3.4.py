# -*- coding: utf-8 -*-
import requests
import chardet


def translate_it(text, lang):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def read_from_file(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        coding = chardet.detect(data)
        data = data.decode(coding['encoding'])
    return data


def main(input_file, output_file, current_lang, new_lang='ru'):
    text = read_from_file(input_file)
    lang = current_lang + '-' + new_lang
    text = translate_it(text, lang)
    with open(output_file, 'w') as file:
        file.write(text)

main('FR.txt', 'FR_new.txt', 'fr')
main('DE.txt', 'DE_new.txt', 'de')
main('ES.txt', 'ES_new.txt', 'es')
