import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

# 책 제목 4페이지까지
for i in range(1, 5):
    res = requests.get('https://kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=0&orderClick=DAA&mallGb=KOR&linkClass=A&targetPage=' + str(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    books = soup.find_all('div', class_='detail')

    for j in books:
        name = j.find('strong').text
        all_name = j.find('div', class_='author').text


        author_name = re.sub(r"[\n\t\s]*", '', all_name, 0).strip()
        author_name = re.sub('<span.*?>.*?</span>', '', author_name, 0, re.I | re.S).replace("|", " ")
        author_name = author_name.split(" ")
        author = author_name[0]
        publisher =author_name[1]
        date = author_name[2]

        pprint(f'{name}, {author}, {publisher}, {date}')


