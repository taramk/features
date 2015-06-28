# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20150625_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
