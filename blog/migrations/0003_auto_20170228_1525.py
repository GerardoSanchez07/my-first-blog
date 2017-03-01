# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_plublish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plublish',
            old_name='age',
            new_name='agep',
        ),
        migrations.RenameField(
            model_name='plublish',
            old_name='name',
            new_name='namep',
        ),
    ]
