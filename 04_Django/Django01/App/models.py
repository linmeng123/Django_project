from django.db import models

# Create your models here.


# 基础类
class Animal(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()

    # 默认这里也会创建一个表

    # 抽象化
    # 父类不会生成表单
    class Meta:
        abstract = True

# 狗 模型类
class Dog(Animal):
    bark = models.CharField(max_length=40)

# 猫
class Cat(Animal):
    sleep = models.CharField(max_length=40)

