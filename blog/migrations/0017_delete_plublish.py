# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170228_1859'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Plublish',
        ),
    ]
