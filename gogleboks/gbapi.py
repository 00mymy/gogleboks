# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:32:05 2016

@author: 00mymy
"""

import requests
#import pprint
import json

search_url = 'https://www.googleapis.com/books/v1/volumes?q='
search_opt = '&maxResults=10'

detail_url = 'https://www.googleapis.com/books/v1/volumes/'
detail_opt = ''

def getGogleBokSearch(search_kw):
    data = requests.get(search_url + search_kw + search_opt)
    binary = data.text
    output = json.loads(binary)
    return output

def getGogleBokDetail(bid):
    data = requests.get(detail_url + bid + detail_opt)
    binary = data.text
    output = json.loads(binary)
    return output
