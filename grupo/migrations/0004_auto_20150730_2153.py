# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0003_auto_20150730_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
