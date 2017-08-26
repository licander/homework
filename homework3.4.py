# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import requests
from time import sleep

token='32f45264a89d42fdbadc17d5a051dcab9beaf55473e03564f476426564308de4ac70abbc3c32998d45518'
url = 'https://oauth.vk.com/authorize'
APP_ID = '6160914'
VERSION = '5.67'

auth_data = {
        'client_id': APP_ID,
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'mobile',
        'scope': 'friends',
        'response_type': 'token',
        'v': VERSION,
        }
# print('?'.join((url, urlencode(auth_data))))


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
    print(res)
    if res.get('error'):
        return 1
    friend_set = set()
    for friend in res['response']['items']:
        friend_set.add(friend['id'])
    return friend_set


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

print(get_general_friends())
# {167837}
