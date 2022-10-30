from django.http import JsonResponse
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import re
from random import sample
from pprint import pprint
from config.env_settings import CERT_KEY
from .models import Dashboard
from accounts.models import User
import cwaling.book_cosine_data2 as word2vec

# from models import Book_data
# Create your views here.
# from models import Book_data
# Create your views here.


def index(request):
    context = {}

    # s_id 세션변수 값이 없다면 '' 을 넣어라
    context['s_id'] = request.session.get('s_id', '')
    context['s_name'] = request.session.get('s_name', '')
    # username = request.COOKIES.get('username')
    # password = request.COOKIES.get('password')

    k_namelist = []
    kb = []
    # k_datelist = []
    k_res = requests.get(
        'https://kyobobook.co.kr/bestSellerNew/bestseller.laf?range=1&kind=0&orderClick=DAA&mallGb=KOR&linkClass=A&targetPage=1')
    soup = BeautifulSoup(k_res.text, 'html.parser')

    books = soup.find_all('div', class_='detail')
    barcode_list = list(soup.find_all(attrs={"name": "barcode"}))

    # 바코드를 모두 리스트화
    for j in range(0, 10):
        v = barcode_list[j]['value']
        kb.append(v)

    for j in books:
        name = j.find('strong').text
        all_name = j.find('div', class_='author').text

        author_name = re.sub(r"[\n\t\s]*", '', all_name, 0).strip()
        author_name = re.sub('<span.*?>.*?</span>', '', author_name, 0, re.I | re.S).replace("|", " ")
        author_name = author_name.split(" ")

        author = author_name[0]
        publisher = author_name[1]
        date = author_name[2]
        # names = f'{name}, {author}, {publisher}, {date}'
        k_namelist.append(name)
    zzip = dict(zip(kb, k_namelist))

    # 인터파크
    i_namelist = []
    i_b = []
    i_img = []
    i_res = requests.get(f'https://book.interpark.com/api/bestSeller.api?key={CERT_KEY}&categoryId=100&output=xml')
    soup = BeautifulSoup(i_res.text, 'lxml-xml')
    name = soup.find_all('item')

    for n in name:
        iname = n.find('title').text
        ib = n.find('isbn').text
        img = n.find('coverLargeUrl').text

        i_namelist.append(iname)
        i_b.append(ib)
        i_img.append(img)

    context['range'] = range(5)

    context['k_namelist'] = k_namelist[0:5]
    context['k_bookid'] = kb[0:5]

    context['i_namelist'] = i_namelist[0:5]
    context['i_bookid'] = i_b[0:5]
    context['i_imgurl'] = i_img[0:5]

    return render(request, 'user/index.html', context)


def bookdetail(request, bookid):
    context = {}

    context['bookid'] = bookid

    context['k_name'] = request.GET.get('kname')
    context['k_img'] = request.GET.get('kimg')

    context['i_name'] = request.GET.get('iname')
    context['i_img'] = request.GET.get('iimg')

    # s_id 세션변수 값이 없다면 '' 을 넣어라
    context['s_id'] = request.session.get('s_id', '')
    context['s_name'] = request.session.get('s_name', '')
    # User.objects.update(userpick=context['k_name'])

    user = User.objects.filter(username=context['s_id'])
    user.update(userpick=context['k_name'])

    # context['bookname'] =
    # return JsonResponse(context)
    return render(request, 'user/book.html', context)


def map(request):
    return render(request, 'user/seoul_map.html')



import cwaling.book_cosine_data2 as word2vec
import pandas as pd
def words(request):
    if request.method == "GET":
        sid = request.session.get('s_id', None)
        context = {}
        pickname = User.objects.filter(username=sid).first()
        print(sid)
        print(pickname)

        if pickname == None:
            context['message'] = '접근 에러'
            # return render(request, redirect('/'), context)
            return JsonResponse(context)

        # 자료 불러오기
        #시간 여유되면 이것도 db에 저장해놓기
        df =  pd.read_excel('yes24_data.xlsx')
        
        #자료 불러오기
        
        # recobook = word2vec.recommendations(pickname.userpick)

        recobook = word2vec.recommendations(str(pickname.userpick))
        recobooks = recobook[0:5]
        context['range'] = range(5)
        context['out_img'] = df[df['name'].isin(recobooks)]['image'].values
        context['outid'] = df[df['name'].isin(recobooks)]['ISBN'].values
        context['output'] = recobooks[0:5]
        print(context['out_img'])
        
        return render(request,'modeltest.html', context)

def survey(request):
    return render(request, 'user/survey.html')


def create(request):
    #Dashboard 모델로 객체 생성
    dashboard = Dashboard()

    dashboard.name = request.POST['name']
    dashboard.age = request.POST['age']
    dashboard.readingvolume = request.POST['readingvolume']
    dashboard.visit = request.POST['visit']
    dashboard.genre = request.POST['genre']
    dashboard.cost = request.POST['cost']

    dashboard.save()

    return redirect('dashboard')

def dashboard(request):

    context = {}
    dashboards = Dashboard.objects.all()
    # 독서량 데이터
    volumelist = []
    volumec = []
    volumecount = []
    for i in dashboards:
        volumelist.append(i.readingvolume)
    vset = set(volumelist)
    volumelist = list(vset)

    for x in dashboards:
        volumec.append(x.readingvolume)

    for j in volumelist:
        volumecount.append(volumec.count(j))

    context['volumelist'] = volumelist
    context['volumec'] = volumec
    context['volumecount'] = volumecount

    visitlist = []
    visitc = []
    visitcount = []
    for i in dashboards:
        visitlist.append(i.visit)
    visitset = set(visitlist)
    visitlist = list(visitset)

    for x in dashboards:
        visitc.append(x.visit)

    for j in visitlist:
        visitcount.append(visitc.count(j))

    context['visitlist'] = visitlist
    context['visitc'] = visitc
    context['visitcount'] = visitcount

    genrelist = []
    genrec = []
    genrecount = []
    for i in dashboards:
        genrelist.append(i.genre)
    gset = set(genrelist)
    genrelist = list(gset)

    for x in dashboards:
        genrec.append(x.genre)

    for j in genrelist:
        genrecount.append(genrec.count(j))

    context['genrelist'] = genrelist
    context['genrec'] = genrec
    context['genrecount'] = genrecount

    costlist = []
    costc = []
    costcount = []
    for i in dashboards:
        costlist.append(i.cost)
    cset = set(costlist)
    costlist = list(cset)

    for x in dashboards:
        costc.append(x.cost)

    for j in costlist:
        costcount.append(costc.count(j))

    context['costlist'] = costlist
    context['costc'] = costc
    context['costcount'] = costcount

    return render(request, 'user/dashboard.html', context)

