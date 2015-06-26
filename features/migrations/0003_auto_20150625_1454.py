# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20150623_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='feature',
            name='customers',
            field=models.ManyToManyField(related_name=b'features', to=b'features.Customer'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='jira_id',
            field=models.IntegerField(unique=True, null=True),
        ),
    ]
