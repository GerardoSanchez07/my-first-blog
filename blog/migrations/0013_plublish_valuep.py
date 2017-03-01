# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170228_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='plublish',
            name='valuep',
            field=models.BooleanField(default=False),
        ),
    ]
