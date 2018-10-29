import io
import random

from django.http import HttpResponse
from django.shortcuts import render

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



# Create your views here.
def index(request):

    return render(request, 'index.html')


def test1(request):
    return HttpResponse('测试数据-反向解析操作')


def home(request):

    # 默认这是当做普通字符串处理
    # 默认会自动转义
    str = '<h1> 今天是周四! </h1>'

    return render(request, 'home.html', context={'str':str})


def cart(request):
    return render(request, 'cart.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


# 导入绘图模块 pip install Pillow
from PIL import Image,ImageDraw,ImageFont
def verifycode(request):
    # 创建图片
    width = 100
    height = 50
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    image = Image.new('RGB', (width, height), (r,g,b))


    # 随机数
    str = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    rand_str = ''
    for i in range(0,4):
        temp = random.randrange(0,len(str))
        rand_str += str[temp]


    # 保存随机数，后续为验证
    # session


    # 创建画笔
    draw = ImageDraw.Draw(image)

    # 添加噪点
    for i in range(0,300):
        xy = (random.randrange(0,width), random.randrange(0,height))
        fill = (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))
        draw.point(xy, fill=fill)

    # 导入字体
    # font = ImageFont.truetype('static/fonts/STXINGKA.ttf', 40)
    font = ImageFont.truetype('static/fonts/Fangsong.ttf', 40)

    # 字体颜色
    fontcolor1 = (255, random.randrange(0,256), random.randrange(0,256))
    fontcolor2 = (255, random.randrange(0, 256), random.randrange(0, 256))
    fontcolor3 = (255, random.randrange(0, 256), random.randrange(0, 256))
    fontcolor4 = (255, random.randrange(0, 256), random.randrange(0, 256))


    # 绘制操作
    draw.text((5,3), rand_str[0], fill=fontcolor1,font=font)
    draw.text((25, 3), rand_str[1], fill=fontcolor2, font=font)
    draw.text((45, 3), rand_str[2], fill=fontcolor3, font=font)
    draw.text((65, 3), rand_str[3], fill=fontcolor4, font=font)

    # 释放
    del draw

    #文件操作
    buff = io.BytesIO()
    image.save(buff, 'png') # 保存在内存中

    return HttpResponse(buff.getvalue(), 'image/png')