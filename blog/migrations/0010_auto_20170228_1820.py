# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_plublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plublish',
            name='nump',
            field=models.IntegerField(default=0),
        ),
    ]
