# Create your views here.
from email import message
from itertools import starmap
import re
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from datetime import datetime

# from requests import session
from .models import User
 
 
# def index(request):
#     context = {}
#     # s_id 세션변수 값이 없다면 '' 을 넣어라
#     context['s_id'] = request.session.get('s_id', '')
#     context['s_name'] = request.session.get('s_name', '')
#     # username = request.COOKIES.get('username')
#     # password = request.COOKIES.get('password')
 
#     return render(request, 'user/index.html', context)
 
 
def register(request):
    if request.method == "GET":
        return render(request, 'user/register.html')
    elif request.method == "POST":
        context = {} 
        username = request.POST.get("username",None)
        password = request.POST.get("password", None)
        fullname = request.POST.get("fullname", None)
        useremail = request.POST.get("useremail", None)
 
        # 회원가입 중복체크
        idcheck = User.objects.filter(username=username)
        if idcheck.exists():
            context['message'] = f"Error! {username} 가 중복됩니다."
            return render(request, 'user/register.html', context, status=400)

        elif not(username or password or fullname or useremail) :
            context['message'] = "빈칸없이 작성해 주세요."
            return render(request, 'user/register.html', context, status=400)
        
        else:
            password = password.encode('utf-8')
            password_crypt = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                username=username, password=password_crypt,  fullname=fullname, useremail=useremail,
                create_at=datetime.now(), update_at=datetime.now()
            )
            context['message'] =f"{fullname}님 회원가입 되었습니다."
            return render(request, 'user/index.html', context, status=200)
 
 
def login(request):
    if request.method == "GET":
        kk = request.session.get('s_id', False)
        if kk is not False :
            context={}
            context['message']= '접근 에러'
            # return render(request, redirect('/'), context)
            return redirect('/')
        return render(request, 'user/login.html')
    elif request.method == "POST":
        context = {}
 
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # 로그인 체크하기
        idcheck = User.objects.filter(username=username).first()
        
        # print(username + '/' + idcheck.password)
        # print(idcheck)

        # try :
        #     if idcheck == None :
        #         context['message'] = '일치하는 회원이 없습니다.'
        #         if idcheck.password == None:
        #             context['message'] = '비밀번호 입력해주세요'
        #             return render(request, 'user/login.html', context, status=400)
        #         return render(request, 'user/login.html', context, status=400)
        #     elif not bcrypt.checkpw(password.encode('utf-8'), idcheck.password.encode('utf-8')) :
        #         context['message'] = '비밀번호가 일치하지 않습니다.'
        #         return render(request, 'user/login.html', context, status=400)
            
        #     context['s_id'] = username
        #     context['s_name'] = idcheck.fullname
        #     context['message'] = f"{idcheck.fullname}님 로그인 하셨습니다."
        #     # redirect('/')
        #     return render(request, 'user/index.html', context, status=200)
            
        # except AttributeError:
        #     context['message']=' 아이디와 패스워드를 입력해주세요'
        #     # if username is None :
        #     #     context['message']=' 아이디 로그인 에러'
        #     # elif password is None:
        #     #     context['message'] = '비밀번호 에러'
        #     return render(request, 'user/login.html', context, status=401)
 
        if idcheck is not None:
     
            # OK - 로그인
            request.session['s_id'] = username
            request.session['s_name'] = idcheck.fullname
 
            if not bcrypt.checkpw(password.encode('utf-8'), idcheck.password.encode('utf-8')) :

                context['message'] = '비밀번호가 존재하지 않습니다. '
                return render(request, 'user/login.html', context, status=400)
            
            context['s_id'] = username
            context['s_name'] = idcheck.fullname
            # context['message'] = f"{idcheck.fullname} 님이 로그인하셨습니다."
            render(request, 'user/index.html', context,status=200)
            return redirect('/')
 
        else:
     
            context['message'] = "로그인 정보를 올바르게 입력해주세요"
            return render(request, 'user/login.html', context)
 
 
def logout(request):
    request.session.flush()
    return redirect('/')
