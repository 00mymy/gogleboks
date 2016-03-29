# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 11:32:05 2016

@author: 00mymy
"""

import requests
import json

#from bs4 import BeautifulSoup
#import urllib

search_url = 'https://www.googleapis.com/books/v1/volumes'
search_opt = '&maxResults=10&printType=books'

detail_url = 'https://www.googleapis.com/books/v1/volumes/'
detail_opt = ''

def getGogleBokSearch(search_kw, startIndex):
    data = requests.get(search_url + '?q=' + search_kw + '&startIndex=' + str(startIndex) + search_opt)
    binary = data.text
    output = json.loads(binary)
    return output

def getGogleBokDetail(bid):
    data = requests.get(detail_url + bid + detail_opt)
    binary = data.text
    output = json.loads(binary)
    return output

def getGogleBokSearchMoreabout(search_kw):
    data = requests.get(search_url + '?q=' + search_kw + search_opt)
    binary = data.text
    output = json.loads(binary)
    return output

'''
def getSimilarBooks(infoLink):
    #req = urllib.request.Request(infoLink)
    #res = urllib.request.urlopen(req)
    #data = res.read()
    data = requests.get(infoLink)
    soup = BeautifulSoup(data.text, "lxml")
    #raw_text = soup.find_all('h3' )
    raw_text = soup.find_all("div", id="scroll_atb")
    return raw_text
'''
