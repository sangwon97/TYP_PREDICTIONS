#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup

index = [201825, 201824, 201819, 201818, 201807, 201718, 201705,201703, 201618,\
         201616, 201515, 201512, 201511, 201511, 201509, 201419, 201412, 201411, 201408]
'''
factor Crawling 하는데 2013년 기록은 존재하지 않아서 삭제

          201324, 201315, 201304, 201216, 201215, 201214, 201210, 201207, 201112,\
          201109, 201105, 201009, 201007, 201004, 200807, 200711, 200705, 200704,\
          200613, 200610, 200603, 200514, 200418, 200416, 200415, 200410, 200407,\
          200314, 200310, 200306, 200304, 200215, 200209, 200208, 200205, 200111]
'''


def getTyphoonName(index): 
    typhoon_name = []
    for idx in index:
        res = requests.get('http://typ.kma.go.kr/TYPHOON/ko/weather/typhoon_06_pop.jsp?' +\
                           'json={%22typYear%22:' +\
                           str(int(idx / 100)) +\
                           ',%22typSeq%22:' +\
                           str(idx % 100) + '}')
        
        soup = BeautifulSoup(res.content, 'html.parser')    
        title = soup.select('div > h1.searchH1')
        fullname = title[0].get_text().strip()
        namesplit = []
        namesplit = fullname.split('(')[1].split(')')[0]
        typhoon_name.append(namesplit)
        #typhoon_name.append(name)
    
    return typhoon_name

name_index = []
beforeNameIndex = getTyphoonName(index)

for idx in beforeNameIndex:
    name_index.append(idx.replace("-",""))    


name_index[0] = 'KONGREY2'
name_index[8] = 'CHABA2'
name_index[15] = 'NAKRI2'

