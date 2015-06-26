# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='request',
            new_name='feature',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
