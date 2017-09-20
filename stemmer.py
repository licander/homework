# -*- coding: utf-8 -*-
from pymystem3 import Mystem
from mean_text_from_url import get_mean_text_without_format
from unique_text import get_serp
import numpy as np
text = get_mean_text_without_format('http://grand-lux.ru/shop/UID_18221.html')

def text_to_unigram(text):
    m = Mystem()
    lemmas = m.lemmatize(text)
    bad_symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', ';', ':', '"', '\'', ',', '.', '\n', ' \n', ' ',
                   '! ', '; ', ': ', '"', '\'', ', ', '. ')
    for i, lemma in enumerate(lemmas):
        if lemma in bad_symbols:
            del lemmas[i]
    return(lemmas)


def find_unigram_in_url(query_list, url):
    text = get_mean_text_without_format(url)
    word_dict = dict()
    for word in query_list:
        word_dict[word] = 0
        
    if (type(text) == int):
        return(word_dict)
    
    text_list = text_to_unigram(text)
    for word in text_list:
        if word in query_list:
            word_dict[word] += 1
    return(word_dict)

def get_top_mediana(query):
    query_list = text_to_unigram(query)
    serp = get_serp(query, '213', 10)
    res = dict()
    for word in query_list:
        res[word] = list()
    for url in serp:
        unigrams = find_unigram_in_url(query_list, url)
        for word in query_list:
            res[word].append(unigrams[word])
    for word, data in res.items():
        res[word] = np.median(data)
    return(res)
 
queries = ['ремонт квартир',
        'ремонт квартир под ключ',
        'ремонт квартир в москве',
        'элитный ремонт квартир',
        'ремонт квартир цены',
        'стоимость ремонта квартиры',
        'ремонт квартир под ключ цена',
        'капитальный ремонт квартир',
        'капитальный ремонт квартиры цена',
        'капитальный ремонт квартир под ключ',
        'дизайнерский ремонт квартир',
        'дизайнерский ремонт квартир под ключ',
        'дизайнерский ремонт квартир в москве',
        'косметический ремонт квартир',
        'косметический ремонт квартир в москве',
        'косметический ремонт в квартире цена',
        'строительство коттеджей',
        'строительство коттеджей под ключ',
        'строительство коттеджей москва',
        'строительство коттеджей цены',
        'строительство коттеджей под ключ цены',
        'стоимость строительства коттеджа',
        'дизайн проект квартиры',
        'проект квартиры цены',
        'проект ремонта квартиры',
        'дизайн проект квартиры цены',
        'проектирование квартиры',
        'проектирование дизайна квартиры',
        'проектирование квартир москва',
        'проект коттежда',
        'проект коттеджа цена',
        'проекты загородных коттеджей',
        'проектирование коттеджей',
        'проектирование коттеджей москва',
        'стоимость проектирования коттеджа',
        'проектирование коттеджа цена',
        'ремонт коттеджей',
        'ремонт коттеджей под ключ',
        'ремонт коттеджей цены',
        'ремонт офисов',
        'ремонт офисов москва',
        'ремонт офисов цена',
        'ремонт офисов под ключ',
        'дизайн проект офиса',
        'дизайн проект офиса',
        'проект офиса москва',
        'проект ремонта офиса',
        'генеральный подряд',
        'генеральный подряд строительство',
        'генеральный подряд стоимость',
        'услуги генерального подряда'
        ]

for query in queries:
    data = get_top_mediana(query)
    with open('text_analiz.csv', 'a', encoding='utf-8') as f:
        for word in data:        
            f.write(word)
            f.write(';')
        f.write('\n')
        for word in data:        
            f.write(str(data[word]))
            f.write(';')
        f.write('\n')
