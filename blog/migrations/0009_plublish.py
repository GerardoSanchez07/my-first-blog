# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_plublish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namep', models.CharField(max_length=30)),
                ('agep', models.CharField(max_length=10)),
                ('valuep', models.BooleanField(default=False)),
                ('nump', models.IntegerField()),
            ],
        ),
    ]
