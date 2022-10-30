#!/usr/bin/env python
# coding: utf-8


import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote


#베스트셀러
URL = 'http://book.interpark.com/api/bestSeller.api'
#신책URL = 'http://book.interpark.com/api/newBook.api'
My_Key = unquote('본인 키')

queryParams = '?' + urlencode({
    quote_plus('key'): My_Key,
    quote_plus('categoryId'): '100'
})
response = requests.get(URL + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')

rows = xmlobj.findAll("item")

rowList = [] #행값
nameList = [] #열이름값
valueList = [] #데이터값

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()
    
    columnsLen = len(columns)
    for j in range(0, columnsLen):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장
        if i == 0:
            nameList.append(columns[j].name)
        # 컬럼값은 모든 행의 값을 저장해야 함
        valueList.append(columns[j].text)
        #valueList.append(eachColumn)
    rowList.append(valueList)
    valueList = []    # 다음 row의 값을 넣기 위해 비워줌(매우 중요!!)
    
result_df = pd.DataFrame(rowList, columns=nameList)
#result_df.head()


result_df.to_csv('korea_book1.csv', encoding='cp949')


