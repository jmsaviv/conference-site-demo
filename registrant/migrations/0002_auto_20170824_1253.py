# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registrant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrant',
            name='date_of_registration',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrant',
            name='card_type',
            field=models.CharField(choices=[('AE', 'AE'), ('MC', 'MC'), ('V', 'V')], max_length=15),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='meals',
            field=models.CharField(choices=[('mealpack', 'mealpack'), ('dinnerday2', 'dinnerday2')], max_length=30),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='session1',
            field=models.CharField(choices=[('Workshop A', 'Workshop A'), ('Workshop B', 'Workshop B'), ('Workshop C', 'Workshop C')], max_length=30),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='session2',
            field=models.CharField(choices=[('Workshop D', 'Workshop D'), ('Workshop E', 'Workshop E'), ('Workshop F', 'Workshop F')], max_length=30),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='session3',
            field=models.CharField(choices=[('Workshop G', 'Workshop G'), ('Workshop H', 'Workshop H'), ('Workshop I', 'Workshop I')], max_length=30),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='title',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Ms.', 'Ms.'), ('Mr.', 'Mr.')], max_length=3),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='website',
            field=models.URLField(max_length=50),
        ),
    ]
