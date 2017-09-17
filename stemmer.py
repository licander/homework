# -*- coding: utf-8 -*-
from pymystem3 import Mystem
text = "Чему стоит научить ребёнка в первом классе. В начальной школе иногда важнее не умение читать или писать, \
а другие вещи. Например, стоит рассказать ребёнку, как бороться со скукой на уроках и насилием со стороны учителей, \
которое может выражаться вовсе не в физической форме."

def text_to_unigram(text):
    m = Mystem()
    lemmas = m.lemmatize(text)
    bad_symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', ';', ':', '"', '\'', ',', '.', '\n', ' ',
                   '! ', '; ', ': ', '"', '\'', ', ', '. ')
    for i, lemma in enumerate(lemmas):
        if lemma in bad_symbols:
            del lemmas[i]
    print(lemmas)

    
text_to_unigram(text)