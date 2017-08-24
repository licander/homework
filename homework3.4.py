# -*- coding: utf-8 -*-
from pprint import pprint
from urllib.parse import urlencode
import requests
token='c47ebd2e2dfab28ecd45605c463e728f3dfbea50783dda0548c5a1a4ef59a7ddbea2fe7c3915e160ed6e0'
url = 'https://oauth.vk.com/authorize'
APP_ID = '6160914'
VERSION = '5.67'

auth_data = {
        'client_id': APP_ID,
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'mobile',
        'scope': 'status',
        'response_type': 'token',
        'v': VERSION,
        }
print('?'.join((url, urlencode(auth_data))))

params = {
        'access_token': token,
        'v': VERSION
        }


response = requests.get('https://api.vk.com/method/status.get', params)
pprint(response.json())
