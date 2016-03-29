# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sites', '0001_squashed_0002_site_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='precedence',
            field=models.FloatField(default=0, max_length=128),
        ),
    ]
