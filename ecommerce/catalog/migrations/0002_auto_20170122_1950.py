# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
