from bs4 import BeautifulSoup
import requests
import re


i_res = requests.get(f'https://book.interpark.com/api/bestSeller.api?key=9B5ECDD9AF5A32F5973EAC757CB6F1256C686473954F652396AEBF9E1AEDB253&categoryId=100&output=xml')
soup = BeautifulSoup(i_res.text, 'lxml-xml')
# print(soup)

name = soup.find_all('item')
for n in name :
    rname = n.find('title').text
    isbn = n.find('isbn').text
    img = n.find('coverLargeUrl').text
    print(rname, isbn,img)
    