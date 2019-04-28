# coding: utf-8
import requests
from bs4 import BeautifulSoup
from TyphoonList import *
from pprint import pprint


def getTyphoonInformation(index): 
    typhoon_dic = {}
    typhoon_arr = []
    res = requests.get('http://typ.kma.go.kr/TYPHOON/ko/weather/typhoon_06_pop.jsp?' +\
                       'json={%22typYear%22:' +\
                       str(int(index / 100)) +\
                       ',%22typSeq%22:' +\
                       str(index % 100) + '}')
    
    soup = BeautifulSoup(res.content, 'html.parser')    
    title = soup.select('div > h1.searchH1')
    typhoon_dic['name'] = title[0].get_text().strip()
    contents = soup.select('div.table_area > table > tbody > tr > td')
    
    num = 0    
    for cnt in contents:
        num = num + 1
        if (num % 11 == 1) :
            typhoon_inf = {}
            typhoon_inf['Date'] = cnt.get_text().strip()
        elif (num % 11 == 2) : 
            typhoon_inf['latitude'] = cnt.get_text().strip()
        elif (num % 11 == 3) :
            typhoon_inf['longitude'] = cnt.get_text().strip()
            typhoon_arr.append(typhoon_inf)
        
        
    typhoon_dic['information'] = typhoon_arr
    
    return typhoon_dic

def callTyphoonInformation(index_arr):
    typhoons_list = []
    
    for idx in index_arr:
        typhoons_list.append(getTyphoonInformation(idx))

    return typhoons_list

