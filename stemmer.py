# -*- coding: utf-8 -*-
from pymystem3 import Mystem
from mean_text_from_url import get_mean_text_without_format
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


def find_unigram_in_url(query, url):
    query_list = text_to_unigram(query)
    text = get_mean_text_without_format(url)
    word_dict = dict()
    for word in query_list:
        word_dict[word] = 0
    
    text_list = text_to_unigram(text)
    for word in text_list:
        if word in query_list:
            word_dict[word] += 1
    return(word_dict)

    
print(find_unigram_in_url('автомобильный видеорегистратор', 'https://new-elektronika.ru/catalog/avtoelektronika-i-tehnika/videoregistratory/'))