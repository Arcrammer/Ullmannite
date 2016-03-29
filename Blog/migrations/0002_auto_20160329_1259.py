# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='date_posted',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='header',
        ),
        migrations.AddField(
            model_name='blog',
            name='last_edited',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
