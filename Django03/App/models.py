from django.db import models
class Dogmanager(models.Manager):
    def all(self):
        return super().all().filter(isdelete = False)
# Create your models here.
class Dog(models.Model):
    d_name = models.CharField(max_length=30)
    d_color = models.CharField(max_length=10)
    d_age = models.IntegerField()
    isdelet = models.BooleanField(default=False)


    myobjects = Dogmanager()


    @classmethod
    def createDog(cls,name,age,color,isdelte=False):
        dog = cls(d_name=name,d_age=age,d_color=color,isdelte=isdelte)
        return dog
    def __str__(self):
        return self.d_name


    #元选项，修改表的一些属性
    class Meta():
        db_table = 'dog'
        ordering = ['d_age']

class Person(models.Model):
    p_name = models.CharField(max_length=60)
    p_age = models.IntegerField()


class IDCard(models.Model):
    i_num = models.CharField(max_length=40)
    i_addr = models.CharField(max_length=256)

    i_person = models.OneToOneField(Person,on_delete=models.SET_NULL,null=True)


class Grade(models.Model):
    g_name = models.CharField(max_length=30)
class Student(models.Model):
    s_name = models.CharField(max_length=20)
    s_socre = models.IntegerField()

    s_grade = models.ForeignKey(Grade,on_delete=models.SET_DEFAULT,default=1)

class User(models.Model):
    u_name = models.CharField(max_length=20)
    u_tel = models.CharField(max_length=20)
class Goods(models.Model):
    g_name = models.CharField(max_length=20)
    g_price = models.IntegerField()

    g_user = models.ManyToManyField(User)