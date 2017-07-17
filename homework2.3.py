# -*- coding: utf-8 -*-
import chardet
import json


def read_from_file(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        coding = chardet.detect(data)
        data = data.decode(coding['encoding'])
        data = json.loads(data)
    return data['rss']['channel']['items']


def find_popular_words(list_of_data):
    dictionary = {}
    for new in list_of_data:
        text_list = new['title'].split() + new['description'].split()
        for word in text_list:
            if len(word) > 6:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1

    def l(x): return x[1]
    word_sort_list = sorted(dictionary.items(), key=l, reverse=True)
    return word_sort_list


def print_results(word_sort_list):
    for i in range(0, 10):
        print(word_sort_list[i])


def main(file_name):
    data = read_from_file(file_name)
    word_sort_list = find_popular_words(data)
    print('Результаты для файла {}'.format(file_name))
    print_results(word_sort_list)

main('newsafr.json')
main('newscy.json')
main('newsfr.json')
main('newsit.json')
