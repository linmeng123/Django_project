from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 首页
from App.models import Cat


def index(request):
    # return HttpResponse('hello world!')

    username = 'Root'
    age = 20

    names = ['张三','李四','王五','赵柳','田七', '王八','老九']

    goods = {
        'icon': 'head.png',
        'name': 'Mac',
        'price': 999
    }

    return render(request, 'index.html', context={'name':username, 'haha':age, 'names':names, 'goods':goods})


def showcat(request):

    cats = Cat.objects.all()

    return render(request, 'showcat.html', context={'cats':cats})


def test1(request):

    return HttpResponse('test1')

def test2(request):
    return HttpResponse('test2')

def test3(request):
    return HttpResponse('test3')