# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170228_1708'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Plublish',
        ),
    ]
