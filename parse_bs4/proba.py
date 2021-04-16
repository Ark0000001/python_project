# import requests      # Библиотека для отправки запросов
# import numpy as np   # Библиотека для матриц, векторов и линала
# import pandas as pd  # Библиотека для табличек
# import time          # Библиотека для тайм-менеджмента
#
# import socks
# import socket
#
# page_link = 'https://86safe.ru/'
# response = requests.get(page_link)
# print(response)
#
# for key, value in response.request.headers.items():
#     print(key+": "+value)

name1 = 'шкаф ПРАКТИК LS-11-40D,5030'
name2 = 'Сейф оружейный Aiko Чирок 1320,6530'

def dict1(s):
    d = dict()
    a = ''
    i = 0
    while i < len(s):
        a = s[i].split(',')
        d[a[i]] = a[i + 1]
        i + 2
    return d

print(h=dict1(name1))
