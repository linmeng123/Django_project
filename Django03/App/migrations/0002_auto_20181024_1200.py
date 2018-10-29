# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-24 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_num', models.CharField(max_length=40)),
                ('i_addr', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=60)),
                ('p_age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='idcard',
            name='i_person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.Person'),
        ),
    ]