# -*- coding: utf-8 -*-
import requests
from time import sleep

token='5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
url = 'https://oauth.vk.com/authorize'
APP_ID = '6160914'
VERSION = '5.67'


def get_friends_set(user_id=''):
    params = {
        'access_token': token,
        'v': VERSION,
        'count': 10,
        'fields': 'nickname',
        }
    if user_id:
        params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    res = response.json()
    if res.get('error'):
        return 1
    friend_set = set()
    for friend in res['response']['items']:
        friend_set.add(friend['id'])
    return friend_set


def get_groups(user_id):
    params = {
        'access_token': token,
        'user_id': user_id,
        'v': VERSION,
        'count': 1000,
        'extended': 0
        }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    res = response.json()
    if res.get('error'):
        return 1
    group_set = set(res['response']['items'])
    return group_set


def get_friends_group():
    my_friends = get_friends_set('5030613')
    friends_group = set()
    for num, friend_id in enumerate(my_friends):
        res = get_groups(friend_id)
        if res != 1:
            if num == 0:
                friends_group = get_groups(friend_id)
                continue
            else:
                groups = get_groups(friend_id)
                if groups != 1:
                    friends_group = friends_group | groups
        sleep(0.34)
    return(friends_group)


def get_group_info(id):
    params = {
        'access_token': token,
        'group_id': id,
        'v': VERSION,
        'fields': 'members_count,',
        }
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    res = response.json()
    result_dict = {
            'name': res['response'][0]['name'],
            'gid': res['response'][0]['id'],
            'members_count': res['response'][0]['members_count'],
            }
    return(result_dict)
 
    
def get_only_my_group():
    my_group = get_groups('5030613')
    friends_group = get_friends_group()
    my_group -= friends_group
    result_list = []
    for group_id in my_group:
        print(group_id)
        group_info = get_group_info(group_id)
        result_list.append(group_info)
    return result_list
    
print(get_only_my_group())

