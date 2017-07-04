# -*- coding: utf-8 -*-
import json 

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  cook_book = get_cook_book('cook_book.json')
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

def get_cook_book(file_name):
    cook_book = {}
    with open(file_name) as file:
        cook_book = json.load(file)
    return cook_book
            

#cook_book = get_cook_book1('cook_book.txt')
#with open('cook_book.json', 'w') as file:
#    json.dump(cook_book, file, indent=2, ensure_ascii=False)
    
create_shop_list()

    
