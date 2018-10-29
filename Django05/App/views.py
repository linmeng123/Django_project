from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User


def index(request):
    return render(request,'index.html')



def datail(request,a,b,c):
    return HttpResponse('对头')


def requesttext(request):
    name = request.GET.get('name')
    return HttpResponse(name)


def register(request):
    if request.method == 'GET': # 获取注册页面
        return render(request, 'register.html')
    elif request.method == 'POST':  # 注册操作
        # 获取客户端传入的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        print(username,password,tel)

        # 存入数据库
        user = User()
        user.username = username
        user.password = password
        user.tel = tel
        user.save()

        # 重定向首页
        response = redirect('app:index')

        # 状态保持
        response.set_cookie('username', username)

        # return HttpResponse('注册成功')
        return response


def login(request):
    if request.method == 'GET': # 获取登录页面
        return render(request, 'login.html')
    elif request.method == 'POST':  # 登录操作
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        # 验证
        # 数据库能找到，登录成功
        # 数据库找不到，登录失败
        users = User.objects.filter(username=username).filter(password=password)
        if users.count():   # 存在
            user = users.first()

            # 重定向首页
            response = redirect('app:index')

            # 设置cookie
            response.set_cookie('username', user.username)

            return response

        else:   # 不存在
            return HttpResponse('用户名或密码错误!')


def cart(request):
    username = request.COOKIES.get('username')

    return render(request,'cart.html',context={'username':username})

def showcookie(request):
    username = request.COOKIES.get('username')
    return render(request,'index.html',context={'username':username})




def logout(request):
    response = redirect('app:index')
    response.delete_cookie('username')
    return response


def jisuanqi(request):
    return render(request,'计算器.html')
