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
    print(res)
    
get_top_mediana('автомобильный видеорегистратор')
