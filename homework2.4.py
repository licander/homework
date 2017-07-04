# -*- coding: utf-8 -*-
import os

def find_sql_files(dir_path):
    sql_files = []
    for file in os.listdir(dir_path):
        if file[-4:] == '.sql':
            sql_files.append(file)
    return sql_files

def search_in_file(file_name, query):
     with open(file_name) as file:
         text = file.read()
         if text.find(query) == -1:
             return False
         else:
             return True

def search_query_in_files_list(dir_path, query, files_list):
    result_files = []
    for file in files_list:
        if search_in_file(os.path.join(dir_path, file), query):
            result_files.append(file)
    return result_files
         

def main():
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Migrations')
    result_files = find_sql_files(dir_path)
    while True:
        query = input('Введите строку: ')
        result_files = search_query_in_files_list(dir_path, query, result_files)
        print(result_files)
        print('Всего: {}'.format(len(result_files)))

main()
        