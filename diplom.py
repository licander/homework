# -*- coding: utf-8 -*-
from urllib.parse import urlencode
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
        'count': 1000,
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
    return res


def get_general_friends():
    my_friends = get_friends_set()
    general_friends = set()
    for num, friend_id in enumerate(my_friends):
        print(friend_id)
        res = get_friends_set(friend_id)
        if res != 1:
            if num == 0:
                general_friends = get_friends_set(friend_id)
                continue
            else:
                friends = get_friends_set(friend_id)
                if friends != 1:
                    general_friends = general_friends & friends
        sleep(0.34)
    return(general_friends)

print(get_groups('5030613'))
# {167837}
