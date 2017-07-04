# -*- coding: utf-8 -*-
import os

def find_sql_files(dir_name):
    sql_files = []
    for file in os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), dir_name)):
        if file[-4:] == '.sql':
            sql_files.append(file)
    return sql_files

def search_in_file(file_name):
     with open(file_name) as file:
         print(type(file.read()))
         
print(find_sql_files('Migrations'))

