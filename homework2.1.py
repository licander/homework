# -*- coding: utf-8 -*-

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  cook_book = get_cook_book('cook_book.txt')
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
        for line in file:
            dish = line.strip()
            count_ingridient = int(file.readline())
            ingridients_list = []
            for _ in range(count_ingridient):
                ingridient = get_dict_from_str(file.readline())
                ingridients_list.append(ingridient)
            cook_book[dish] = ingridients_list
    return cook_book
            
def get_dict_from_str(ingridient_str):
    ingridient_str = ingridient_str.strip()
    ingridient_list = ingridient_str.split(' | ')
    ingridient_dict = {'ingridient_name': ingridient_list[0], \
                       'quantity': int(ingridient_list[1]),\
                       'measure': ingridient_list[2]}
    return ingridient_dict

create_shop_list()
