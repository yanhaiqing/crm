# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-21 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20190621_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='identity',
            new_name='role',
        ),
    ]
