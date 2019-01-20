# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-20 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('description', models.CharField(max_length=222)),
                ('password', models.CharField(max_length=222)),
                ('photo_url', models.CharField(max_length=222, null=True)),
                ('phone', models.CharField(max_length=22, null=True)),
                ('coord_x', models.DecimalField(decimal_places=10, max_digits=10)),
                ('coord_y', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222, null=True)),
                ('photo_url', models.CharField(max_length=22, null=True)),
                ('description', models.CharField(max_length=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('giving', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=222, null=True)),
                ('count', models.IntegerField(default=1)),
                ('status', models.IntegerField(default=1)),
                ('cafe_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Cafe')),
                ('dish', models.ManyToManyField(to='app.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('surname', models.CharField(max_length=222)),
                ('phone', models.CharField(max_length=222)),
                ('password', models.CharField(max_length=222)),
                ('card', models.CharField(blank=True, max_length=222, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.User'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='dish',
            field=models.ManyToManyField(to='app.Dish'),
        ),
    ]