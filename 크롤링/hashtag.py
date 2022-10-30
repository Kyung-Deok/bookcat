import requests
import re
from bs4 import BeautifulSoup


target_url = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791191114225'
res = requests.get(target_url)

soup = BeautifulSoup(res.text, 'html.parser')
books = soup.find_all('div', class_='detail')

result_hashtag01 = soup.select('.tag_list em')
print(result_hashtag01)

#result01_class01 = soup.select('div', class_='tag_list')
#result01_class02 = result01_class01.select('em')
#print(result01_class02.get_text().strip())

'''
for i in range(9791190977661, 9791191114225):
    res = requests.get('http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=' + str(i))
    soup = BeautifulSoup(res.text, 'html.parser')

    result_hashtag01 = soup.select('.tag_list em')
    print(result_hashtag01)
'''