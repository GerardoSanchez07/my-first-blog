# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170228_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plublish',
            name='nump',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='plublish',
            name='valuep',
            field=models.BooleanField(),
        ),
    ]
