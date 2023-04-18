from django.shortcuts import render, HttpResponse
from app01.models import UserInfo


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def user_list(request):
    user = [
        {'name': "DoubleHappy"},
        {'name': 'Xfish'},
        {'name': 'hkp'}
    ]
    print(request.GET)
    print(request.POST)
    return render(request, 'show.html', {'n1': user})


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")

    user_name = request.POST.get('username')
    password = request.POST.get('password')
    if user_name == "root" and password == '123':
        return HttpResponse('登陆成功')
    else:
        return HttpResponse("登录失败")
