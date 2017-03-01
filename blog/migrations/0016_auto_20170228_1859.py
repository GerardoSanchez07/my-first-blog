# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_plublish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plublish',
            name='valuep',
        ),
        migrations.AddField(
            model_name='plublish',
            name='nump',
            field=models.IntegerField(default=0),
        ),
    ]
