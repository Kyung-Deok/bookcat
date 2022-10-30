import pandas as pd
import requests
from bs4 import BeautifulSoup

for i in range(1, 5):
    res = requests.get('https://kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=0&orderClick=DAA&mallGb=KOR&linkClass=A&targetPage=' + str(i))
    soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find_all('ul', class_='list_type01'))
    barcode_list = list(soup.find_all(attrs={"name": "barcode"}))

# 바코드를 모두 리스트화
    b = []
    for j in range(0, 50):
        v = barcode_list[j]['value']
        b.append(v)
    print(b)


