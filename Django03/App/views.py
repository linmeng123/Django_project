import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Dog, Person, IDCard, Grade, Student, User, Goods


def index(request):
    return render(request,'index.html')


#加狗

def adddog(request):
    dog = Dog()
    dog.d_name = "afu" + str(random.randrange(1000))
    dog.d_age = random.randrange(20)
    dog.d_color = '#' + str(random.randrange(100,1000))
    dog.save()
    return HttpResponse('<p> {} 加进去了</p>'.format(dog.d_name))


def showdog(request):
    dog_list = Dog.myobjects.all()

    str = ''
    for dog in dog_list:
        str += '<p>狗名{} 狗的颜色{} 狗的age:{}</P>'.format(dog.d_name,dog.d_color,dog.d_age)
    return HttpResponse(str)


def addperson(request):
    per = Person()
    per.p_name = 'gui_' + str(random.randrange(50))
    per.p_age = random.randrange(1,101)
    per.save()
    return HttpResponse('{}符合条件，加进去了'.format(per.p_name))

def addcard(request):
    card = IDCard()
    card.i_num = '360424'+str(random.randrange(100000000))
    card.i_addr = "shengzheng"
    per = Person.objects.last()
    card.i_person = per
    card.save()
    return HttpResponse('{}绑定身份证{}成功'.format(per.p_name,card.i_num))
def delperson(request):
    per = Person.objects.last()
    per.delete()
    return HttpResponse("你杀了{}".format(per.p_name))

def getpersoncard(request):
    per = Person.objects.last()
    idcard = per.idcard
    return HttpResponse('身份证号: {} -- 绑定名: {}'.format(idcard.i_num, per.p_name))
def getcardperson(request):
    card = IDCard.objects.last()
    per = card.i_person
    return HttpResponse('身份证{}对应的是姓名:{}, 年龄:{}'.format(card.i_num,per.p_name, per.p_age))

def addgrade(request):
    grade = Grade()
    grade.g_name = 'computer' + str(random.randrange(1,10))
    grade.save()
    return HttpResponse("{}班添加成功".format(grade.g_name))
def addstudent(request):
    stu = Student()
    stu.s_name = 'guilin--' + str(random.randrange(10))
    stu.s_socre = random.randrange(1,101)
    grade = Grade.objects.last()
    stu.s_grade = grade
    stu.save()
    return HttpResponse('{}同学添加到{}成功'.format(stu.s_name,grade.g_name))
def showgrade(request):
    grade_list = Grade.objects.all()
    info = ''
    for grade in grade_list:
        student_list = grade.student_set.all()
        student_str = ''
        for student in student_list:
            student_str += '<p>{}</p>'.format(student.s_name)
        info += '<p>班级{} 班级人数{} 人员列表{}</p>'.format(grade.g_name,student_list.count(),student_str)
    return HttpResponse(info)
def showstudent(request):
    students = Student.objects.all()
    str = ''
    for student in students:
        grade = student.s_grade
        str += '<p> 姓名:{}   成绩{}  班级:{}</p>'.format(student.s_name,student.s_socre, grade.g_name)
    return HttpResponse(str)

def adduser(request):
    user = User()
    user.u_name = 'guilin-' + str(random.randrange(1000))
    user.u_tel = random.randrange(10000000000,99999999999)
    user.save()

    return HttpResponse('用户 {} 注册成功!'.format(user.u_name))
def addgoods(request):
    goods = Goods()
    goods.g_name = 'ipad-' + str(random.randrange(1,10))
    goods.g_price = random.randrange(1000,20000)
    goods.save()

    return HttpResponse('添加商品 {} 成功'.format(goods.g_name))
def addcart(request):
    users = User.objects.last()
    goods = Goods.objects.last()
    goods.g_user.add(users)
    goods.save()
    return HttpResponse('<p>{}用户添加{}商品成功</p>'.format(users.u_name,goods.g_name))
def showcart(request):
    users = User.objects.last()
    goods_list = users.Goods_set.all()
    str = '<p>{}的购物车</p>'.format(users.u_name)
    for goods in goods_list:
        str += '<p> 商品名称: {}    商品价格:{} </p>'.format(goods.g_name, goods.g_price)
    return HttpResponse(str)
def addcollect(request):
    goods = Goods.objects.last()
    users_list = goods.g_user.all()
    str = ''
    for users in users_list:
        str += '<p>{}商品被{}用户收藏</p>'.format(goods.g_name,users.u_name)
    return HttpResponse(str)
def showgoods(request):
    goods_list = Goods.objects.all()

    str = '<h1>商品列表</h1>'
    for goods in goods_list:

        # 一个商品 对应 多个用户
        user_list = goods.g_user.all()
        if user_list.count():
            str += '<p> 商品名称:{}   商品价格:{}   收藏数量:{}</p>  '.format(goods.g_name, goods.g_price, user_list.count())
        else:
            str += '<p> 商品名称:{}   商品价格:{} </p>'.format(goods.g_name, goods.g_price)

    return HttpResponse(str)