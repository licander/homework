# -*- coding: utf-8 -*-
import os
import subprocess

def find_photo(dir_path):
    photo = []
    for file in os.listdir(dir_path):
        photo.append(file)
    return photo

def resize(file_name, start_dir):
    dir_path = os.path.join(start_dir, 'convert')
    path_start_photo = os.path.join(start_dir, 'Source', file_name)
    path_finish_photo = os.path.join(start_dir, 'Result', file_name)
    subprocess.run(dir_path + ' ' + path_start_photo +' -resize 200 ' + path_finish_photo)
    
def main():
    start_dir = os.path.dirname(os.path.realpath(__file__))
    photo_list = find_photo(os.path.join(start_dir, 'Source'))
    for photo in photo_list:
        resize(photo, start_dir)

main()
        