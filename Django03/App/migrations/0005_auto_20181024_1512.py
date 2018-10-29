# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-24 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=20)),
                ('g_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=20)),
                ('u_tel', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='g_user',
            field=models.ManyToManyField(to='App.User'),
        ),
    ]